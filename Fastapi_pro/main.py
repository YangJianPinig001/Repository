import uvicorn
from fastapi import FastAPI
from Fastapi_pro.db import create_db_and_tables
from Fastapi_pro.routers import users, auth, team


app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(team.router)


@app.get("/createDatabase", tags=["database"])
async def create_database():
    """Create the database and tables."""
    create_db_and_tables()
    return {"message": "Database and tables created successfully!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)