cd frontend
git pull
cd ..
docker build Pixelback -t pixelback-backend:latest
docker build frontend -t pixelback-front:latest
docker-compose down
docker-compose up -d
