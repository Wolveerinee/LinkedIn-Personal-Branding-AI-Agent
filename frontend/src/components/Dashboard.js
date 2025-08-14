import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Dashboard.css';

function Dashboard() {
  const [metrics, setMetrics] = useState({
    totalPosts: 0,
    engagementRate: 0,
    followers: 0,
    scheduledPosts: 0
  });

  const [recentPosts, setRecentPosts] = useState([]);

  useEffect(() => {
    // In a real application, you would fetch this data from your backend API
    // For now, we'll use mock data
    
    // Mock data for metrics
    setMetrics({
      totalPosts: 24,
      engagementRate: 4.2,
      followers: 1240,
      scheduledPosts: 7
    });

    // Mock data for recent posts
    setRecentPosts([
      {
        id: 1,
        title: "Latest Industry Trends",
        content: "Exploring the latest trends in technology and their impact on business...",
        likes: 42,
        comments: 5,
        shares: 3,
        date: "2025-08-12"
      },
      {
        id: 2,
        title: "Professional Development Tips",
        content: "5 essential tips for advancing your career in the tech industry...",
        likes: 38,
        comments: 8,
        shares: 2,
        date: "2025-08-10"
      },
      {
        id: 3,
        title: "Networking Strategies",
        content: "How to build meaningful professional relationships in the digital age...",
        likes: 56,
        comments: 12,
        shares: 7,
        date: "2025-08-08"
      }
    ]);
  }, []);

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      
      <div className="dashboard-grid">
        <div className="metric-card">
          <h3>Total Posts</h3>
          <div className="value">{metrics.totalPosts}</div>
        </div>
        
        <div className="metric-card">
          <h3>Engagement Rate</h3>
          <div className="value">{metrics.engagementRate}%</div>
        </div>
        
        <div className="metric-card">
          <h3>Followers</h3>
          <div className="value">{metrics.followers}</div>
        </div>
        
        <div className="metric-card">
          <h3>Scheduled Posts</h3>
          <div className="value">{metrics.scheduledPosts}</div>
        </div>
      </div>
      
      <div className="content-calendar">
        <h2>Recent Posts</h2>
        <div className="posts-list">
          {recentPosts.map(post => (
            <div key={post.id} className="post-card">
              <h3>{post.title}</h3>
              <p>{post.content}</p>
              <div className="post-stats">
                <span>❤️ {post.likes}</span>
                <span>💬 {post.comments}</span>
                <span>🔄 {post.shares}</span>
                <span>📅 {post.date}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Dashboard;