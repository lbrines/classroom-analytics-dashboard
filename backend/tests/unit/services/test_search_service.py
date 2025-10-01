import pytest
from app.services.search_service import SearchService
from app.models.search import SearchQuery, SearchResult, SearchEntityType


class TestSearchService:
    """Test suite for SearchService following TDD methodology."""
    
    @pytest.fixture
    def search_service(self):
        """Create a SearchService instance for testing."""
        return SearchService()
    
    def test_search_students_returns_results(self, search_service):
        """Test that search_students returns SearchResult object."""
        query = SearchQuery(query="Ana", entity_type=SearchEntityType.STUDENT)
        result = search_service.search(query)
        assert isinstance(result, SearchResult)
        assert result.entity_type == "student"
    
    def test_search_students_finds_by_name(self, search_service):
        """Test that search finds students by name."""
        query = SearchQuery(query="Ana", entity_type=SearchEntityType.STUDENT)
        result = search_service.search(query)
        assert result.total_results > 0
        assert len(result.results) > 0
    
    def test_search_students_finds_by_email(self, search_service):
        """Test that search finds students by email."""
        query = SearchQuery(query="student1@", entity_type=SearchEntityType.STUDENT)
        result = search_service.search(query)
        assert result.total_results > 0
    
    def test_search_returns_empty_for_no_matches(self, search_service):
        """Test that search returns empty results for no matches."""
        query = SearchQuery(query="NonExistentStudent123", entity_type=SearchEntityType.STUDENT)
        result = search_service.search(query)
        assert result.total_results == 0
        assert len(result.results) == 0
    
    def test_search_respects_pagination(self, search_service):
        """Test that search respects page and page_size parameters."""
        query = SearchQuery(
            query="",  # Empty query returns all
            entity_type=SearchEntityType.STUDENT,
            page=1,
            page_size=2
        )
        result = search_service.search(query)
        assert len(result.results) <= 2
        assert result.page == 1
        assert result.page_size == 2
    
    def test_search_calculates_total_pages(self, search_service):
        """Test that search calculates total pages correctly."""
        query = SearchQuery(
            query="",
            entity_type=SearchEntityType.STUDENT,
            page_size=2
        )
        result = search_service.search(query)
        expected_pages = (result.total_results + 1) // 2
        assert result.total_pages >= expected_pages
    
    def test_search_execution_time_recorded(self, search_service):
        """Test that search records execution time."""
        query = SearchQuery(query="Ana", entity_type=SearchEntityType.STUDENT)
        result = search_service.search(query)
        assert result.execution_time_ms is not None
        assert result.execution_time_ms >= 0
    
    def test_search_performance_under_500ms(self, search_service):
        """Test that search executes in under 500ms."""
        query = SearchQuery(query="Ana", entity_type=SearchEntityType.STUDENT)
        result = search_service.search(query)
        assert result.execution_time_ms < 500

