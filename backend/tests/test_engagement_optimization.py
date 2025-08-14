import pytest
from ..services import engagement_optimization_service

def test_optimize_content_for_engagement():
    # Test content
    content = {
        "title": "Test Post",
        "body": "This is a test post for engagement optimization.",
        "hashtags": ["#AI", "#MachineLearning", "#DataScience"]
    }
    
    # Test analytics data
    analytics = {
        "engagement_rate": 2.5,
        "likes": 25,
        "comments": 3,
        "shares": 2
    }
    
    # Call the function
    result = engagement_optimization_service.optimize_content_for_engagement(content, analytics)
    
    # Assertions
    assert "optimized_content" in result
    assert "suggestions" in result
    assert "predicted_improvement" in result
    
    optimized_content = result["optimized_content"]
    assert "title" in optimized_content
    assert "body" in optimized_content
    assert "hashtags" in optimized_content
    
    suggestions = result["suggestions"]
    assert isinstance(suggestions, list)
    assert len(suggestions) > 0
    
    predicted_improvement = result["predicted_improvement"]
    assert isinstance(predicted_improvement, (int, float))
    assert predicted_improvement >= 0

def test_analyze_content_engagement_factors():
    # Test content
    content = {
        "title": "Test Post",
        "body": "This is a test post for engagement analysis. It contains some information about AI and machine learning.",
        "hashtags": ["#AI", "#MachineLearning", "#DataScience", "#Technology", "#Innovation"]
    }
    
    # Call the function
    result = engagement_optimization_service.analyze_content_engagement_factors(content)
    
    # Assertions
    assert "factors" in result
    assert "engagement_score" in result
    assert "recommendations" in result
    
    factors = result["factors"]
    assert "title_length" in factors
    assert "body_length" in factors
    assert "hashtag_count" in factors
    assert "keywords" in factors
    
    engagement_score = result["engagement_score"]
    assert isinstance(engagement_score, (int, float))
    assert engagement_score >= 0
    assert engagement_score <= 100
    
    recommendations = result["recommendations"]
    assert isinstance(recommendations, list)
    assert len(recommendations) > 0

def test_suggest_hashtag_optimization():
    # Test hashtags
    hashtags = ["#AI", "#MachineLearning", "#DataScience", "#Technology", "#Innovation", "#Future", "#Trends"]
    
    # Test engagement data
    engagement_data = {
        "engagement_rate": 1.8
    }
    
    # Call the function
    result = engagement_optimization_service.suggest_hashtag_optimization(hashtags, engagement_data)
    
    # Assertions
    assert "optimized_hashtags" in result
    assert "suggestions" in result
    assert "predicted_improvement" in result
    
    optimized_hashtags = result["optimized_hashtags"]
    assert isinstance(optimized_hashtags, list)
    assert len(optimized_hashtags) <= 5  # We limit to 5 hashtags
    
    suggestions = result["suggestions"]
    assert isinstance(suggestions, list)
    assert len(suggestions) > 0
    
    # Check if we have suggestions about reducing hashtag count
    assert any("reduce the number of hashtags" in suggestion for suggestion in suggestions)

def test_get_optimal_posting_time():
    # Test user profile with optimal posting times
    user_profile = {
        "optimal_posting_times": ["08:00", "12:00", "18:00"]
    }
    
    # Test content type
    content_type = "article"
    
    # Call the function
    result = engagement_optimization_service.get_optimal_posting_time(user_profile, content_type)
    
    # Assertions
    assert "optimal_time" in result
    assert "explanation" in result
    
    optimal_time = result["optimal_time"]
    assert optimal_time in user_profile["optimal_posting_times"]
    
    explanation = result["explanation"]
    assert isinstance(explanation, str)
    assert len(explanation) > 0

def test_ab_test_content_variants():
    # Test content variants
    variants = [
        {
            "title": "Variant A",
            "body": "This is variant A content."
        },
        {
            "title": "Variant B",
            "body": "This is variant B content."
        }
    ]
    
    # Test engagement data for variants
    engagement_data = [
        {"engagement_rate": 3.2, "likes": 32, "comments": 5, "shares": 3},
        {"engagement_rate": 2.8, "likes": 28, "comments": 4, "shares": 2}
    ]
    
    # Call the function
    result = engagement_optimization_service.ab_test_content_variants(variants, engagement_data)
    
    # Assertions
    assert "winner" in result
    assert "performance_comparison" in result
    assert "recommendations" in result
    
    winner = result["winner"]
    assert winner in [0, 1]  # Index of the winning variant
    
    performance_comparison = result["performance_comparison"]
    assert isinstance(performance_comparison, list)
    assert len(performance_comparison) == 2
    
    recommendations = result["recommendations"]
    assert isinstance(recommendations, list)
    assert len(recommendations) > 0

def test_get_content_tone_suggestions():
    # Test content
    content = {
        "body": "This is a test post about AI and machine learning trends.",
        "content_type": "text"
    }
    
    # Test user profile with content tone
    user_profile = {
        "content_tone": "Professional and Informative"
    }
    
    # Test engagement data
    engagement_data = {
        "engagement_rate": 2.1
    }
    
    # Call the function
    result = engagement_optimization_service.get_content_tone_suggestions(content, user_profile, engagement_data)
    
    # Assertions
    assert "tone_analysis" in result
    assert "suggestions" in result
    assert "predicted_improvement" in result
    
    tone_analysis = result["tone_analysis"]
    assert isinstance(tone_analysis, dict)
    assert "current_tone" in tone_analysis
    assert "detected_tone" in tone_analysis
    
    suggestions = result["suggestions"]
    assert isinstance(suggestions, list)
    
    predicted_improvement = result["predicted_improvement"]
    assert isinstance(predicted_improvement, (int, float))
    assert predicted_improvement >= 0