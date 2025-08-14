import React, { useState, useEffect } from 'react';
import { Bar, Line, Pie } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement,
  ArcElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import axios from 'axios';
import './Analytics.css';

// Register the required components
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement,
  ArcElement,
  Title,
  Tooltip,
  Legend
);

function Analytics() {
  const [analyticsData, setAnalyticsData] = useState({
    engagementData: {},
    contentPerformance: {},
    audienceInsights: {}
  });

  useEffect(() => {
    // In a real application, you would fetch this data from your backend API
    // For now, we'll use mock data
    
    // Mock engagement data
    const engagementData = {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
      datasets: [
        {
          label: 'Engagement Rate (%)',
          data: [2.1, 2.5, 3.2, 2.8, 3.5, 4.2, 3.8, 4.0],
          backgroundColor: 'rgba(0, 115, 177, 0.6)',
          borderColor: 'rgba(0, 115, 177, 1)',
          borderWidth: 1,
        },
      ],
    };

    // Mock content performance data
    const contentPerformance = {
      labels: ['Text Posts', 'Carousels', 'Articles', 'Polls'],
      datasets: [
        {
          label: 'Average Engagement Rate',
          data: [2.5, 3.8, 4.2, 3.0],
          backgroundColor: [
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
          ],
          borderWidth: 1,
        },
      ],
    };

    // Mock audience insights data
    const audienceInsights = {
      labels: ['08:00', '12:00', '18:00', '20:00', '22:00'],
      datasets: [
        {
          label: 'Post Views',
          data: [1200, 1800, 2400, 1500, 800],
          fill: false,
          backgroundColor: 'rgb(0, 115, 177)',
          borderColor: 'rgba(0, 115, 177, 0.2)',
        },
      ],
    };

    setAnalyticsData({
      engagementData,
      contentPerformance,
      audienceInsights
    });
  }, []);

  const engagementOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Monthly Engagement Rate',
      },
    },
  };

  const contentPerformanceOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Content Type Performance',
      },
    },
  };

  const audienceInsightsOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Audience Activity by Time',
      },
    },
  };

  return (
    <div className="analytics">
      <h1>Analytics Dashboard</h1>
      
      <div className="analytics-grid">
        <div className="metric-card">
          <h3>Average Engagement Rate</h3>
          <div className="value">4.2%</div>
          <div className="trend positive">↑ 12% from last month</div>
        </div>
        
        <div className="metric-card">
          <h3>Total Posts</h3>
          <div className="value">24</div>
          <div className="trend">+3 from last month</div>
        </div>
        
        <div className="metric-card">
          <h3>Reach</h3>
          <div className="value">12,400</div>
          <div className="trend positive">↑ 8% from last month</div>
        </div>
        
        <div className="metric-card">
          <h3>Impressions</h3>
          <div className="value">45,600</div>
          <div className="trend positive">↑ 15% from last month</div>
        </div>
      </div>
      
      <div className="chart-container">
        <h2>Engagement Trends</h2>
        {analyticsData.engagementData.datasets && (
          <Bar data={analyticsData.engagementData} options={engagementOptions} />
        )}
      </div>
      
      <div className="chart-container">
        <h2>Content Performance</h2>
        {analyticsData.contentPerformance.datasets && (
          <Pie data={analyticsData.contentPerformance} options={contentPerformanceOptions} />
        )}
      </div>
      
      <div className="chart-container">
        <h2>Audience Insights</h2>
        {analyticsData.audienceInsights.datasets && (
          <Line data={analyticsData.audienceInsights} options={audienceInsightsOptions} />
        )}
      </div>
      
      <div className="insights-section">
        <h2>Performance Insights</h2>
        <div className="insights-list">
          <div className="insight-item">
            <h3>Top Performing Content</h3>
            <p>Articles have the highest engagement rate at 4.2%</p>
          </div>
          <div className="insight-item">
            <h3>Best Posting Times</h3>
            <p>18:00 has the highest audience activity</p>
          </div>
          <div className="insight-item">
            <h3>Recommendations</h3>
            <p>Increase article posts to boost engagement</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Analytics;