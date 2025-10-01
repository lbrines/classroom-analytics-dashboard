from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class SearchRequest(BaseModel):
    query: str
    entity_type: str = "student"
    page: int = 1
    page_size: int = 10


class SearchResultResponse(BaseModel):
    query: str
    entity_type: str
    total_results: int
    page: int
    page_size: int
    total_pages: int
    results: List[Dict[str, Any]]
    execution_time_ms: Optional[float] = None

