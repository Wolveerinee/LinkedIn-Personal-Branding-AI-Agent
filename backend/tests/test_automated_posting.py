import pytest
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock
from ..services import automated_posting_service

def test_schedule_post():
    # Create an instance of the service
    service = automated_posting_service.AutomatedPostingService()
    
    # Test content
    content = {
        "id": 1,
        "title": "Test Post",
        "body": "This is a test post for scheduling."
    }
    
    # Test scheduled time
    scheduled_time = "2025-08-15 08:00"
    
    # Call the function
    result = service.schedule_post(content, scheduled_time)
    
    # Assertions
    assert "message" in result
    assert "scheduled_time" in result
    assert "status" in result
    
    assert result["message"] == "Post scheduled successfully"
    assert result["scheduled_time"] == scheduled_time
    assert result["status"] == "scheduled"
    
    # Check that the post was added to scheduled_posts
    assert len(service.scheduled_posts) == 1
    scheduled_post = service.scheduled_posts[0]
    assert scheduled_post["content"] == content
    assert scheduled_post["scheduled_time"] == scheduled_time
    assert scheduled_post["status"] == "scheduled"

@patch('backend.services.automated_posting_service.linkedin_service.post_content')
def test_publish_scheduled_posts(mock_post_content):
    # Mock the LinkedIn service function
    mock_post_content.return_value = {"post_id": "test_post_id", "status": "posted"}
    
    # Create an instance of the service
    service = automated_posting_service.AutomatedPostingService()
    
    # Add a scheduled post with a past time
    past_time = (datetime.now() - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M")
    content = {
        "id": 1,
        "title": "Past Post",
        "body": "This post should be published."
    }
    
    service.schedule_post(content, past_time)
    
    # Call the function
    result = service.publish_scheduled_posts()
    
    # Assertions
    assert isinstance(result, list)
    assert len(result) == 1
    
    published_post = result[0]
    assert "content_id" in published_post
    assert "linkedin_post_id" in published_post
    assert "status" in published_post
    
    assert published_post["content_id"] == 1
    assert published_post["linkedin_post_id"] == "test_post_id"
    assert published_post["status"] == "published"
    
    # Check that the scheduled post status was updated
    assert len(service.scheduled_posts) == 1
    scheduled_post = service.scheduled_posts[0]
    assert scheduled_post["status"] == "published"
    assert "published_time" in scheduled_post
    assert "linkedin_post_id" in scheduled_post

def test_add_to_posting_queue():
    # Create an instance of the service
    service = automated_posting_service.AutomatedPostingService()
    
    # Test content
    content = {
        "id": 1,
        "title": "Queued Post",
        "body": "This post is in the queue."
    }
    
    # Call the function
    result = service.add_to_posting_queue(content)
    
    # Assertions
    assert "message" in result
    assert "queue_position" in result
    assert "status" in result
    
    assert result["message"] == "Content added to posting queue"
    assert result["queue_position"] == 1
    assert result["status"] == "in_queue"
    
    # Check that the content was added to the queue
    assert len(service.posting_queue) == 1
    queue_item = service.posting_queue[0]
    assert queue_item["content"] == content
    assert queue_item["status"] == "in_queue"
    assert "added_time" in queue_item

@patch('backend.services.automated_posting_service.linkedin_service.post_content')
def test_approve_queue_item(mock_post_content):
    # Mock the LinkedIn service function
    mock_post_content.return_value = {"post_id": "test_post_id", "status": "posted"}
    
    # Create an instance of the service
    service = automated_posting_service.AutomatedPostingService()
    
    # Add content to the queue
    content = {
        "id": 1,
        "title": "Approved Post",
        "body": "This post has been approved."
    }
    
    service.add_to_posting_queue(content)
    
    # Call the function
    result = service.approve_queue_item(0)
    
    # Assertions
    assert "message" in result
    assert "linkedin_post_id" in result
    assert "status" in result
    
    assert result["message"] == "Content published successfully"
    assert result["linkedin_post_id"] == "test_post_id"
    assert result["status"] == "published"
    
    # Check that the queue item status was updated
    assert len(service.posting_queue) == 1
    queue_item = service.posting_queue[0]
    assert queue_item["status"] == "published"
    assert "published_time" in queue_item
    assert "linkedin_post_id" in queue_item

def test_get_scheduled_posts():
    # Create an instance of the service
    service = automated_posting_service.AutomatedPostingService()
    
    # Add some scheduled posts
    content1 = {"id": 1, "title": "Post 1"}
    content2 = {"id": 2, "title": "Post 2"}
    
    service.schedule_post(content1, "2025-08-15 08:00")
    service.schedule_post(content2, "2025-08-16 12:00")
    
    # Call the function
    result = service.get_scheduled_posts()
    
    # Assertions
    assert isinstance(result, list)
    assert len(result) == 2
    
    # Check that we get the scheduled posts
    post_titles = [post["content"]["title"] for post in result]
    assert "Post 1" in post_titles
    assert "Post 2" in post_titles

def test_get_posting_queue():
    # Create an instance of the service
    service = automated_posting_service.AutomatedPostingService()
    
    # Add some content to the queue
    content1 = {"id": 1, "title": "Queue Item 1"}
    content2 = {"id": 2, "title": "Queue Item 2"}
    
    service.add_to_posting_queue(content1)
    service.add_to_posting_queue(content2)
    
    # Call the function
    result = service.get_posting_queue()
    
    # Assertions
    assert isinstance(result, list)
    assert len(result) == 2
    
    # Check that we get the queue items
    queue_titles = [item["content"]["title"] for item in result]
    assert "Queue Item 1" in queue_titles
    assert "Queue Item 2" in queue_titles

def test_cancel_scheduled_post():
    # Create an instance of the service
    service = automated_posting_service.AutomatedPostingService()
    
    # Add a scheduled post
    content = {"id": 1, "title": "To Cancel"}
    scheduled_time = "2025-08-15 08:00"
    
    service.schedule_post(content, scheduled_time)
    
    # Call the function
    result = service.cancel_scheduled_post(scheduled_time)
    
    # Assertions
    assert "message" in result
    assert "status" in result
    
    assert result["message"] == "Scheduled post cancelled"
    assert result["status"] == "cancelled"
    
    # Check that the scheduled post was removed
    assert len(service.scheduled_posts) == 0

def test_reschedule_post():
    # Create an instance of the service
    service = automated_posting_service.AutomatedPostingService()
    
    # Add a scheduled post
    content = {"id": 1, "title": "To Reschedule"}
    old_scheduled_time = "2025-08-15 08:00"
    new_scheduled_time = "2025-08-16 12:00"
    
    service.schedule_post(content, old_scheduled_time)
    
    # Call the function
    result = service.reschedule_post(old_scheduled_time, new_scheduled_time)
    
    # Assertions
    assert "message" in result
    assert "old_scheduled_time" in result
    assert "new_scheduled_time" in result
    
    assert result["message"] == "Post rescheduled successfully"
    assert result["old_scheduled_time"] == old_scheduled_time
    assert result["new_scheduled_time"] == new_scheduled_time
    
    # Check that the scheduled post was updated
    assert len(service.scheduled_posts) == 1
    scheduled_post = service.scheduled_posts[0]
    assert scheduled_post["scheduled_time"] == new_scheduled_time