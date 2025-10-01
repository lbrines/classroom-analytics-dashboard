from fastapi import APIRouter, Depends
from app.services.search_service import SearchService
from app.models.search import SearchQuery, SearchEntityType
from app.schemas.search_schema import SearchRequest
from app.schemas.response_schema import create_success_response
from app.middleware.auth_middleware import get_current_user
from app.models.user import User

router = APIRouter()


def get_search_service():
    """Dependency to get SearchService instance."""
    return SearchService()


@router.post("/search", response_model=dict)
async def search(
    request: SearchRequest,
    current_user: User = Depends(get_current_user),
    search_service: SearchService = Depends(get_search_service)
):
    """
    Search for entities (students, courses, etc).
    
    Requires authentication.
    """
    query = SearchQuery(
        query=request.query,
        entity_type=SearchEntityType(request.entity_type),
        page=request.page,
        page_size=request.page_size
    )
    
    result = search_service.search(query)
    
    # Convert to dict for response
    response_data = {
        "query": result.query,
        "entity_type": result.entity_type,
        "total_results": result.total_results,
        "page": result.page,
        "page_size": result.page_size,
        "total_pages": result.total_pages,
        "results": [r.model_dump() for r in result.results],
        "execution_time_ms": result.execution_time_ms
    }
    
    return create_success_response(response_data).model_dump()

