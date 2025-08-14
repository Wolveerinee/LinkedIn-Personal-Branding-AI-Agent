# LinkedIn Personal Branding AI Agent API Documentation

## Overview

This document provides detailed information about the RESTful API endpoints for the LinkedIn Personal Branding AI Agent. The API allows users to manage their LinkedIn profile, generate content, schedule posts, and analyze performance.

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

All API endpoints require authentication via LinkedIn OAuth 2.0. Users must first authenticate with LinkedIn to access the API.

## API Endpoints

### User Management

#### Get User Profile

```
GET /users/{user_id}
```

Retrieves a user's profile information.

**Parameters:**

- `user_id` (integer, required): The unique identifier of the user

**Response:**

```json
{
  "id": 1,
  "linkedin_profile_url": "https://www.linkedin.com/in/johndoe",
  "name": "John Doe",
  "headline": "Software Engineer",
  "about": "Passionate about AI and machine learning",
  "skills": "[\"Python\", \"JavaScript\", \"Machine Learning\"]",
  "experience": "[{\"title\": \"Software Engineer\", \"company\": \"XYZ Corp\"}]",
  "education": "[{\"degree\": \"MSc Computer Science\", \"institution\": \"ABC University\"}]",
  "interests": "[\"Technology\", \"Innovation\"]",
  "created_at": "2025-08-01T12:00:00Z",
  "updated_at": "2025-08-10T15:30:00Z"
}
```

#### Update User Profile

```
PUT /users/{user_id}
```

Updates a user's profile information.

**Parameters:**

- `user_id` (integer, required): The unique identifier of the user

**Request Body:**

```json
{
  "linkedin_profile_url": "https://www.linkedin.com/in/johndoe",
  "name": "John Doe",
  "headline": "Senior Software Engineer",
  "about": "Passionate about AI and machine learning with 5+ years experience",
  "skills": "[\"Python\", \"JavaScript\", \"Machine Learning\", \"Data Science\"]",
  "experience": "[{\"title\": \"Senior Software Engineer\", \"company\": \"XYZ Corp\"}]",
  "education": "[{\"degree\": \"MSc Computer Science\", \"institution\": \"ABC University\"}]",
  "interests": "[\"Technology\", \"Innovation\", \"Professional Development\"]"
}
```

### Content Management

#### Create Content

```
POST /content/
```

Creates a new content item.

**Request Body:**

```json
{
  "user_id": 1,
  "title": "Latest Industry Trends",
  "body": "Exploring the latest trends in technology and their impact on business...",
  "content_type": "text",
  "hashtags": "[\"#Technology\", \"#Innovation\"]",
  "scheduled_time": "2025-08-15T08:00:00Z"
}
```

#### Get Content

```
GET /content/{content_id}
```

Retrieves a specific content item.

**Parameters:**

- `content_id` (integer, required): The unique identifier of the content

#### Get User's Content

```
GET /content/user/{user_id}
```

Retrieves all content items for a specific user.

**Parameters:**

- `user_id` (integer, required): The unique identifier of the user

### Analytics

#### Get Content Analytics

```
GET /analytics/content/{content_id}
```

Retrieves analytics data for a specific content item.

**Parameters:**

- `content_id` (integer, required): The unique identifier of the content

**Response:**

```json
{
  "id": 1,
  "content_id": 1,
  "likes": 42,
  "comments": 5,
  "shares": 3,
  "impressions": 1200,
  "engagement_rate": 4.2,
  "reach": 800,
  "created_at": "2025-08-10T12:00:00Z",
  "updated_at": "2025-08-12T15:30:00Z"
}
```

### LinkedIn Integration

#### Authenticate with LinkedIn

```
POST /linkedin/authenticate
```

Authenticates with LinkedIn API using OAuth 2.0.

**Request Body:**

```json
{
  "profile_url": "https://www.linkedin.com/in/johndoe"
}
```

#### Get LinkedIn Profile

```
GET /linkedin/profile/{user_id}
```

Retrieves a user's LinkedIn profile information.

**Parameters:**

- `user_id` (integer, required): The unique identifier of the user

#### Post to LinkedIn

```
POST /linkedin/post/{content_id}
```

Posts content to LinkedIn.

**Parameters:**

- `content_id` (integer, required): The unique identifier of the content

## Error Responses

The API uses standard HTTP status codes to indicate the success or failure of requests:

- `200 OK` - The request was successful
- `201 Created` - The resource was successfully created
- `400 Bad Request` - The request was invalid
- `401 Unauthorized` - Authentication failed
- `404 Not Found` - The requested resource was not found
- `500 Internal Server Error` - An error occurred on the server

## Rate Limiting

The API implements rate limiting to ensure fair usage. Users are limited to 100 requests per hour.

## Versioning

This documentation covers version 1.0.0 of the API.
