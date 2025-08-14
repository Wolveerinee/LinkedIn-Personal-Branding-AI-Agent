import pytest
from datetime import datetime, timedelta
from ..services import content_strategy_service

def test_create_content_calendar():
    # Test user profile
    user_profile = {
        "optimal_posting_times": ["08:00", "12:00", "18:00"]
    }
    
    # Test trending topics
    trending_topics = [
        {"topic": "AI Trends", "relevance_score": 90},
        {"topic": "Machine Learning", "relevance_score": 85},
        {"topic": "Data Science", "relevance_score": 80}
    ]
    
    # Test content preferences
    content_preferences = {
        "content_types": ["text", "carousel", "article"]
    }
    
    # Call the function
    result = content_strategy_service.create_content_calendar(user_profile, trending_topics, content_preferences)
    
    # Assertions
    assert isinstance(result, list)
    assert len(result) == 7  # We create content for the next 7 days
    
    # Check each day's content
    for day_content in result:
        assert "date" in day_content
        assert "topic" in day_content
        assert "content_type" in day_content
        assert "scheduled" in day_content
        assert "posted" in day_content
        
        # Check that the topic is from our trending topics
        topic_names = [topic["topic"] for topic in trending_topics]
        assert day_content["topic"] in topic_names
        
        # Check that the content type is from our preferences
        assert day_content["content_type"] in content_preferences["content_types"]
        
        # Check that scheduled is True and posted is False
        assert day_content["scheduled"] == True
        assert day_content["posted"] == False

def test_suggest_content_themes():
    # Test user profile with content themes
    user_profile = {
        "content_themes": ["Technology", "AI", "Machine Learning"]
    }
    
    # Test industry trends
    industry_trends = [
        {"topic": "Latest AI Developments"},
        {"topic": "Machine Learning Breakthroughs"},
        {"topic": "Data Science Innovations"}
    ]
    
    # Call the function
    result = content_strategy_service.suggest_content_themes(user_profile, industry_trends)
    
    # Assertions
    assert isinstance(result, list)
    assert len(result) <= 10  # We limit to 10 themes
    
    # Check that user themes are included
    for theme in user_profile["content_themes"]:
        assert theme in result
    
    # Check that trend topics are included (top 3)
    trend_topics = [trend["topic"] for trend in industry_trends[:3]]
    for topic in trend_topics:
        assert topic in result

def test_optimize_posting_schedule():
    # Test user profile with optimal posting times
    user_profile = {
        "optimal_posting_times": ["08:00", "12:00", "18:00"]
    }
    
    # Test content calendar
    content_calendar = [
        {"date": "2025-08-15", "topic": "AI Trends", "content_type": "text"},
        {"date": "2025-08-16", "topic": "Machine Learning", "content_type": "carousel"},
        {"date": "2025-08-17", "topic": "Data Science", "content_type": "article"}
    ]
    
    # Call the function
    result = content_strategy_service.optimize_posting_schedule(user_profile, content_calendar)
    
    # Assertions
    assert isinstance(result, list)
    assert len(result) == len(content_calendar)
    
    # Check each optimized item
    for item in result:
        assert "scheduled_time" in item
        assert item["date"] in [cal_item["date"] for cal_item in content_calendar]
        assert item["topic"] in [cal_item["topic"] for cal_item in content_calendar]
        assert item["content_type"] in [cal_item["content_type"] for cal_item in content_calendar]
        
        # Check that scheduled_time includes both date and time
        scheduled_time = item["scheduled_time"]
        assert " " in scheduled_time
        assert any(time in scheduled_time for time in user_profile["optimal_posting_times"])

def test_get_content_engagement_prediction():
    # Test content type and hashtags
    content_type = "carousel"
    hashtags = ["#AI", "#MachineLearning", "#DataScience", "#Technology"]
    
    # Call the function
    result = content_strategy_service.get_content_engagement_prediction(content_type, hashtags)
    
    # Assertions
    assert "predicted_engagement_score" in result
    assert "factors" in result
    
    # Check predicted engagement score
    engagement_score = result["predicted_engagement_score"]
    assert isinstance(engagement_score, (int, float))
    assert engagement_score >= 0
    assert engagement_score <= 100
    
    # Check factors
    factors = result["factors"]
    assert "content_type" in factors
    assert "base_score" in factors
    assert "hashtag_bonus" in factors
    
    assert factors["content_type"] == content_type
    assert factors["base_score"] > 0
    assert factors["hashtag_bonus"] >= 0

def test_recommend_content_improvements():
    # Test content and analytics
    content = {
        "body": "This is a test content post with some information.",
        "hashtags": "#AI #MachineLearning #DataScience #Technology #Innovation #Future"
    }
    
    analytics = {
        "engagement_rate": 1.5
    }
    
    # Call the function
    result = content_strategy_service.recommend_content_improvements(content, analytics)
    
    # Assertions
    assert isinstance(result, list)
    assert len(result) > 0
    
    # Check recommendations based on low engagement rate
    assert any("engaging headlines" in rec for rec in result) or \
           any("ask questions" in rec for rec in result) or \
           any("add more depth" in rec for rec in result) or \
           any("too many hashtags" in rec for rec in result)
    
    # Test with higher engagement rate
    analytics_high = {
        "engagement_rate": 6.0
    }
    
    result_high = content_strategy_service.recommend_content_improvements(content, analytics_high)
    assert any("Keep creating content like this" in rec for rec in result_high)
    
    # Test with too many hashtags
    result_many_hashtags = content_strategy_service.recommend_content_improvements(content, analytics)
    assert any("too many hashtags" in rec for rec in result_many_hashtags)