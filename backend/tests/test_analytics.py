import pytest
from ..services import analytics_service

def test_calculate_engagement_rate():
    # Test with valid data
    likes = 50
    comments = 10
    shares = 5
    impressions = 1000
    
    # Call the function
    result = analytics_service.calculate_engagement_rate(likes, comments, shares, impressions)
    
    # Calculate expected result manually
    expected = ((likes + comments + shares) / impressions) * 100
    expected = round(expected, 2)
    
    # Assertions
    assert result == expected
    assert isinstance(result, float)
    
    # Test with zero impressions
    result_zero = analytics_service.calculate_engagement_rate(likes, comments, shares, 0)
    assert result_zero == 0.0

def test_get_content_performance_metrics():
    # Test content data
    content_data = {
        "id": 1,
        "content_type": "text"
    }
    
    # Test analytics data
    analytics_data = {
        "likes": 42,
        "comments": 5,
        "shares": 3,
        "impressions": 1200,
        "reach": 800
    }
    
    # Call the function
    result = analytics_service.get_content_performance_metrics(content_data, analytics_data)
    
    # Assertions
    assert "likes" in result
    assert "comments" in result
    assert "shares" in result
    assert "impressions" in result
    assert "reach" in result
    assert "engagement_rate" in result
    assert "content_id" in result
    assert "content_type" in result
    
    assert result["likes"] == 42
    assert result["comments"] == 5
    assert result["shares"] == 3
    assert result["impressions"] == 1200
    assert result["reach"] == 800
    assert result["content_id"] == 1
    assert result["content_type"] == "text"
    
    # Check engagement rate calculation
    expected_engagement = ((42 + 5 + 3) / 1200) * 100
    expected_engagement = round(expected_engagement, 2)
    assert result["engagement_rate"] == expected_engagement

def test_compare_performance_to_benchmarks():
    # Test performance data
    performance_data = {
        "content_type": "article",
        "engagement_rate": 4.5
    }
    
    # Call the function
    result = analytics_service.compare_performance_to_benchmarks(performance_data)
    
    # Assertions
    assert "content_type" in result
    assert "content_engagement_rate" in result
    assert "benchmark_engagement_rate" in result
    assert "performance_vs_benchmark" in result
    assert "performance_description" in result
    
    assert result["content_type"] == "article"
    assert result["content_engagement_rate"] == 4.5
    
    # Check benchmark for article content type
    assert result["benchmark_engagement_rate"] == 4.0  # From our implementation
    
    # Check performance comparison
    expected_comparison = 4.5 - 4.0
    assert result["performance_vs_benchmark"] == expected_comparison
    
    # Check performance description
    assert result["performance_description"] == "Above benchmark"
    
    # Test with below benchmark performance
    performance_data_low = {
        "content_type": "text",
        "engagement_rate": 1.5
    }
    
    result_low = analytics_service.compare_performance_to_benchmarks(performance_data_low)
    assert result_low["performance_description"] == "Below benchmark"

def test_generate_performance_insights():
    # Test content analytics data
    content_analytics = [
        {
            "engagement_rate": 4.2,
            "likes": 42,
            "comments": 5,
            "shares": 3,
            "content_type": "text"
        },
        {
            "engagement_rate": 3.8,
            "likes": 38,
            "comments": 8,
            "shares": 2,
            "content_type": "carousel"
        },
        {
            "engagement_rate": 5.1,
            "likes": 56,
            "comments": 12,
            "shares": 7,
            "content_type": "article"
        }
    ]
    
    # Call the function
    result = analytics_service.generate_performance_insights(content_analytics)
    
    # Assertions
    assert "insights" in result
    assert "summary" in result
    assert isinstance(result["insights"], list)
    assert isinstance(result["summary"], dict)
    
    # Check summary
    summary = result["summary"]
    assert "average_engagement_rate" in summary
    assert "average_likes" in summary
    assert "average_comments" in summary
    assert "average_shares" in summary
    assert "best_performing_content" in summary
    
    # Check that average engagement rate is calculated correctly
    engagement_rates = [4.2, 3.8, 5.1]
    expected_avg = sum(engagement_rates) / len(engagement_rates)
    expected_avg = round(expected_avg, 2)
    assert summary["average_engagement_rate"] == expected_avg
    
    # Check best performing content
    best_content = summary["best_performing_content"]
    assert best_content["engagement_rate"] == 5.1
    assert best_content["content_type"] == "article"
    
    # Test with empty data
    result_empty = analytics_service.generate_performance_insights([])
    assert result_empty["insights"] == []
    assert result_empty["summary"] == "No data available"

def test_get_audience_insights():
    # Test content analytics data
    content_analytics = [
        {
            "engagement_rate": 4.2,
            "likes": 42,
            "comments": 5,
            "shares": 3,
            "content_type": "text"
        }
    ]
    
    # Call the function
    result = analytics_service.get_audience_insights(content_analytics)
    
    # Assertions
    assert "peak_engagement_times" in result
    assert "most_engaged_content_types" in result
    assert "audience_growth" in result
    assert "top_comments" in result
    
    # Check that we have the expected data structure
    assert isinstance(result["peak_engagement_times"], list)
    assert isinstance(result["most_engaged_content_types"], list)
    assert isinstance(result["audience_growth"], str)
    assert isinstance(result["top_comments"], list)
    
    # Check that we have some data
    assert len(result["peak_engagement_times"]) > 0
    assert len(result["most_engaged_content_types"]) > 0
    assert len(result["top_comments"]) > 0