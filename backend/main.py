from fastapi import FastAPI
from routers import router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# הוסף CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # בפיתוח - מאפשר הכל
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI(title="Todo API")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)