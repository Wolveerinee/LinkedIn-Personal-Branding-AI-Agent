import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './ContentCalendar.css';

function ContentCalendar() {
  const [currentDate, setCurrentDate] = useState(new Date());
  const [contentItems, setContentItems] = useState([]);
  const [isAddingContent, setIsAddingContent] = useState(false);
  const [newContent, setNewContent] = useState({
    title: '',
    body: '',
    contentType: 'text',
    scheduledDate: ''
  });

  useEffect(() => {
    // In a real application, you would fetch this data from your backend API
    // For now, we'll use mock data
    const mockContent = [
      {
        id: 1,
        title: "Industry Trends",
        body: "Exploring the latest trends in technology and their impact on business...",
        contentType: "text",
        scheduledDate: "2025-08-15",
        status: "scheduled"
      },
      {
        id: 2,
        title: "Professional Tips",
        body: "5 essential tips for advancing your career in the tech industry...",
        contentType: "carousel",
        scheduledDate: "2025-08-18",
        status: "scheduled"
      },
      {
        id: 3,
        title: "Networking Strategies",
        body: "How to build meaningful professional relationships in the digital age...",
        contentType: "article",
        scheduledDate: "2025-08-20",
        status: "scheduled"
      }
    ];
    
    setContentItems(mockContent);
  }, []);

  const getDaysInMonth = (date) => {
    const year = date.getFullYear();
    const month = date.getMonth();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const firstDayOfMonth = new Date(year, month, 1).getDay();
    
    const days = [];
    
    // Add empty cells for days before the first day of the month
    for (let i = 0; i < firstDayOfMonth; i++) {
      days.push(null);
    }
    
    // Add days of the month
    for (let day = 1; day <= daysInMonth; day++) {
      days.push(day);
    }
    
    return days;
  };

  const getMonthName = (date) => {
    return date.toLocaleString('default', { month: 'long' });
  };

  const getYear = (date) => {
    return date.getFullYear();
  };

  const navigateMonth = (direction) => {
    const newDate = new Date(currentDate);
    newDate.setMonth(currentDate.getMonth() + direction);
    setCurrentDate(newDate);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewContent(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // In a real application, you would send this data to your backend API
    console.log('New content:', newContent);
    setIsAddingContent(false);
    setNewContent({
      title: '',
      body: '',
      contentType: 'text',
      scheduledDate: ''
    });
  };

  const days = getDaysInMonth(currentDate);
  const monthName = getMonthName(currentDate);
  const year = getYear(currentDate);

  return (
    <div className="content-calendar">
      <div className="calendar-header">
        <h1>Content Calendar</h1>
        <button className="btn" onClick={() => setIsAddingContent(true)}>
          Add Content
        </button>
      </div>
      
      <div className="calendar-navigation">
        <button className="btn btn-secondary" onClick={() => navigateMonth(-1)}>
          Previous
        </button>
        <h2>{monthName} {year}</h2>
        <button className="btn btn-secondary" onClick={() => navigateMonth(1)}>
          Next
        </button>
      </div>
      
      <div className="calendar-grid">
        {['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].map(day => (
          <div key={day} className="calendar-day-header">
            {day}
          </div>
        ))}
        
        {days.map((day, index) => (
          <div key={index} className="calendar-day">
            {day && (
              <>
                <div className="day-number">{day}</div>
                <div className="day-content">
                  {contentItems
                    .filter(item => {
                      const itemDate = new Date(item.scheduledDate);
                      return (
                        itemDate.getDate() === day &&
                        itemDate.getMonth() === currentDate.getMonth() &&
                        itemDate.getFullYear() === currentDate.getFullYear()
                      );
                    })
                    .map(item => (
                      <div key={item.id} className={`content-item ${item.contentType} ${item.status}`}>
                        <div className="content-title">{item.title}</div>
                        <div className="content-type">{item.contentType}</div>
                      </div>
                    ))
                  }
                </div>
              </>
            )}
          </div>
        ))}
      </div>
      
      {isAddingContent && (
        <div className="modal">
          <div className="modal-content">
            <h2>Add New Content</h2>
            <form onSubmit={handleSubmit}>
              <div className="form-group">
                <label htmlFor="title">Title</label>
                <input
                  type="text"
                  id="title"
                  name="title"
                  value={newContent.title}
                  onChange={handleInputChange}
                  required
                />
              </div>
              
              <div className="form-group">
                <label htmlFor="body">Content</label>
                <textarea
                  id="body"
                  name="body"
                  value={newContent.body}
                  onChange={handleInputChange}
                  rows="4"
                  required
                />
              </div>
              
              <div className="form-group">
                <label htmlFor="contentType">Content Type</label>
                <select
                  id="contentType"
                  name="contentType"
                  value={newContent.contentType}
                  onChange={handleInputChange}
                >
                  <option value="text">Text Post</option>
                  <option value="carousel">Carousel</option>
                  <option value="article">Article</option>
                  <option value="poll">Poll</option>
                </select>
              </div>
              
              <div className="form-group">
                <label htmlFor="scheduledDate">Scheduled Date</label>
                <input
                  type="date"
                  id="scheduledDate"
                  name="scheduledDate"
                  value={newContent.scheduledDate}
                  onChange={handleInputChange}
                  required
                />
              </div>
              
              <div className="form-actions">
                <button type="submit" className="btn">Add Content</button>
                <button 
                  type="button" 
                  className="btn btn-secondary" 
                  onClick={() => setIsAddingContent(false)}
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

export default ContentCalendar;