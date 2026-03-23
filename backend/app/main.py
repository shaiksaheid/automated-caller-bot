from fastapi import FastAPI
from app.database.db import engine
from app.database import models
from app.api.routes.calls import router as calls_router

# Import routers directly (safe & clear)
from app.api.routes.students import router as students_router
from app.api.routes.attendance import router as attendance_router

from app.api.routes.admin import router as admin_router


from app.services.scheduler_service import start_scheduler


from fastapi.middleware.cors import CORSMiddleware

# Create DB tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Automated Caller Bot API",
    version="1.0.0"
)

# Register routers
app.include_router(students_router)
app.include_router(attendance_router)
app.include_router(calls_router)
app.include_router(admin_router)
from app.api.routes import admin
from app.api.routes import calls

app.include_router(admin.router)
app.include_router(calls.router)

# Health check
@app.get("/")
def health_check():
    return {"status": "API is running"}




@app.on_event("startup")
def startup_event():
    start_scheduler()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)