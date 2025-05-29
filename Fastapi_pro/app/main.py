import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.db import create_db_and_tables
from app.routers import user_router, team_router, auth_router

app = FastAPI()
# app = FastAPI(dependencies=[Depends(get_query_token)]) 声明全局依赖响

app.include_router(user_router.router)
app.include_router(team_router.router)
app.include_router(auth_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/createDatabase", tags=["database"])
async def create_database():
    """Create the database and tables."""
    create_db_and_tables()
    return {"message": "Database and tables created successfully!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
