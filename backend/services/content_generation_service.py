import openai
import json
from typing import Dict, List, Any
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_content_prompt(user_profile: Dict[str, Any], topic: str, content_type: str) -> str:
    """
    Generate a prompt for the AI content generator
    """
    professional_identity = user_profile.get("professional_identity", {})
    content_tone = user_profile.get("content_tone", "Professional and Informative")
    
    prompt = f"""
    You are an expert content creator helping {professional_identity.get('name', 'a professional')} 
    with the headline "{professional_identity.get('headline', '')}" create engaging LinkedIn content.
    
    Content Topic: {topic}
    Content Type: {content_type}
    Content Tone: {content_tone}
    
    Please create content that:
    1. Is relevant to their professional background
    2. Provides value to their target audience
    3. Maintains a {content_tone} tone
    4. Is appropriate for LinkedIn platform
    5. Is between 100-300 words for text posts
    
    For carousel posts, create 5-7 slides with titles and content for each slide.
    For articles, create a more detailed piece with sections and subheadings.
    """
    
    return prompt

def generate_text_content(user_profile: Dict[str, Any], topic: str) -> Dict[str, Any]:
    """
    Generate text content for a LinkedIn post
    """
    prompt = generate_content_prompt(user_profile, topic, "text post")
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.7,
            stop=["\n\n"]
        )
        
        content = response.choices[0].text.strip()
        
        return {
            "title": f"Insights on {topic}",
            "body": content,
            "content_type": "text",
            "status": "generated"
        }
    except Exception as e:
        return {
            "title": f"Insights on {topic}",
            "body": f"Couldn't generate content at this time. Here are some thoughts on {topic}...",
            "content_type": "text",
            "status": "error",
            "error": str(e)
        }

def generate_carousel_content(user_profile: Dict[str, Any], topic: str) -> Dict[str, Any]:
    """
    Generate carousel content for LinkedIn
    """
    prompt = generate_content_prompt(user_profile, topic, "carousel")
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=800,
            temperature=0.7
        )
        
        content = response.choices[0].text.strip()
        
        # In a real implementation, you would parse this into slides
        # For now, we'll return the raw content
        return {
            "title": f"Key Points on {topic}",
            "body": content,
            "content_type": "carousel",
            "status": "generated"
        }
    except Exception as e:
        return {
            "title": f"Key Points on {topic}",
            "body": f"Couldn't generate carousel content at this time. Here are some key points on {topic}...",
            "content_type": "carousel",
            "status": "error",
            "error": str(e)
        }

def generate_article_content(user_profile: Dict[str, Any], topic: str) -> Dict[str, Any]:
    """
    Generate article content for LinkedIn
    """
    prompt = generate_content_prompt(user_profile, topic, "article")
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            temperature=0.7
        )
        
        content = response.choices[0].text.strip()
        
        return {
            "title": f"Deep Dive: {topic}",
            "body": content,
            "content_type": "article",
            "status": "generated"
        }
    except Exception as e:
        return {
            "title": f"Deep Dive: {topic}",
            "body": f"Couldn't generate article content at this time. Here's an introduction to {topic}...",
            "content_type": "article",
            "status": "error",
            "error": str(e)
        }

def generate_content_with_hashtags(content: Dict[str, Any], hashtags: List[str]) -> Dict[str, Any]:
    """
    Add hashtags to generated content
    """
    if content.get("status") == "generated":
        hashtag_string = " ".join(hashtags[:5])  # Use first 5 hashtags
        content["body"] = f"{content['body']}\n\n{hashtag_string}"
        content["hashtags"] = hashtag_string
    
    return content

def generate_content_title(topic: str, content_type: str) -> str:
    """
    Generate a compelling title for the content
    """
    title_prompts = {
        "text": f"Quick insights on {topic}",
        "carousel": f"Key points about {topic}",
        "article": f"Deep dive into {topic}",
        "poll": f"What do you think about {topic}?"
    }
    
    return title_prompts.get(content_type, f"Thoughts on {topic}")