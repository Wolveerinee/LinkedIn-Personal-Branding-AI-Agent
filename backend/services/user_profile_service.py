import json
from typing import Dict, List, Any
from ..models import user

def analyze_user_profile(user_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze user's LinkedIn profile to extract key information for content generation
    """
    analysis = {
        "professional_identity": {},
        "content_themes": [],
        "target_audience": [],
        "content_tone": ""
    }
    
    # Extract professional identity
    analysis["professional_identity"] = {
        "name": user_data.get("name", ""),
        "headline": user_data.get("headline", ""),
        "skills": user_data.get("skills", []),
        "experience": user_data.get("experience", [])
    }
    
    # Determine content themes based on skills and experience
    skills = user_data.get("skills", [])
    experience = user_data.get("experience", [])
    
    # Simple keyword-based theme extraction
    tech_keywords = ["python", "javascript", "ai", "machine learning", "data science"]
    business_keywords = ["marketing", "sales", "management", "strategy"]
    design_keywords = ["ui", "ux", "design", "graphic"]
    
    themes = []
    for skill in skills:
        skill_lower = skill.lower()
        if any(keyword in skill_lower for keyword in tech_keywords):
            themes.append("Technology")
        if any(keyword in skill_lower for keyword in business_keywords):
            themes.append("Business")
        if any(keyword in skill_lower for keyword in design_keywords):
            themes.append("Design")
    
    analysis["content_themes"] = list(set(themes))
    
    # Determine target audience based on experience
    audience = []
    for exp in experience:
        if "engineer" in exp.get("title", "").lower():
            audience.extend(["Developers", "Engineers", "Tech Enthusiasts"])
        if "manager" in exp.get("title", "").lower():
            audience.extend(["Managers", "Leaders", "Professionals"])
    
    analysis["target_audience"] = list(set(audience))
    
    # Determine content tone based on headline and about section
    about = user_data.get("about", "").lower()
    headline = user_data.get("headline", "").lower()
    
    if "passionate" in about or "enthusiast" in headline:
        analysis["content_tone"] = "Enthusiastic and Educational"
    elif "expert" in about or "senior" in headline:
        analysis["content_tone"] = "Authoritative and Insightful"
    else:
        analysis["content_tone"] = "Professional and Informative"
    
    return analysis

def extract_skills_and_interests(user_data: Dict[str, Any]) -> Dict[str, List[str]]:
    """
    Extract skills and interests from user profile
    """
    return {
        "skills": user_data.get("skills", []),
        "interests": user_data.get("interests", []) if user_data.get("interests") else []
    }

def get_content_preferences(user_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Determine content preferences based on user profile
    """
    preferences = {
        "content_types": [],
        "posting_frequency": "daily",
        "optimal_posting_times": []
    }
    
    # Determine preferred content types based on skills
    skills = user_data.get("skills", [])
    if any(skill.lower() in ["python", "javascript", "programming"] for skill in skills):
        preferences["content_types"].extend(["technical_tutorials", "code_snippets"])
    
    if any(skill.lower() in ["marketing", "sales"] for skill in skills):
        preferences["content_types"].extend(["industry_insights", "case_studies"])
    
    # Default posting frequency
    preferences["posting_frequency"] = "daily"
    
    # Default optimal posting times (these could be customized based on audience)
    preferences["optimal_posting_times"] = ["08:00", "12:00", "18:00"]
    
    return preferences