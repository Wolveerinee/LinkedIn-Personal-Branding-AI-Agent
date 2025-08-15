# LinkedIn Personal Branding AI Agent

An autonomous AI agent that researches, creates, and posts LinkedIn content for personal branding.

## Features

- **User Profile Analysis**: Analyzes LinkedIn profile, work history, skills, and interests
- **Industry Research**: Stays updated with industry trends, news, and relevant topics
- **Content Strategy**: Develops a content calendar and posting strategy
- **Content Generation**: Creates various types of LinkedIn posts (articles, updates, carousels)
- **Engagement Optimization**: Optimizes posts for maximum engagement
- **Performance Analytics**: Tracks and analyzes post performance
- **Automated Posting**: Schedules and publishes content automatically

## Tech Stack

- **Backend**: FastAPI (Python)
- **AI/ML**: OpenAI GPT-4, LangChain
- **Database**: PostgreSQL
- **Caching**: Redis
- **Frontend**: React/Next.js
- **Deployment**: Docker containers
- **Cloud Platforms**: AWS/GCP/Azure

## Project Structure

```
├── backend/              # FastAPI backend application
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   ├── routers/          # API routes
│   ├── services/         # Business logic
│   ├── database.py       # Database configuration
│   ├── main.py           # Main application
│   └── app.py           # Application entry point
├── frontend/             # React frontend application
│   ├── src/              # Source code
│   │   ├── components/    # React components
│   │   └── ...
│   └── README.md        # Frontend documentation
├── docs/                 # Documentation
│   ├── api.md            # API documentation
│   ├── technical_report.md # Technical report
│   ├── user_guide.md     # User guide
│   ├── demo_script.md    # Demo video script
│   └── deployment_guide.md # Deployment guide
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile            # Docker configuration
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables example
└── README.md             # This file
```

## Setup and Installation

### Prerequisites

- Python 3.9+
- Node.js 14+
- Docker and Docker Compose
- PostgreSQL
- Redis

### Environment Variables

Copy `.env.example` to `.env` and update the values:

```bash
cp .env.example .env
```

### Backend Setup

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the backend server:
   ```bash
   python backend/app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

### Docker Setup (Recommended)

1. Build and start all services:

   ```bash
   docker-compose up -d
   ```

2. The application will be available at:
   - Backend API: http://localhost:8000
   - Frontend: http://localhost:3000

## API Documentation

Detailed API documentation is available in [docs/api.md](docs/api.md).

## Technical Report

A comprehensive technical report is available in [docs/technical_report.md](docs/technical_report.md).

## User Guide

Instructions for using the application are available in [docs/user_guide.md](docs/user_guide.md).

## Deployment Guide

Deployment instructions are available in [docs/deployment_guide.md](docs/deployment_guide.md).

## Demo Video Script

A script for creating a demo video is available in [docs/demo_script.md](docs/demo_script.md).

## Testing

To run all tests:

```bash
python run_all_tests.py
```

Or run individual test files with pytest:

```bash
pytest backend/tests/test_api.py -v
```

## Troubleshooting

### Installation Issues

If you encounter issues installing the Python dependencies, particularly with packages like `psycopg2-binary` or `numpy`, this may be due to missing build tools on your system:

1. **For Windows users**:

   - Install Microsoft C++ Build Tools from https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - Or install Visual Studio with C++ development tools
   - Alternatively, use pre-compiled wheels by upgrading pip: `pip install --upgrade pip`

2. **For macOS users**:

   - Install Xcode command line tools: `xcode-select --install`
   - Install Homebrew if not already installed
   - Consider using conda instead of pip for scientific packages

3. **For Linux users**:
   - Install build essentials: `sudo apt-get install build-essential`
   - Install Python development headers: `sudo apt-get install python3-dev`

### Docker Issues

If you encounter issues with Docker:

1. Ensure Docker Desktop is running
2. Check that you have sufficient resources allocated to Docker
3. Try running `docker-compose down` and then `docker-compose up` again

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a pull request



## Contact

For technical questions, contact: tech-support@influence-os.com

