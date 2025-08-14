from typing import Dict, List, Any
from datetime import datetime
import statistics

def calculate_engagement_rate(likes: int, comments: int, shares: int, impressions: int) -> float:
    """
    Calculate engagement rate for a post
    Formula: (likes + comments + shares) / impressions * 100
    """
    if impressions == 0:
        return 0.0
    
    engagement = likes + comments + shares
    engagement_rate = (engagement / impressions) * 100
    return round(engagement_rate, 2)

def get_content_performance_metrics(content_data: Dict[str, Any], 
                                   analytics_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get performance metrics for content
    """
    likes = analytics_data.get("likes", 0)
    comments = analytics_data.get("comments", 0)
    shares = analytics_data.get("shares", 0)
    impressions = analytics_data.get("impressions", 0)
    reach = analytics_data.get("reach", 0)
    
    engagement_rate = calculate_engagement_rate(likes, comments, shares, impressions)
    
    return {
        "likes": likes,
        "comments": comments,
        "shares": shares,
        "impressions": impressions,
        "reach": reach,
        "engagement_rate": engagement_rate,
        "content_id": content_data.get("id"),
        "content_type": content_data.get("content_type")
    }

def compare_performance_to_benchmarks(performance_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compare content performance to industry benchmarks
    """
    # Industry benchmarks (these would be more detailed in a real implementation)
    benchmarks = {
        "text": {"engagement_rate": 2.5},
        "carousel": {"engagement_rate": 3.0},
        "article": {"engagement_rate": 4.0},
        "poll": {"engagement_rate": 3.5}
    }
    
    content_type = performance_data.get("content_type", "text")
    content_engagement_rate = performance_data.get("engagement_rate", 0)
    benchmark_engagement_rate = benchmarks.get(content_type, {}).get("engagement_rate", 2.0)
    
    performance_comparison = content_engagement_rate - benchmark_engagement_rate
    
    return {
        "content_type": content_type,
        "content_engagement_rate": content_engagement_rate,
        "benchmark_engagement_rate": benchmark_engagement_rate,
        "performance_vs_benchmark": performance_comparison,
        "performance_description": "Above benchmark" if performance_comparison > 0 else "Below benchmark"
    }

def generate_performance_insights(content_analytics: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generate insights from content performance data
    """
    if not content_analytics:
        return {"insights": [], "summary": "No data available"}
    
    # Calculate average metrics
    engagement_rates = [data.get("engagement_rate", 0) for data in content_analytics]
    avg_engagement_rate = statistics.mean(engagement_rates) if engagement_rates else 0
    
    likes_list = [data.get("likes", 0) for data in content_analytics]
    avg_likes = statistics.mean(likes_list) if likes_list else 0
    
    comments_list = [data.get("comments", 0) for data in content_analytics]
    avg_comments = statistics.mean(comments_list) if comments_list else 0
    
    shares_list = [data.get("shares", 0) for data in content_analytics]
    avg_shares = statistics.mean(shares_list) if shares_list else 0
    
    # Find best performing content
    best_content = max(content_analytics, key=lambda x: x.get("engagement_rate", 0))
    
    insights = []
    
    if avg_engagement_rate < 2.0:
        insights.append("Overall engagement rate is below industry average. Consider optimizing content strategy.")
    elif avg_engagement_rate > 5.0:
        insights.append("Overall engagement rate is above industry average. Keep up the good work!")
    else:
        insights.append("Engagement rate is within industry average range.")
    
    # Content type insights
    content_types = {}
    for data in content_analytics:
        content_type = data.get("content_type", "text")
        if content_type not in content_types:
            content_types[content_type] = []
        content_types[content_type].append(data.get("engagement_rate", 0))
    
    for content_type, rates in content_types.items():
        avg_type_rate = statistics.mean(rates) if rates else 0
        insights.append(f"{content_type.title()} posts have an average engagement rate of {avg_type_rate:.2f}%")
    
    return {
        "insights": insights,
        "summary": {
            "average_engagement_rate": round(avg_engagement_rate, 2),
            "average_likes": round(avg_likes, 2),
            "average_comments": round(avg_comments, 2),
            "average_shares": round(avg_shares, 2),
            "best_performing_content": {
                "id": best_content.get("content_id"),
                "engagement_rate": best_content.get("engagement_rate", 0),
                "content_type": best_content.get("content_type")
            }
        }
    }

def get_audience_insights(content_analytics: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Get insights about audience behavior
    """
    # This would be more detailed in a real implementation
    # For now, we'll provide placeholder insights
    
    return {
        "peak_engagement_times": ["08:00", "12:00", "18:00"],
        "most_engaged_content_types": ["carousel", "article"],
        "audience_growth": "15% increase in followers last month",
        "top_comments": [
            "Great insights!",
            "Thanks for sharing",
            "Very helpful information"
        ]
    }