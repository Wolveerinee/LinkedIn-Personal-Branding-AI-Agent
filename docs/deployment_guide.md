# LinkedIn Personal Branding AI Agent - Deployment Guide

## Overview

This guide provides instructions for deploying the LinkedIn Personal Branding AI Agent application to a production environment. The application consists of a backend API built with FastAPI and a frontend built with React.

## Prerequisites

Before deploying, ensure you have:

1. A server or cloud instance (AWS, GCP, Azure, etc.)
2. Docker and Docker Compose installed
3. A domain name (optional but recommended)
4. SSL certificate (optional but recommended)
5. LinkedIn API credentials
6. OpenAI API key

## Architecture

The application uses the following architecture in production:

```
Internet → Load Balancer/Reverse Proxy → Application Containers
                    ↓
              Database (PostgreSQL)
                    ↓
               Cache (Redis)
```

## Deployment Options

### Option 1: Docker Deployment (Recommended)

#### 1. Clone the Repository

```bash
git clone <repository-url>
cd linkedin-ai-agent
```

#### 2. Configure Environment Variables

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Update the following variables in `.env`:

- `DATABASE_URL`: PostgreSQL connection string
- `LINKEDIN_CLIENT_ID`: Your LinkedIn app client ID
- `LINKEDIN_CLIENT_SECRET`: Your LinkedIn app client secret
- `OPENAI_API_KEY`: Your OpenAI API key
- `SECRET_KEY`: A secure secret key for JWT tokens
- `HOST`: Set to 0.0.0.0 for production
- `PORT`: Set to 8000
- `DEBUG`: Set to False for production

#### 3. Configure Docker Compose

Update the `docker-compose.yml` file with production-specific settings:

- Set appropriate resource limits
- Configure volume mappings for persistent data
- Update network settings if needed

#### 4. Start the Application

```bash
docker-compose up -d
```

This will start:

- PostgreSQL database
- Redis cache
- Backend API
- (Frontend - if included in docker-compose)

#### 5. Initialize the Database

```bash
docker-compose exec backend python -m backend.init_db
```

### Option 2: Manual Deployment

#### Backend Deployment

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables:

   ```bash
   export DATABASE_URL=your_database_url
   export LINKEDIN_CLIENT_ID=your_client_id
   export LINKEDIN_CLIENT_SECRET=your_client_secret
   export OPENAI_API_KEY=your_openai_key
   export SECRET_KEY=your_secret_key
   ```

3. Start the application:
   ```bash
   uvicorn backend.main:app --host 0.0.0.0 --port 8000
   ```

#### Frontend Deployment

1. Install dependencies:

   ```bash
   cd frontend
   npm install
   ```

2. Build the production version:

   ```bash
   npm run build
   ```

3. Serve the build folder using a web server like Nginx or Apache.

### Option 3: Cloud Platform Deployment

#### AWS Deployment

1. Create an EC2 instance
2. Install Docker and Docker Compose
3. Follow the Docker deployment steps above
4. Configure Security Groups to allow HTTP/HTTPS traffic
5. (Optional) Use RDS for PostgreSQL instead of containerized database

#### Google Cloud Platform Deployment

1. Create a Compute Engine instance
2. Install Docker and Docker Compose
3. Follow the Docker deployment steps above
4. (Optional) Use Cloud SQL for PostgreSQL instead of containerized database

#### Azure Deployment

1. Create a Virtual Machine
2. Install Docker and Docker Compose
3. Follow the Docker deployment steps above
4. (Optional) Use Azure Database for PostgreSQL instead of containerized database

## Configuration

### Environment Variables

| Variable               | Description                  | Required |
| ---------------------- | ---------------------------- | -------- |
| DATABASE_URL           | PostgreSQL connection string | Yes      |
| LINKEDIN_CLIENT_ID     | LinkedIn app client ID       | Yes      |
| LINKEDIN_CLIENT_SECRET | LinkedIn app client secret   | Yes      |
| OPENAI_API_KEY         | OpenAI API key               | Yes      |
| SECRET_KEY             | Secret key for JWT tokens    | Yes      |
| REDIS_URL              | Redis connection string      | Yes      |
| HOST                   | Host IP address              | Yes      |
| PORT                   | Port number                  | Yes      |
| DEBUG                  | Debug mode (True/False)      | Yes      |

### LinkedIn API Configuration

1. Create a LinkedIn Developer app at https://developer.linkedin.com/
2. Configure the redirect URI to match your domain
3. Note the Client ID and Client Secret for environment configuration

### SSL Configuration

For production deployments, it's recommended to use SSL. You can:

1. Use a reverse proxy like Nginx with Let's Encrypt
2. Configure your cloud provider's load balancer with SSL termination
3. Use a service like Cloudflare for SSL

## Monitoring and Maintenance

### Health Checks

The application provides health check endpoints:

- Backend: `GET /health`
- Database: Check PostgreSQL connection
- Redis: Check Redis connection

### Logging

The application logs to stdout/stderr by default. Configure your deployment platform to capture and store these logs.

### Backup and Recovery

1. Regularly backup the PostgreSQL database
2. Backup the Docker volumes containing application data
3. Test recovery procedures periodically

### Updates

To update the application:

1. Pull the latest code:

   ```bash
   git pull origin main
   ```

2. Rebuild and restart containers:
   ```bash
   docker-compose down
   docker-compose up -d --build
   ```

## Troubleshooting

### Common Issues

1. **Database Connection Failed**

   - Check DATABASE_URL environment variable
   - Verify PostgreSQL container is running
   - Check network connectivity between containers

2. **LinkedIn Authentication Not Working**

   - Verify LinkedIn app credentials
   - Check redirect URI configuration
   - Ensure LinkedIn app is approved for production use

3. **Content Generation Failing**
   - Check OpenAI API key
   - Verify OpenAI API quota and limits
   - Check network connectivity to OpenAI API

### Logs

Check container logs for detailed error information:

```bash
docker-compose logs backend
docker-compose logs db
docker-compose logs redis
```

## Scaling

For high-traffic deployments:

1. Use a managed database service instead of containerized PostgreSQL
2. Use a managed Redis service instead of containerized Redis
3. Deploy multiple backend instances behind a load balancer
4. Use a CDN for frontend assets
5. Implement caching strategies for API responses

## Security Considerations

1. Always use HTTPS in production
2. Store secrets securely using your platform's secret management
3. Regularly update dependencies and base images
4. Implement proper firewall rules
5. Use non-root users in Docker containers
6. Regularly rotate API keys and secrets

## Performance Optimization

1. Use connection pooling for database connections
2. Implement Redis caching for frequently accessed data
3. Use CDN for frontend assets
4. Optimize database indexes
5. Implement API response caching where appropriate

## Conclusion

This deployment guide covers the essential steps for deploying the LinkedIn Personal Branding AI Agent to a production environment. Depending on your specific requirements and infrastructure, you may need to adjust these instructions.

For additional support, please contact our technical team or refer to the documentation.
