# Educational Dashboard - Stage 1 Implementation

## Overview

This project implements **Stage 1: Fundaciones y Autenticación** of the Educational Dashboard system. It provides a complete foundation with authentication, OAuth integration, and a modern frontend interface.

## Architecture

### Backend (FastAPI + Python)
- **Framework**: FastAPI 0.104.1
- **Language**: Python 3.10+
- **Authentication**: JWT + OAuth 2.0 with Google
- **Database**: Mock data with JSON files
- **Testing**: pytest with ≥70% coverage requirement

### Frontend (Next.js + React)
- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Authentication**: JWT + OAuth integration
- **Internationalization**: i18n with English as base language
- **Testing**: Vitest + React Testing Library

## Features Implemented

### ✅ Backend Features
- [x] FastAPI server with health check endpoint
- [x] JWT authentication with mock users
- [x] OAuth 2.0 integration with Google
- [x] Standardized API response envelope
- [x] Middleware for authentication and CORS
- [x] Mock data service with realistic test data
- [x] Comprehensive error handling
- [x] Structured logging

### ✅ Frontend Features
- [x] Next.js 15 with TypeScript configuration
- [x] Responsive design with Tailwind CSS
- [x] Login form with validation
- [x] OAuth Google integration
- [x] Protected routes with AuthGuard
- [x] Dashboard with statistics cards
- [x] Internationalization (i18n) system
- [x] Modern UI components
- [x] Error handling and loading states

### ✅ Integration Features
- [x] Frontend-backend communication
- [x] CORS configuration
- [x] JWT token management
- [x] OAuth callback handling
- [x] Session persistence

## Project Structure

```
/
├── backend/
│   ├── app/
│   │   ├── api/endpoints/     # API endpoints
│   │   ├── services/          # Business logic
│   │   ├── core/              # Configuration & security
│   │   ├── middleware/        # Request middleware
│   │   ├── models/            # Data models
│   │   ├── schemas/           # API schemas
│   │   ├── utils/             # Utilities
│   │   └── data/              # Mock data
│   ├── tests/                 # Test suites
│   └── requirements.txt       # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── app/               # Next.js app router
│   │   ├── components/        # React components
│   │   ├── hooks/             # Custom hooks
│   │   ├── lib/               # Utilities & services
│   │   ├── types/             # TypeScript types
│   │   ├── constants/         # App constants
│   │   └── i18n/              # Internationalization
│   └── package.json           # Node.js dependencies
└── contracts/                 # Project contracts
```

## Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- npm or yarn

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Install dependencies**:
   ```bash
   ./install.sh
   # OR manually:
   pip3 install -r requirements.txt
   ```

3. **Configure environment**:
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

4. **Start the server**:
   ```bash
   python -m uvicorn app.main:app --reload
   ```

   The backend will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   ./install.sh
   # OR manually:
   npm install
   ```

3. **Configure environment**:
   ```bash
   cp env.local.example .env.local
   # Edit .env.local with your configuration
   ```

4. **Start the development server**:
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:3000`

## API Endpoints

### Authentication
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/refresh` - Refresh token
- `POST /api/v1/auth/logout` - User logout
- `GET /api/v1/auth/me` - Get current user

### OAuth
- `GET /api/v1/oauth/google/url` - Get Google OAuth URL
- `GET /api/v1/oauth/google/callback` - Handle OAuth callback
- `POST /api/v1/oauth/google/revoke` - Revoke OAuth connection
- `GET /api/v1/oauth/status` - Get OAuth status

### Health
- `GET /api/v1/health/health` - Health check

## Mock Users

The system includes the following test users:

| Email | Password | Role |
|-------|----------|------|
| admin@educational.dashboard | admin123 | Administrator |
| coordinator@educational.dashboard | coord123 | Coordinator |
| teacher1@educational.dashboard | teacher123 | Teacher |
| teacher2@educational.dashboard | teacher123 | Teacher |
| student1@educational.dashboard | student123 | Student |
| student2@educational.dashboard | student123 | Student |

## Testing

### Backend Tests
```bash
cd backend
python -m pytest tests/ -v --cov=app --cov-report=html
```

### Frontend Tests
```bash
cd frontend
npm run test
```

## Development

### Code Quality
- **Backend**: Black, isort, flake8
- **Frontend**: ESLint, Prettier
- **Testing**: pytest (backend), Vitest (frontend)

### Environment Variables

#### Backend (.env)
```env
ENVIRONMENT=development
PORT=8000
JWT_SECRET=dev-secret-key-change-in-production
JWT_EXPIRES_IN=24h
CORS_ORIGIN=http://localhost:3000
LOG_LEVEL=debug
GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=http://localhost:3000/oauth/callback
```

#### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_APP_NAME=Educational Dashboard
NEXT_PUBLIC_VERSION=1.0.0
NEXT_PUBLIC_DEFAULT_LOCALE=en
NEXT_PUBLIC_GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
```

## Deployment

### Backend
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
npm run build
npm start
```

## Contributing

1. Follow the established code style
2. Write tests for new features
3. Ensure all tests pass
4. Update documentation as needed

## License

This project is part of the Educational Dashboard system implementation.

## Support

For issues and questions, please refer to the project documentation or contact the development team.
