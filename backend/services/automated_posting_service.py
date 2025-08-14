from typing import Dict, List, Any
from datetime import datetime
import schedule
import time
from . import linkedin_service, content_generation_service

class AutomatedPostingService:
    def __init__(self):
        self.scheduled_posts = []
        self.posting_queue = []
    
    def schedule_post(self, content: Dict[str, Any], scheduled_time: str) -> Dict[str, Any]:
        """
        Schedule a post for automatic publishing
        """
        post_job = {
            "content": content,
            "scheduled_time": scheduled_time,
            "status": "scheduled"
        }
        
        self.scheduled_posts.append(post_job)
        
        # In a real implementation, you would use a proper job scheduler
        # like Celery or APScheduler to handle the actual scheduling
        # For now, we'll just store the scheduled post
        
        return {
            "message": "Post scheduled successfully",
            "scheduled_time": scheduled_time,
            "status": "scheduled"
        }
    
    def publish_scheduled_posts(self) -> List[Dict[str, Any]]:
        """
        Publish posts that are scheduled for the current time
        """
        current_time = datetime.now()
        published_posts = []
        
        for post in self.scheduled_posts:
            scheduled_time = datetime.strptime(post["scheduled_time"], "%Y-%m-%d %H:%M")
            
            # Check if it's time to publish the post
            if current_time >= scheduled_time and post["status"] == "scheduled":
                # Publish the post
                result = linkedin_service.post_content(post["content"])
                
                # Update post status
                post["status"] = "published"
                post["published_time"] = current_time.strftime("%Y-%m-%d %H:%M")
                post["linkedin_post_id"] = result.get("post_id")
                
                published_posts.append({
                    "content_id": post["content"].get("id"),
                    "linkedin_post_id": result.get("post_id"),
                    "status": "published"
                })
        
        return published_posts
    
    def add_to_posting_queue(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add content to the posting queue for review before publishing
        """
        queue_item = {
            "content": content,
            "added_time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "status": "in_queue"
        }
        
        self.posting_queue.append(queue_item)
        
        return {
            "message": "Content added to posting queue",
            "queue_position": len(self.posting_queue),
            "status": "in_queue"
        }
    
    def approve_queue_item(self, queue_index: int) -> Dict[str, Any]:
        """
        Approve a content item in the posting queue for publishing
        """
        if queue_index < 0 or queue_index >= len(self.posting_queue):
            return {"error": "Invalid queue index"}
        
        queue_item = self.posting_queue[queue_index]
        content = queue_item["content"]
        
        # Publish the content
        result = linkedin_service.post_content(content)
        
        # Update queue item status
        queue_item["status"] = "published"
        queue_item["published_time"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        queue_item["linkedin_post_id"] = result.get("post_id")
        
        return {
            "message": "Content published successfully",
            "linkedin_post_id": result.get("post_id"),
            "status": "published"
        }
    
    def get_scheduled_posts(self) -> List[Dict[str, Any]]:
        """
        Get all scheduled posts
        """
        return self.scheduled_posts
    
    def get_posting_queue(self) -> List[Dict[str, Any]]:
        """
        Get all items in the posting queue
        """
        return self.posting_queue
    
    def cancel_scheduled_post(self, scheduled_time: str) -> Dict[str, Any]:
        """
        Cancel a scheduled post
        """
        for i, post in enumerate(self.scheduled_posts):
            if post["scheduled_time"] == scheduled_time and post["status"] == "scheduled":
                self.scheduled_posts.pop(i)
                return {"message": "Scheduled post cancelled", "status": "cancelled"}
        
        return {"error": "Scheduled post not found or already published"}
    
    def reschedule_post(self, old_scheduled_time: str, new_scheduled_time: str) -> Dict[str, Any]:
        """
        Reschedule a post for a different time
        """
        for post in self.scheduled_posts:
            if post["scheduled_time"] == old_scheduled_time and post["status"] == "scheduled":
                post["scheduled_time"] = new_scheduled_time
                return {
                    "message": "Post rescheduled successfully",
                    "old_scheduled_time": old_scheduled_time,
                    "new_scheduled_time": new_scheduled_time
                }
        
        return {"error": "Scheduled post not found or already published"}

# Global instance of the automated posting service
posting_service = AutomatedPostingService()

def start_posting_scheduler():
    """
    Start the automated posting scheduler
    In a real implementation, this would run as a background process
    """
    # This is a placeholder implementation
    # In a real application, you would use a proper scheduler
    print("Posting scheduler started")
    
    # Example of how you might check for scheduled posts periodically
    # schedule.every().minute.do(posting_service.publish_scheduled_posts)
    # 
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)