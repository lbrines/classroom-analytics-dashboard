from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional, Dict, Any
from app.services.insights_service import InsightsService
from app.schemas.response_schema import create_success_response
from app.middleware.auth_middleware import get_current_user
from app.models.user import User

router = APIRouter()


def get_insights_service():
    """Dependency to get InsightsService instance."""
    return InsightsService()


@router.get("/insights/metrics", response_model=dict)
async def get_advanced_metrics(
    current_user: User = Depends(get_current_user),
    insights_service: InsightsService = Depends(get_insights_service)
):
    """
    Get advanced metrics and insights for the current user.
    
    Returns comprehensive analytics including trends, correlations, and predictions.
    Requires authentication.
    """
    try:
        metrics = insights_service.get_advanced_metrics(
            user_id=current_user.id,
            role=current_user.role.value
        )
        
        return create_success_response(metrics).model_dump()
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate advanced metrics: {str(e)}"
        )


@router.get("/insights/entity/{entity_type}/{entity_id}", response_model=dict)
async def get_entity_insights(
    entity_type: str,
    entity_id: str,
    current_user: User = Depends(get_current_user),
    insights_service: InsightsService = Depends(get_insights_service)
):
    """
    Get insights for a specific entity (course, student, etc.).
    
    Args:
        entity_type: Type of entity (course, student, etc.)
        entity_id: ID of the entity
        
    Requires authentication.
    """
    try:
        if entity_type == "course":
            insights = insights_service.analyze_course_performance(entity_id)
        elif entity_type == "student":
            insights = [insights_service.predict_student_risk(entity_id)]
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported entity type: {entity_type}"
            )
        
        insights_data = [
            {
                "type": insight.insight_type,
                "entity_id": insight.entity_id,
                "prediction": insight.prediction,
                "confidence": insight.confidence,
                "timeframe": insight.timeframe,
                "factors": insight.factors,
                "recommendation": insight.recommendation
            }
            for insight in insights
        ]
        
        response_data = {
            "entity_type": entity_type,
            "entity_id": entity_id,
            "insights": insights_data,
            "total_insights": len(insights_data)
        }
        
        return create_success_response(response_data).model_dump()
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate entity insights: {str(e)}"
        )


@router.get("/insights/trends", response_model=dict)
async def get_trend_analysis(
    metric: str = Query(..., description="Metric to analyze (completion_rate, engagement_score, etc.)"),
    period_days: int = Query(7, description="Number of days to analyze"),
    current_user: User = Depends(get_current_user),
    insights_service: InsightsService = Depends(get_insights_service)
):
    """
    Get trend analysis for a specific metric.
    
    Args:
        metric: The metric to analyze
        period_days: Number of days to look back
        
    Requires authentication.
    """
    try:
        trend = insights_service.analyze_trends(metric, period_days)
        
        trend_data = {
            "metric": trend.metric,
            "period": trend.period,
            "current_value": trend.current_value,
            "previous_value": trend.previous_value,
            "change_percentage": trend.change_percentage,
            "trend_direction": trend.trend_direction,
            "confidence": trend.confidence
        }
        
        return create_success_response(trend_data).model_dump()
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to analyze trends: {str(e)}"
        )


@router.get("/insights/engagement", response_model=dict)
async def get_engagement_metrics(
    current_user: User = Depends(get_current_user),
    insights_service: InsightsService = Depends(get_insights_service)
):
    """
    Get engagement metrics and analysis.
    
    Returns detailed engagement analytics and trends.
    Requires authentication.
    """
    try:
        # Get engagement trends
        engagement_trend = insights_service.analyze_trends("engagement_score", 14)
        
        # Get correlations related to engagement
        engagement_correlations = insights_service.find_correlations([
            "engagement_score", "completion_rate", "average_grade", "active_students"
        ])
        
        engagement_data = {
            "current_engagement": engagement_trend.current_value,
            "engagement_trend": {
                "direction": engagement_trend.trend_direction,
                "change_percentage": engagement_trend.change_percentage,
                "confidence": engagement_trend.confidence
            },
            "correlations": [
                {
                    "metric": corr.metric2 if corr.metric1 == "engagement_score" else corr.metric1,
                    "correlation_coefficient": corr.correlation_coefficient,
                    "interpretation": corr.interpretation
                }
                for corr in engagement_correlations
                if "engagement_score" in [corr.metric1, corr.metric2]
            ],
            "insights": [
                "High engagement correlates with better completion rates",
                "Interactive content increases student engagement",
                "Regular feedback improves engagement scores"
            ]
        }
        
        return create_success_response(engagement_data).model_dump()
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate engagement metrics: {str(e)}"
        )


