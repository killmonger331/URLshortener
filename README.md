# URL Shortener (Vercel + FastAPI on AWS Elastic Beanstalk)

A full-stack URL shortener web application built with a Vercel-hosted frontend, a FastAPI backend deployed on AWS Elastic Beanstalk, and Redis for persistence.

## Live Demo
Frontend: https://ur-lshortener-2tyie8x33-richards-projects-c0a9c9b4.vercel.app/

Backend API: https://api.richard-morales.com/health

Note: The backend is an API service and does not serve a web UI at the root path. 

## Overview
This project allows uers to submit long URLs and receive shortened links that redirect to the original destination. The backend is containerized using Docker and deployed to AWS with HTTPS enabled via a custom domain. 

## Architecture
- Frontend: Static HTML/CSS/JS deployed on Vercel
- Backend: FastAPI deployed on AWS Elastic Beanstalk (Docker)
- Storage:
  - Default: in-memory (resets on restart)
  - Production: Redis (persistent storage)
  
 ## Tech Stack
 Frontend:
 - HTML, CSS, JavaScript
 - Hosted on Vercel
Backend:
 - Python
 - FastAPI
 - Uvicorn
Infrastructure:
 - Docker
 - AWS Elastic Beanstalk
 - AWS Application Load Balancer
 - AWS ACM (HTTPS / TLS)
 - Route 53 (Custom Domain)
Storage
 - Redis

## Features
- URL shortening with unique short codes
- Persistent storage using Redis
- HTTPS-secured custom domain
- CORS-protected API access
- Dockerized backend for portability
- Production deployment on AWS

## Production Deployment
- Frontend: Vercel
- Backend: FastAPI running on AWS Elastic Beanstalk (Docker)
- Storage: Redis
- HTTPS: AWS ACM + Application Load Balancer
- DNS: Route 53

## Local Development
The backend can be ran locally using Docker Compose for development and testing.

### Backend + Redis (Docker-compose)
```bash
cd ops/docker
docker compose up --build
```

## What I Learned
- How to containerize a FastAPI applciation with Docker
- How environment variables differ between local and cloud environments
- How to configure HTTPS using AWS ACM and Elastic Beanstalk
- How DNS, load balancers, and TLS certificates work together
- How to debug CORS and cross-origin issues in production
- How to deploy and maintain a live backend independent of a local machine

## Future Improvements 
- Link expiration (TTL)
- Click analytics per short URL
- Rate limiting
- Authentication
- Database persistence (PostgreSQL)


