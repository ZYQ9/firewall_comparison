from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from core.database import Base, engine
from api import models_router
import logging
import uvicorn
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    logging.info("Starting up the Firewall Comparison API...")
    yield
    # Shutdown code
    logging.info("Shutting down the Firewall Comparison API...")

# Initialize the FastAPI app
app = FastAPI(
    title="Firewall Comparison API",
    description=(
        " Rest API for comparing firewall vendors and models."
        "Support for CRUD operations, model comparisons, and PDF exports"
    ),
    version="1.0.0",
    lifespan=lifespan,
)

# DB Initialization
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(models_router.router)

# Health Check Endpoint
@app.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "OK"} 

@app.get("/", tags=["Health"])
async def root():
    return {"message": "Firewall Comparison API is running"}

