import json
import os
import time
from typing import List, Dict, Any, Optional
from app.models.search import SearchQuery, SearchResult, SearchResultItem, SearchEntityType


class SearchService:
    """
    Service for advanced search functionality.
    Supports searching students, courses, and assignments.
    """
    
    def __init__(self):
        """Initialize SearchService."""
        self.students_file = os.path.join(
            os.path.dirname(__file__), "..", "data", "mock_students.json"
        )
        self.users_file = os.path.join(
            os.path.dirname(__file__), "..", "data", "mock_users.json"
        )
        self._students_cache = None
        self._users_cache = None
    
    def _load_students(self) -> List[dict]:
        """Load students from mock data."""
        if self._students_cache is None:
            try:
                with open(self.students_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self._students_cache = data.get("students", [])
            except FileNotFoundError:
                self._students_cache = []
        return self._students_cache
    
    def _load_users(self) -> List[dict]:
        """Load users from mock data."""
        if self._users_cache is None:
            try:
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Filter only student users
                    all_users = data.get("users", [])
                    self._users_cache = [u for u in all_users if u.get("role") == "student"]
            except FileNotFoundError:
                self._users_cache = []
        return self._users_cache
    
    def _search_students(self, query_text: str) -> List[Dict[str, Any]]:
        """
        Search students by name, email, or ID.
        
        Args:
            query_text: The search query
            
        Returns:
            List of matching student records
        """
        students = self._load_students()
        users = self._load_users()
        
        # If empty query, return all
        if not query_text:
            return self._merge_student_data(students[:50])  # Limit to 50
        
        query_lower = query_text.lower()
        matches = []
        
        # Search in students data
        for student in students:
            full_name = student.get("full_name", "").lower()
            email = student.get("email_address", "").lower()
            user_id = student.get("user_id", "").lower()
            
            if (query_lower in full_name or 
                query_lower in email or 
                query_lower in user_id):
                matches.append(student)
        
        # Also search in user data for additional matches
        for user in users:
            user_name = user.get("name", "").lower()
            user_email = user.get("email", "").lower()
            
            if query_lower in user_name or query_lower in user_email:
                # Check if not already in matches
                if not any(s.get("user_id") == user.get("id") for s in matches):
                    # Create student-like structure from user data
                    matches.append({
                        "user_id": user.get("id"),
                        "full_name": user.get("name"),
                        "email_address": user.get("email"),
                        "course_id": None,
                        "profile_id": None
                    })
        
        return matches
    
    def _merge_student_data(self, students: List[dict]) -> List[dict]:
        """Merge student enrollment data with user data."""
        return students  # Simplified for now
    
    def _calculate_score(self, item: dict, query: str) -> float:
        """
        Calculate relevance score for search result.
        
        Args:
            item: The item to score
            query: The search query
            
        Returns:
            Relevance score between 0 and 1
        """
        if not query:
            return 0.5
        
        query_lower = query.lower()
        name = item.get("full_name", "").lower()
        email = item.get("email_address", "").lower()
        
        # Exact match = 1.0
        if query_lower == name or query_lower == email:
            return 1.0
        
        # Starts with = 0.8
        if name.startswith(query_lower) or email.startswith(query_lower):
            return 0.8
        
        # Contains = 0.6
        if query_lower in name or query_lower in email:
            return 0.6
        
        return 0.3
    
    def search(self, query: SearchQuery) -> SearchResult:
        """
        Execute a search query.
        
        Args:
            query: SearchQuery object with search parameters
            
        Returns:
            SearchResult with matching items
        """
        start_time = time.time()
        
        if query.entity_type == SearchEntityType.STUDENT:
            items = self._search_students(query.query)
        else:
            # TODO: Implement search for other entity types
            items = []
        
        # Calculate scores and create results
        results = []
        for item in items:
            score = self._calculate_score(item, query.query)
            result_item = SearchResultItem(
                id=item.get("user_id") or item.get("id"),
                entity_type=query.entity_type.value,
                score=score,
                data=item,
                highlights=self._generate_highlights(item, query.query)
            )
            results.append(result_item)
        
        # Sort by score (descending)
        results.sort(key=lambda x: x.score, reverse=True)
        
        # Apply pagination
        total_results = len(results)
        start_idx = (query.page - 1) * query.page_size
        end_idx = start_idx + query.page_size
        paginated_results = results[start_idx:end_idx]
        
        # Calculate total pages
        total_pages = (total_results + query.page_size - 1) // query.page_size
        
        # Calculate execution time
        execution_time_ms = (time.time() - start_time) * 1000
        
        return SearchResult(
            query=query.query,
            entity_type=query.entity_type.value,
            total_results=total_results,
            page=query.page,
            page_size=query.page_size,
            total_pages=total_pages,
            results=paginated_results,
            execution_time_ms=execution_time_ms
        )
    
    def _generate_highlights(self, item: dict, query: str) -> Optional[Dict[str, List[str]]]:
        """Generate search highlights for matched text."""
        if not query:
            return None
        
        highlights = {}
        query_lower = query.lower()
        
        # Highlight name
        name = item.get("full_name", "")
        if query_lower in name.lower():
            highlighted = name.replace(
                query, f"<em>{query}</em>"
            ).replace(
                query.lower(), f"<em>{query}</em>"
            ).replace(
                query.capitalize(), f"<em>{query.capitalize()}</em>"
            )
            highlights["name"] = [highlighted]
        
        return highlights if highlights else None

