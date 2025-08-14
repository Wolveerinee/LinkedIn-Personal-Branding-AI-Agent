import pytest
from unittest.mock import patch, MagicMock
from ..services import content_generation_service

@patch('backend.services.content_generation_service.openai.Completion.create')
def test_generate_text_content(mock_openai_create):
    # Mock the OpenAI API response
    mock_openai_create.return_value = MagicMock(
        choices=[MagicMock(text="This is a test LinkedIn post content.")]
    )
    
    # Test user profile data
    user_profile = {
        "professional_identity": {
            "name": "Test User",
            "headline": "Software Engineer"
        },
        "content_tone": "Professional and Informative"
    }
    
    # Test topic
    topic = "Latest trends in AI"
    
    # Call the function
    result = content_generation_service.generate_text_content(user_profile, topic)
    
    # Assertions
    assert result["status"] == "generated"
    assert "body" in result
    assert "title" in result
    assert result["content_type"] == "text"
    assert "AI" in result["title"]  # Check that the topic is in the title

@patch('backend.services.content_generation_service.openai.Completion.create')
def test_generate_carousel_content(mock_openai_create):
    # Mock the OpenAI API response
    mock_openai_create.return_value = MagicMock(
        choices=[MagicMock(text="Slide 1: Introduction\nSlide 2: Key Points\nSlide 3: Conclusion")]
    )
    
    # Test user profile data
    user_profile = {
        "professional_identity": {
            "name": "Test User",
            "headline": "Data Scientist"
        },
        "content_tone": "Educational and Insightful"
    }
    
    # Test topic
    topic = "Machine Learning Best Practices"
    
    # Call the function
    result = content_generation_service.generate_carousel_content(user_profile, topic)
    
    # Assertions
    assert result["status"] == "generated"
    assert "body" in result
    assert "title" in result
    assert result["content_type"] == "carousel"
    assert "Machine Learning" in result["title"]

@patch('backend.services.content_generation_service.openai.Completion.create')
def test_generate_article_content(mock_openai_create):
    # Mock the OpenAI API response
    mock_openai_create.return_value = MagicMock(
        choices=[MagicMock(text="Introduction\n\nMain Content\n\nConclusion")]
    )
    
    # Test user profile data
    user_profile = {
        "professional_identity": {
            "name": "Test User",
            "headline": "Technical Writer"
        },
        "content_tone": "Authoritative and Insightful"
    }
    
    # Test topic
    topic = "Blockchain Technology"
    
    # Call the function
    result = content_generation_service.generate_article_content(user_profile, topic)
    
    # Assertions
    assert result["status"] == "generated"
    assert "body" in result
    assert "title" in result
    assert result["content_type"] == "article"
    assert "Blockchain" in result["title"]

def test_generate_content_with_hashtags():
    # Test content without hashtags
    content = {
        "title": "Test Content",
        "body": "This is a test content post.",
        "content_type": "text",
        "status": "generated"
    }
    
    # Test hashtags
    hashtags = ["#AI", "#Technology", "#Innovation"]
    
    # Call the function
    result = content_generation_service.generate_content_with_hashtags(content, hashtags)
    
    # Assertions
    assert "body" in result
    assert "hashtags" in result
    assert "#AI" in result["hashtags"]
    assert "#Technology" in result["hashtags"]
    assert "#Innovation" in result["hashtags"]

def test_generate_content_title():
    # Test different content types
    topic = "Artificial Intelligence"
    
    # Test text content type
    title_text = content_generation_service.generate_content_title(topic, "text")
    assert "Artificial Intelligence" in title_text
    assert "Quick insights" in title_text
    
    # Test carousel content type
    title_carousel = content_generation_service.generate_content_title(topic, "carousel")
    assert "Artificial Intelligence" in title_carousel
    assert "Key points" in title_carousel
    
    # Test article content type
    title_article = content_generation_service.generate_content_title(topic, "article")
    assert "Artificial Intelligence" in title_article
    assert "Deep dive" in title_article
    
    # Test poll content type
    title_poll = content_generation_service.generate_content_title(topic, "poll")
    assert "Artificial Intelligence" in title_poll
    assert "What do you think" in title_poll