docker-compose up -d
cd backend
uv run alembic upgrade head
uv run main.py
cd ../frontend
npm i
npm run dev 