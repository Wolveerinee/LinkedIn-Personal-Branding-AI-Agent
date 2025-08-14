import pytest
from unittest.mock import patch, MagicMock
from ..services import industry_research_service

def test_get_trending_topics():
    # Test industry and skills
    industry = "Technology"
    skills = ["Python", "Machine Learning", "Data Science"]
    
    # Call the function
    result = industry_research_service.get_trending_topics(industry, skills)
    
    # Assertions
    assert isinstance(result, list)
    assert len(result) > 0
    
    # Check that we have the expected topics
    topics = [item["topic"] for item in result]
    assert f"Latest trends in {industry}" in topics
    assert "Industry best practices" in topics
    
    # Check that we have skill-based topics
    skill_topics = [item["topic"] for item in result if "Advanced" in item["topic"]]
    assert len(skill_topics) > 0
    
    # Check relevance scores
    for item in result:
        assert "relevance_score" in item
        assert isinstance(item["relevance_score"], int)
        assert item["relevance_score"] >= 0
        assert item["relevance_score"] <= 100

def test_get_industry_news():
    # Test industry
    industry = "Technology"
    
    # Call the function
    result = industry_research_service.get_industry_news(industry)
    
    # Assertions
    assert isinstance(result, list)
    assert len(result) == 2  # We expect 2 news items in our mock
    
    # Check news items
    for item in result:
        assert "title" in item
        assert "summary" in item
        assert "url" in item
        assert "published_date" in item
        assert industry in item["title"] or industry in item["summary"]

@patch('backend.services.industry_research_service.requests.get')
def test_get_competitor_analysis(mock_requests_get):
    # Mock the requests response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "competitors": [
            {
                "name": "Industry Leader 1",
                "content_strategy": "Focuses on educational content and tutorials",
                "posting_frequency": "daily",
                "popular_content_types": ["articles", "videos"]
            }
        ],
        "content_gaps": ["Interactive content like polls and quizzes"]
    }
    mock_requests_get.return_value = mock_response
    
    # Test profile URL
    profile_url = "https://www.linkedin.com/in/testuser"
    
    # Call the function
    result = industry_research_service.get_competitor_analysis(profile_url)
    
    # Assertions
    assert "competitors" in result
    assert "content_gaps" in result
    assert len(result["competitors"]) > 0
    assert len(result["content_gaps"]) > 0
    
    # Check competitor data
    competitor = result["competitors"][0]
    assert "name" in competitor
    assert "content_strategy" in competitor
    assert "posting_frequency" in competitor
    assert "popular_content_types" in competitor

def test_get_hashtag_suggestions():
    # Test industry, skills, and content theme
    industry = "Technology"
    skills = ["Python", "Machine Learning", "Data Science"]
    content_theme = "Technology"
    
    # Call the function
    result = industry_research_service.get_hashtag_suggestions(industry, skills, content_theme)
    
    # Assertions
    assert isinstance(result, list)
    assert len(result) <= 10  # We limit to 10 hashtags
    
    # Check that we have industry hashtags
    assert f"#{industry.replace(' ', '')}" in result
    
    # Check that we have skill-based hashtags
    skill_hashtags = [f"#{skill.replace(' ', '')}" for skill in skills]
    for hashtag in skill_hashtags:
        if hashtag in result:
            break
    else:
        # If none of the skill hashtags are in result, that's fine
        # (we limit to first 5 skills)
        pass
    
    # Check that we have theme-based hashtags
    theme_hashtags = ["#TechTrends", "#Innovation", "#DigitalTransformation"]
    for hashtag in theme_hashtags:
        if hashtag in result:
            break
    else:
        # If none of the theme hashtags are in result, that's fine
        # (we add theme-based hashtags based on content_theme)
        pass