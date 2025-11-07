from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

from core.database import Base, engine
from api import models_router
import logging
import uvicorn
from contextlib import asynccontextmanager
import time

def init_database(max_retries: int = 10, delay_seconds: int = 3) -> None:
    """
    Ensure the database is reachable and initialize tables before serving traffic.
    """
    for attempt in range(1, max_retries + 1):
        try:
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            Base.metadata.create_all(bind=engine)
            logging.info("Database is ready.")
            return
        except OperationalError as exc:
            logging.warning(
                "Database not ready (attempt %s/%s): %s", attempt, max_retries, exc
            )
            time.sleep(delay_seconds)
    raise RuntimeError("Database did not become ready in time.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    logging.info("Starting up the Firewall Comparison API...")
    init_database()
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

# Routers
app.include_router(models_router.router)

# Health Check Endpoint
@app.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "OK"} 

@app.get("/", tags=["Health"])
async def root():
    return {"message": "Firewall Comparison API is running"}
