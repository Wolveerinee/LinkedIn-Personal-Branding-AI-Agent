from typing import Dict, List, Any
from datetime import datetime, timedelta
import random

def create_content_calendar(user_profile: Dict[str, Any], trending_topics: List[Dict[str, Any]], 
                           content_preferences: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Create a content calendar based on user profile and trending topics
    """
    calendar = []
    start_date = datetime.now()
    
    # Get content types based on user preferences
    content_types = content_preferences.get("content_types", ["text"])
    
    # Create content for the next 7 days
    for i in range(7):
        date = start_date + timedelta(days=i)
        
        # Select a topic for the day
        topic = random.choice(trending_topics) if trending_topics else {"topic": "Professional Development"}
        
        # Select a content type for the day
        content_type = random.choice(content_types) if content_types else "text"
        
        calendar.append({
            "date": date.strftime("%Y-%m-%d"),
            "topic": topic["topic"],
            "content_type": content_type,
            "scheduled": True,
            "posted": False
        })
    
    return calendar

def suggest_content_themes(user_profile: Dict[str, Any], industry_trends: List[Dict[str, Any]]) -> List[str]:
    """
    Suggest content themes based on user profile and industry trends
    """
    themes = []
    
    # Get user's content themes
    user_themes = user_profile.get("content_themes", [])
    
    # Add industry trend topics
    trend_topics = [trend["topic"] for trend in industry_trends[:3]]  # Top 3 trends
    
    # Combine user themes with trend topics
    themes.extend(user_themes)
    themes.extend(trend_topics)
    
    # Remove duplicates while preserving order
    unique_themes = []
    for theme in themes:
        if theme not in unique_themes:
            unique_themes.append(theme)
    
    return unique_themes[:10]  # Limit to 10 themes

def optimize_posting_schedule(user_profile: Dict[str, Any], 
                            content_calendar: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Optimize posting schedule based on user's audience and optimal posting times
    """
    optimized_calendar = []
    
    # Get optimal posting times from user preferences
    optimal_times = user_profile.get("optimal_posting_times", ["08:00", "12:00", "18:00"])
    
    for item in content_calendar:
        # Assign a random optimal time to each post
        posting_time = random.choice(optimal_times)
        
        # Combine date with posting time
        scheduled_datetime = f"{item['date']} {posting_time}"
        
        optimized_item = item.copy()
        optimized_item["scheduled_time"] = scheduled_datetime
        optimized_calendar.append(optimized_item)
    
    return optimized_calendar

def get_content_engagement_prediction(content_type: str, hashtags: List[str]) -> Dict[str, Any]:
    """
    Predict engagement for content based on type and hashtags
    """
    # Base engagement scores by content type
    engagement_scores = {
        "text": 70,
        "carousel": 85,
        "article": 90,
        "poll": 75
    }
    
    # Calculate base score
    base_score = engagement_scores.get(content_type, 70)
    
    # Adjust based on number of hashtags (optimal is 3-5)
    hashtag_count = len(hashtags)
    if hashtag_count >= 3 and hashtag_count <= 5:
        hashtag_bonus = 10
    elif hashtag_count > 5:
        hashtag_bonus = 5  # Too many hashtags can reduce engagement
    else:
        hashtag_bonus = 0
    
    predicted_engagement = base_score + hashtag_bonus
    
    return {
        "predicted_engagement_score": min(predicted_engagement, 100),  # Cap at 100
        "factors": {
            "content_type": content_type,
            "base_score": base_score,
            "hashtag_bonus": hashtag_bonus
        }
    }

def recommend_content_improvements(content: Dict[str, Any], analytics: Dict[str, Any]) -> List[str]:
    """
    Recommend improvements based on content performance
    """
    recommendations = []
    
    # Get engagement rate from analytics
    engagement_rate = analytics.get("engagement_rate", 0)
    
    if engagement_rate < 2:
        recommendations.append("Consider using more engaging headlines")
        recommendations.append("Try asking questions to encourage comments")
    
    if engagement_rate >= 2 and engagement_rate < 5:
        recommendations.append("Add relevant hashtags to increase discoverability")
        recommendations.append("Include a clear call-to-action")
    
    if engagement_rate >= 5:
        recommendations.append("Keep creating content like this - it's performing well!")
    
    # Check content length
    content_length = len(content.get("body", ""))
    if content_length < 100:
        recommendations.append("Consider adding more depth to your content")
    elif content_length > 3000:
        recommendations.append("Content might be too long - consider breaking it into multiple posts")
    
    # Check hashtags
    hashtags = content.get("hashtags", "").split()
    if len(hashtags) < 3:
        recommendations.append("Add more relevant hashtags to increase reach")
    elif len(hashtags) > 10:
        recommendations.append("Too many hashtags can reduce engagement - consider using fewer")
    
    return recommendations