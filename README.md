# URL Shortener (Vercel + FastAPI on AWS Elastic Beanstalk)

A full-stack URL shortener web application built with a Vercel-hosted frontend, a FastAPI backend deployed on AWS Elastic Beanstalk, and Redis for persistence.

## Live Demo
Frontend: https://url-shortener-zeta.vercel.app
Backend API: https://api.richard-morales.com

## Overview
This project allows uers to submit long URLs and receive shortened links that redirect to the original destination. The backend is containerized using Docker and deployed to AWS with HTTPS enabled via a custom domain. 

## Architecture
- Frontend: Static HTML/CSS/JS deployed on Vercel
- Backend: FastAPI deployed on AWS Elastic Beanstalk (Docker)
- Storage:
  - Default: in-memory (resets on restart)
  - Production: Redis (persistent storage)
 
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


