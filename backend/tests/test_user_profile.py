import pytest
from ..services import user_profile_service

def test_analyze_user_profile():
    # Test user data
    user_data = {
        "name": "John Doe",
        "headline": "Software Engineer at XYZ Corp",
        "about": "Passionate about AI and machine learning with 5 years of experience.",
        "skills": ["Python", "JavaScript", "Machine Learning", "Data Science"],
        "experience": [
            {
                "title": "Software Engineer",
                "company": "XYZ Corp",
                "duration": "2020-Present"
            },
            {
                "title": "Junior Developer",
                "company": "ABC Inc",
                "duration": "2018-2020"
            }
        ],
        "education": [
            {
                "degree": "MSc Computer Science",
                "institution": "ABC University",
                "year": "2018"
            }
        ]
    }
    
    # Call the function
    result = user_profile_service.analyze_user_profile(user_data)
    
    # Assertions
    assert "professional_identity" in result
    assert "content_themes" in result
    assert "target_audience" in result
    assert "content_tone" in result
    
    # Check professional identity
    prof_identity = result["professional_identity"]
    assert prof_identity["name"] == "John Doe"
    assert "Software Engineer" in prof_identity["headline"]
    assert len(prof_identity["skills"]) > 0
    assert len(prof_identity["experience"]) > 0
    
    # Check content themes
    themes = result["content_themes"]
    assert "Technology" in themes  # Should be detected from skills like Python, JavaScript
    assert len(themes) > 0
    
    # Check target audience
    audience = result["target_audience"]
    assert "Developers" in audience  # Should be detected from engineer title
    assert "Engineers" in audience
    assert len(audience) > 0
    
    # Check content tone
    tone = result["content_tone"]
    assert tone in ["Enthusiastic and Educational", "Authoritative and Insightful", "Professional and Informative"]

def test_extract_skills_and_interests():
    # Test user data with skills and interests
    user_data = {
        "skills": ["Python", "JavaScript", "Machine Learning"],
        "interests": ["AI", "Data Science", "Open Source"]
    }
    
    # Call the function
    result = user_profile_service.extract_skills_and_interests(user_data)
    
    # Assertions
    assert "skills" in result
    assert "interests" in result
    assert "Python" in result["skills"]
    assert "AI" in result["interests"]
    assert len(result["skills"]) == 3
    assert len(result["interests"]) == 3

def test_get_content_preferences():
    # Test user data with skills
    user_data = {
        "skills": ["Python", "JavaScript", "Marketing", "Sales"]
    }
    
    # Call the function
    result = user_profile_service.get_content_preferences(user_data)
    
    # Assertions
    assert "content_types" in result
    assert "posting_frequency" in result
    assert "optimal_posting_times" in result
    
    # Check content types
    content_types = result["content_types"]
    assert "technical_tutorials" in content_types  # From Python, JavaScript
    assert "code_snippets" in content_types       # From programming skills
    assert "industry_insights" in content_types    # From Marketing, Sales
    
    # Check posting frequency
    assert result["posting_frequency"] == "daily"
    
    # Check optimal posting times
    assert len(result["optimal_posting_times"]) == 3
    assert "08:00" in result["optimal_posting_times"]
    assert "12:00" in result["optimal_posting_times"]
    assert "18:00" in result["optimal_posting_times"]