from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from enum import Enum


class SearchEntityType(str, Enum):
    STUDENT = "student"
    COURSE = "course"
    ASSIGNMENT = "assignment"


class SearchFilter(BaseModel):
    field: str
    operator: str  # eq, contains, gt, lt, in
    value: Any


class SearchQuery(BaseModel):
    query: str
    entity_type: SearchEntityType
    filters: Optional[List[SearchFilter]] = None
    page: int = 1
    page_size: int = 10
    sort_by: Optional[str] = None
    sort_order: str = "asc"


class SearchHighlight(BaseModel):
    field: str
    fragments: List[str]


class SearchResultItem(BaseModel):
    id: str
    entity_type: str
    score: float
    data: Dict[str, Any]
    highlights: Optional[Dict[str, List[str]]] = None


class SearchResult(BaseModel):
    query: str
    entity_type: str
    total_results: int
    page: int
    page_size: int
    total_pages: int
    results: List[SearchResultItem]
    filters_applied: Optional[Dict[str, Any]] = None
    filters_available: Optional[Dict[str, List[Any]]] = None
    execution_time_ms: Optional[float] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "Smith",
                "entity_type": "student",
                "total_results": 15,
                "page": 1,
                "page_size": 10,
                "total_pages": 2,
                "results": [
                    {
                        "id": "student-045",
                        "entity_type": "student",
                        "score": 0.95,
                        "data": {
                            "name": "John Smith",
                            "email": "john.smith@example.com",
                            "status": "at_risk"
                        },
                        "highlights": {
                            "name": ["John <em>Smith</em>"]
                        }
                    }
                ],
                "execution_time_ms": 45.3
            }
        }

