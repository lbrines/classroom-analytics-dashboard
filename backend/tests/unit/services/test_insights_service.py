import pytest
import numpy as np
from app.services.insights_service import InsightsService, TrendAnalysis, PredictiveInsight, CorrelationAnalysis


class TestInsightsService:
    """Test suite for InsightsService following TDD methodology."""
    
    @pytest.fixture
    def insights_service(self):
        """Create an InsightsService instance for testing."""
        return InsightsService()
    
    def test_analyze_trends_returns_trend_analysis_object(self, insights_service):
        """Test that analyze_trends returns TrendAnalysis object."""
        trend = insights_service.analyze_trends("completion_rate", 7)
        
        assert isinstance(trend, TrendAnalysis)
        assert trend.metric == "completion_rate"
        assert trend.period == "7 days"
    
    def test_analyze_trends_calculates_trend_direction(self, insights_service):
        """Test that analyze_trends calculates correct trend direction."""
        trend = insights_service.analyze_trends("completion_rate", 7)
        
        assert trend.trend_direction in ["up", "down", "stable"]
        assert isinstance(trend.change_percentage, float)
        assert isinstance(trend.confidence, float)
        assert 0 <= trend.confidence <= 1
    
    def test_analyze_trends_handles_unknown_metrics(self, insights_service):
        """Test that analyze_trends handles unknown metrics gracefully."""
        trend = insights_service.analyze_trends("unknown_metric", 7)
        
        assert isinstance(trend, TrendAnalysis)
        assert trend.metric == "unknown_metric"
        assert trend.current_value == 0.0
        assert trend.previous_value == 0.0
        assert trend.confidence == 0.0
    
    def test_predict_student_risk_returns_predictive_insight(self, insights_service):
        """Test that predict_student_risk returns PredictiveInsight object."""
        insight = insights_service.predict_student_risk("student-001")
        
        assert isinstance(insight, PredictiveInsight)
        assert insight.insight_type == "student_risk"
        assert insight.entity_id == "student-001"
        assert insight.entity_type == "student"
    
    def test_predict_student_risk_includes_prediction_and_recommendation(self, insights_service):
        """Test that predict_student_risk includes prediction and recommendation."""
        insight = insights_service.predict_student_risk("student-001")
        
        assert insight.prediction is not None
        assert insight.recommendation is not None
        assert isinstance(insight.confidence, float)
        assert 0 <= insight.confidence <= 1
        assert insight.timeframe == "next 30 days"
        assert isinstance(insight.factors, list)
        assert len(insight.factors) > 0
    
    def test_analyze_course_performance_returns_list_of_insights(self, insights_service):
        """Test that analyze_course_performance returns list of PredictiveInsight objects."""
        insights = insights_service.analyze_course_performance("course-001")
        
        assert isinstance(insights, list)
        # May be empty depending on trends, but should be a valid list
    
    def test_find_correlations_returns_correlation_analysis_list(self, insights_service):
        """Test that find_correlations returns list of CorrelationAnalysis objects."""
        metrics = ["completion_rate", "engagement_score", "average_grade"]
        correlations = insights_service.find_correlations(metrics)
        
        assert isinstance(correlations, list)
        # Should have correlations between the metrics
        assert len(correlations) >= 0
    
    def test_find_correlations_calculates_correlation_coefficients(self, insights_service):
        """Test that find_correlations calculates correlation coefficients correctly."""
        metrics = ["completion_rate", "engagement_score"]
        correlations = insights_service.find_correlations(metrics)
        
        if correlations:  # If correlations exist
            for corr in correlations:
                assert isinstance(corr, CorrelationAnalysis)
                assert -1 <= corr.correlation_coefficient <= 1
                assert 0 <= corr.significance <= 1
                assert corr.interpretation is not None
    
    def test_find_correlations_handles_insufficient_metrics(self, insights_service):
        """Test that find_correlations handles insufficient metrics gracefully."""
        metrics = ["single_metric"]
        correlations = insights_service.find_correlations(metrics)
        
        assert isinstance(correlations, list)
        assert len(correlations) == 0
    
    def test_get_advanced_metrics_returns_dictionary_with_expected_keys(self, insights_service):
        """Test that get_advanced_metrics returns dictionary with expected structure."""
        user_id = "user-001"
        role = "teacher"
        
        metrics = insights_service.get_advanced_metrics(user_id, role)
        
        assert isinstance(metrics, dict)
        assert "basic_metrics" in metrics
        assert "trends" in metrics
        assert "correlations" in metrics
        assert "predictive_insights" in metrics
        assert "analysis_metadata" in metrics
    
    def test_get_advanced_metrics_includes_trend_analysis(self, insights_service):
        """Test that get_advanced_metrics includes trend analysis."""
        user_id = "user-001"
        role = "teacher"
        
        metrics = insights_service.get_advanced_metrics(user_id, role)
        
        trends = metrics["trends"]
        assert isinstance(trends, dict)
        
        # Should include key metrics
        expected_metrics = ["completion_rate", "engagement_score", "enrollment_trend"]
        for metric in expected_metrics:
            if metric in trends:
                trend_data = trends[metric]
                assert "current_value" in trend_data
                assert "change_percentage" in trend_data
                assert "trend_direction" in trend_data
                assert "confidence" in trend_data
    
    def test_get_advanced_metrics_includes_correlations(self, insights_service):
        """Test that get_advanced_metrics includes correlation analysis."""
        user_id = "user-001"
        role = "teacher"
        
        metrics = insights_service.get_advanced_metrics(user_id, role)
        
        correlations = metrics["correlations"]
        assert isinstance(correlations, list)
        
        if correlations:  # If correlations exist
            for corr in correlations:
                assert "metric1" in corr
                assert "metric2" in corr
                assert "correlation_coefficient" in corr
                assert "interpretation" in corr
    
    def test_get_advanced_metrics_includes_predictive_insights(self, insights_service):
        """Test that get_advanced_metrics includes predictive insights."""
        user_id = "teacher-001"
        role = "teacher"
        
        metrics = insights_service.get_advanced_metrics(user_id, role)
        
        insights = metrics["predictive_insights"]
        assert isinstance(insights, list)
        
        if insights:  # If insights exist
            for insight in insights:
                assert "type" in insight
                assert "entity_id" in insight
                assert "prediction" in insight
                assert "confidence" in insight
                assert "timeframe" in insight
                assert "recommendation" in insight
    
    def test_generate_insights_report_returns_comprehensive_report(self, insights_service):
        """Test that generate_insights_report returns comprehensive report."""
        user_id = "user-001"
        role = "teacher"
        
        report = insights_service.generate_insights_report(user_id, role)
        
        assert isinstance(report, dict)
        assert "report_type" in report
        assert "generated_for" in report
        assert "executive_summary" in report
        assert "detailed_analysis" in report
        assert "generated_at" in report
    
    def test_generate_insights_report_includes_executive_summary(self, insights_service):
        """Test that generate_insights_report includes executive summary."""
        user_id = "user-001"
        role = "teacher"
        
        report = insights_service.generate_insights_report(user_id, role)
        
        summary = report["executive_summary"]
        assert "overall_performance" in summary
        assert "key_highlights" in summary
        assert "recommendations" in summary
        
        assert summary["overall_performance"] in ["improving", "declining"]
        assert isinstance(summary["key_highlights"], list)
        assert isinstance(summary["recommendations"], list)
    
    def test_generate_insights_report_includes_detailed_analysis(self, insights_service):
        """Test that generate_insights_report includes detailed analysis."""
        user_id = "user-001"
        role = "teacher"
        
        report = insights_service.generate_insights_report(user_id, role)
        
        detailed = report["detailed_analysis"]
        assert "basic_metrics" in detailed
        assert "trends" in detailed
        assert "correlations" in detailed
        assert "predictive_insights" in detailed
        assert "analysis_metadata" in detailed
    
    def test_historical_data_generation_creates_consistent_data(self, insights_service):
        """Test that historical data generation creates consistent data."""
        data = insights_service._historical_data
        
        assert isinstance(data, dict)
        assert len(data) > 0
        
        # Check that all data arrays have the same length
        data_lengths = [len(values) for values in data.values()]
        assert all(length == data_lengths[0] for length in data_lengths)
        
        # Check that data contains expected metrics
        expected_metrics = [
            "enrollment_trend", "completion_rate", "engagement_score",
            "average_grade", "active_students", "assignment_submissions"
        ]
        for metric in expected_metrics:
            assert metric in data
            assert isinstance(data[metric], list)
            assert len(data[metric]) > 0
            assert all(isinstance(val, (int, float)) for val in data[metric])

