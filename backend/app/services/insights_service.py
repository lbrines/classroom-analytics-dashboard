import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass
from app.services.metrics_service import MetricsService
from app.services.classroom_service import ClassroomService
from app.services.search_service import SearchService


@dataclass
class TrendAnalysis:
    """Represents trend analysis results."""
    metric: str
    period: str
    current_value: float
    previous_value: float
    change_percentage: float
    trend_direction: str  # 'up', 'down', 'stable'
    confidence: float  # 0-1 confidence score


@dataclass
class PredictiveInsight:
    """Represents predictive analysis insight."""
    insight_type: str
    entity_id: str
    entity_type: str
    prediction: str
    confidence: float
    timeframe: str
    factors: List[str]
    recommendation: str


@dataclass
class CorrelationAnalysis:
    """Represents correlation analysis results."""
    metric1: str
    metric2: str
    correlation_coefficient: float
    significance: float
    interpretation: str


class InsightsService:
    """
    Advanced analytics and insights service.
    Provides predictive analysis, trend detection, and correlation analysis.
    """
    
    def __init__(self):
        """Initialize InsightsService."""
        self.metrics_service = MetricsService()
        self.classroom_service = ClassroomService()
        self.search_service = SearchService()
        
        # Mock historical data for analysis
        self._historical_data = self._generate_mock_historical_data()
    
    def _generate_mock_historical_data(self) -> Dict[str, List[float]]:
        """Generate mock historical data for analysis."""
        # Generate 30 days of mock data
        dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq='D')
        
        # Simulate realistic educational metrics with trends
        np.random.seed(42)  # For reproducible results
        
        return {
            "enrollment_trend": [100 + i + np.random.normal(0, 5) for i in range(len(dates))],
            "completion_rate": [70 + i * 0.2 + np.random.normal(0, 3) for i in range(len(dates))],
            "engagement_score": [75 + i * 0.15 + np.random.normal(0, 4) for i in range(len(dates))],
            "average_grade": [8.0 + i * 0.01 + np.random.normal(0, 0.3) for i in range(len(dates))],
            "active_students": [150 + i * 0.5 + np.random.normal(0, 8) for i in range(len(dates))],
            "assignment_submissions": [200 + i * 0.3 + np.random.normal(0, 15) for i in range(len(dates))]
        }
    
    def analyze_trends(self, metric: str, period_days: int = 7) -> TrendAnalysis:
        """
        Analyze trends for a specific metric.
        
        Args:
            metric: The metric to analyze
            period_days: Number of days to look back
            
        Returns:
            TrendAnalysis object with trend information
        """
        if metric not in self._historical_data:
            # Generate default trend for unknown metrics
            return TrendAnalysis(
                metric=metric,
                period=f"{period_days} days",
                current_value=0.0,
                previous_value=0.0,
                change_percentage=0.0,
                trend_direction="stable",
                confidence=0.0
            )
        
        data = self._historical_data[metric]
        current_period = data[-period_days:]
        previous_period = data[-period_days*2:-period_days] if len(data) >= period_days*2 else data[:period_days]
        
        current_avg = np.mean(current_period)
        previous_avg = np.mean(previous_period)
        
        change_percentage = ((current_avg - previous_avg) / previous_avg * 100) if previous_avg != 0 else 0
        
        # Determine trend direction
        if abs(change_percentage) < 2:
            trend_direction = "stable"
        elif change_percentage > 0:
            trend_direction = "up"
        else:
            trend_direction = "down"
        
        # Calculate confidence based on data consistency
        confidence = min(1.0, max(0.0, 1 - (np.std(current_period) / np.mean(current_period)) if np.mean(current_period) > 0 else 0))
        
        return TrendAnalysis(
            metric=metric,
            period=f"{period_days} days",
            current_value=round(current_avg, 2),
            previous_value=round(previous_avg, 2),
            change_percentage=round(change_percentage, 2),
            trend_direction=trend_direction,
            confidence=round(confidence, 2)
        )
    
    def predict_student_risk(self, student_id: str) -> PredictiveInsight:
        """
        Predict student at-risk status using mock predictive analysis.
        
        Args:
            student_id: The student ID to analyze
            
        Returns:
            PredictiveInsight with risk prediction
        """
        # Mock risk factors analysis
        mock_factors = [
            "assignment_completion_rate",
            "engagement_score",
            "attendance_rate",
            "grade_trend"
        ]
        
        # Simulate risk calculation
        risk_score = np.random.uniform(0, 1)
        
        if risk_score > 0.7:
            prediction = "High risk of academic failure"
            confidence = 0.85
            recommendation = "Immediate intervention recommended. Schedule meeting with student and provide additional support resources."
        elif risk_score > 0.4:
            prediction = "Moderate risk of falling behind"
            confidence = 0.72
            recommendation = "Monitor closely and provide targeted support. Consider study group assignment."
        else:
            prediction = "Low risk, performing well"
            confidence = 0.68
            recommendation = "Continue current support level. Student is on track for success."
        
        return PredictiveInsight(
            insight_type="student_risk",
            entity_id=student_id,
            entity_type="student",
            prediction=prediction,
            confidence=confidence,
            timeframe="next 30 days",
            factors=mock_factors,
            recommendation=recommendation
        )
    
    def analyze_course_performance(self, course_id: str) -> List[PredictiveInsight]:
        """
        Analyze course performance and generate insights.
        
        Args:
            course_id: The course ID to analyze
            
        Returns:
            List of PredictiveInsight objects
        """
        insights = []
        
        # Mock course analysis
        completion_trend = self.analyze_trends("completion_rate", 14)
        engagement_trend = self.analyze_trends("engagement_score", 14)
        
        # Generate insights based on trends
        if completion_trend.trend_direction == "down" and completion_trend.change_percentage < -5:
            insights.append(PredictiveInsight(
                insight_type="course_completion",
                entity_id=course_id,
                entity_type="course",
                prediction=f"Course completion rate declining by {abs(completion_trend.change_percentage):.1f}%",
                confidence=completion_trend.confidence,
                timeframe="current semester",
                factors=["completion_rate", "engagement_score", "assignment_difficulty"],
                recommendation="Review course materials and provide additional support. Consider adjusting assignment difficulty."
            ))
        
        if engagement_trend.trend_direction == "down":
            insights.append(PredictiveInsight(
                insight_type="student_engagement",
                entity_id=course_id,
                entity_type="course",
                prediction=f"Student engagement decreasing by {abs(engagement_trend.change_percentage):.1f}%",
                confidence=engagement_trend.confidence,
                timeframe="current semester",
                factors=["engagement_score", "interaction_rate", "content_quality"],
                recommendation="Increase interactive activities and improve content delivery methods."
            ))
        
        return insights
    
    def find_correlations(self, metrics: List[str]) -> List[CorrelationAnalysis]:
        """
        Find correlations between different metrics.
        
        Args:
            metrics: List of metrics to analyze for correlations
            
        Returns:
            List of CorrelationAnalysis objects
        """
        correlations = []
        
        # Get data for available metrics
        available_metrics = [m for m in metrics if m in self._historical_data]
        
        if len(available_metrics) < 2:
            return correlations
        
        # Calculate correlations between all pairs
        for i in range(len(available_metrics)):
            for j in range(i + 1, len(available_metrics)):
                metric1 = available_metrics[i]
                metric2 = available_metrics[j]
                
                data1 = self._historical_data[metric1]
                data2 = self._historical_data[metric2]
                
                # Calculate correlation coefficient
                correlation_coef = np.corrcoef(data1, data2)[0, 1]
                
                # Determine significance (simplified)
                significance = 1 - abs(correlation_coef)  # Simplified significance
                
                # Interpret correlation
                if abs(correlation_coef) > 0.7:
                    strength = "strong"
                elif abs(correlation_coef) > 0.4:
                    strength = "moderate"
                else:
                    strength = "weak"
                
                direction = "positive" if correlation_coef > 0 else "negative"
                
                interpretation = f"{strength.capitalize()} {direction} correlation between {metric1} and {metric2}"
                
                correlations.append(CorrelationAnalysis(
                    metric1=metric1,
                    metric2=metric2,
                    correlation_coefficient=round(correlation_coef, 3),
                    significance=round(significance, 3),
                    interpretation=interpretation
                ))
        
        return correlations
    
    def get_advanced_metrics(self, user_id: str, role: str) -> Dict[str, Any]:
        """
        Get advanced metrics and insights for a user.
        
        Args:
            user_id: The user ID
            role: The user's role
            
        Returns:
            Dictionary with advanced metrics and insights
        """
        # Get basic metrics
        basic_metrics = self.metrics_service.get_dashboard_metrics(user_id, role)
        
        # Analyze trends for key metrics
        trends = {
            "completion_rate": self.analyze_trends("completion_rate", 7),
            "engagement_score": self.analyze_trends("engagement_score", 7),
            "enrollment_trend": self.analyze_trends("enrollment_trend", 7)
        }
        
        # Get correlation analysis
        key_metrics = ["completion_rate", "engagement_score", "average_grade", "active_students"]
        correlations = self.find_correlations(key_metrics)
        
        # Generate predictive insights based on role
        predictive_insights = []
        
        if role == "teacher":
            # Analyze course performance for teachers
            courses = self.classroom_service.get_courses()
            for course in courses[:2]:  # Analyze first 2 courses
                insights = self.analyze_course_performance(course.id)
                predictive_insights.extend(insights)
        
        elif role == "administrator":
            # System-wide insights for administrators
            predictive_insights.append(PredictiveInsight(
                insight_type="system_performance",
                entity_id="system",
                entity_type="system",
                prediction="System performance is stable with slight improvement in user engagement",
                confidence=0.78,
                timeframe="next 30 days",
                factors=["user_activity", "system_load", "feature_usage"],
                recommendation="Continue current system maintenance schedule. Consider adding new features based on user feedback."
            ))
        
        # Prepare advanced metrics response
        advanced_metrics = {
            "basic_metrics": basic_metrics.model_dump(),
            "trends": {
                metric: {
                    "current_value": trend.current_value,
                    "change_percentage": trend.change_percentage,
                    "trend_direction": trend.trend_direction,
                    "confidence": trend.confidence
                }
                for metric, trend in trends.items()
            },
            "correlations": [
                {
                    "metric1": corr.metric1,
                    "metric2": corr.metric2,
                    "correlation_coefficient": corr.correlation_coefficient,
                    "interpretation": corr.interpretation
                }
                for corr in correlations[:5]  # Top 5 correlations
            ],
            "predictive_insights": [
                {
                    "type": insight.insight_type,
                    "entity_id": insight.entity_id,
                    "prediction": insight.prediction,
                    "confidence": insight.confidence,
                    "timeframe": insight.timeframe,
                    "recommendation": insight.recommendation
                }
                for insight in predictive_insights
            ],
            "analysis_metadata": {
                "generated_at": datetime.now().isoformat(),
                "data_points_analyzed": len(self._historical_data["completion_rate"]),
                "analysis_period": "30 days"
            }
        }
        
        return advanced_metrics
    
    def generate_insights_report(self, user_id: str, role: str, report_type: str = "comprehensive") -> Dict[str, Any]:
        """
        Generate comprehensive insights report.
        
        Args:
            user_id: The user ID
            role: The user's role
            report_type: Type of report to generate
            
        Returns:
            Dictionary with insights report
        """
        advanced_metrics = self.get_advanced_metrics(user_id, role)
        
        # Generate executive summary
        trends = advanced_metrics["trends"]
        positive_trends = [t for t in trends.values() if t["trend_direction"] == "up"]
        negative_trends = [t for t in trends.values() if t["trend_direction"] == "down"]
        
        summary = {
            "overall_performance": "improving" if len(positive_trends) > len(negative_trends) else "declining",
            "key_highlights": [
                f"{trend['current_value']:.1f}% {metric.replace('_', ' ')} (trend: {trend['trend_direction']})"
                for metric, trend in trends.items()
            ],
            "recommendations": [
                insight["recommendation"]
                for insight in advanced_metrics["predictive_insights"]
            ]
        }
        
        report = {
            "report_type": report_type,
            "generated_for": {
                "user_id": user_id,
                "role": role
            },
            "executive_summary": summary,
            "detailed_analysis": advanced_metrics,
            "generated_at": datetime.now().isoformat()
        }
        
        return report