@router.get("/insights/predictions", response_model=dict)
async def get_predictions(
    prediction_type: str = Query("student_risk", description="Type of prediction (student_risk, course_performance)"),
    entity_id: Optional[str] = Query(None, description="Entity ID for specific predictions"),
    current_user: User = Depends(get_current_user),
    insights_service: InsightsService = Depends(get_insights_service)
):
    """
    Get predictive insights and forecasts.
    
    Args:
        prediction_type: Type of prediction to generate
        entity_id: Optional specific entity ID
        
    Requires authentication.
    """
    try:
        predictions = []
        
        if prediction_type == "student_risk" and entity_id:
            prediction = insights_service.predict_student_risk(entity_id)
            predictions = [prediction]
        elif prediction_type == "course_performance" and entity_id:
            predictions = insights_service.analyze_course_performance(entity_id)
        else:
            # Generate general predictions based on user role
            if current_user.role.value == "administrator":
                predictions = [
                    insights_service.predict_student_risk("student-001"),
                    insights_service.predict_student_risk("student-002")
                ]
            elif current_user.role.value == "teacher":
                # Get teacher's courses and analyze performance
                from app.services.classroom_service import ClassroomService
                classroom_service = ClassroomService()
                courses = classroom_service.get_courses()
                for course in courses[:2]:
                    course_predictions = insights_service.analyze_course_performance(course.id)
                    predictions.extend(course_predictions)
        
        predictions_data = [
            {
                "type": pred.insight_type,
                "entity_id": pred.entity_id,
                "entity_type": pred.entity_type,
                "prediction": pred.prediction,
                "confidence": pred.confidence,
                "timeframe": pred.timeframe,
                "factors": pred.factors,
                "recommendation": pred.recommendation
            }
            for pred in predictions
        ]
        
        response_data = {
            "prediction_type": prediction_type,
            "predictions": predictions_data,
            "total_predictions": len(predictions_data),
            "generated_at": insights_service._historical_data.get("timestamp", "N/A")
        }
        
        return create_success_response(response_data).model_dump()
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate predictions: {str(e)}"
        )


@router.get("/insights/correlations", response_model=dict)
async def get_correlation_analysis(
    metrics: str = Query("completion_rate,engagement_score,average_grade", description="Comma-separated list of metrics"),
    current_user: User = Depends(get_current_user),
    insights_service: InsightsService = Depends(get_insights_service)
):
    """
    Get correlation analysis between metrics.
    
    Args:
        metrics: Comma-separated list of metrics to analyze
        
    Requires authentication.
    """
    try:
        metric_list = [m.strip() for m in metrics.split(",")]
        correlations = insights_service.find_correlations(metric_list)
        
        correlations_data = [
            {
                "metric1": corr.metric1,
                "metric2": corr.metric2,
                "correlation_coefficient": corr.correlation_coefficient,
                "significance": corr.significance,
                "interpretation": corr.interpretation
            }
            for corr in correlations
        ]
        
        response_data = {
            "analyzed_metrics": metric_list,
            "correlations": correlations_data,
            "total_correlations": len(correlations_data)
        }
        
        return create_success_response(response_data).model_dump()
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to analyze correlations: {str(e)}"
        )


@router.post("/insights/report", response_model=dict)
async def generate_insights_report(
    report_type: str = "comprehensive",
    current_user: User = Depends(get_current_user),
    insights_service: InsightsService = Depends(get_insights_service)
):
    """
    Generate comprehensive insights report.
    
    Args:
        report_type: Type of report to generate (comprehensive, executive, detailed)
        
    Requires authentication.
    """
    try:
        report = insights_service.generate_insights_report(
            user_id=current_user.id,
            role=current_user.role.value,
            report_type=report_type
        )
        
        return create_success_response(report).model_dump()
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate insights report: {str(e)}"
        )

