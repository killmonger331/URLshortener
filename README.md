# URL Shortener (Vercel + FastAPI on AWS Elastic Beanstalk)

## Architecture
- Frontend: Static HTML/CSS/JS deployed on Vercel
- Backend: FastAPI deployed on AWS Elastic Beanstalk (Docker)
- Storage:
  - Default: in-memory (resets on restart)
  - Optional: Redis (recommended for persistence)

---

## Local dev

### Backend (recommended: docker-compose)
```bash
cd ops/docker
docker compose up --build
