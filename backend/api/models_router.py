from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.core import schemas
from crud import (
    create_firewall_model,
    get_firewall_model,
    get_firewall_models,
    get_firewall_models_by_vendor,
    search_firewall_models,
    delete_firewall_model,
)
from backend.core.database import get_db

router = APIRouter(prefix="/firewall_models", tags=["firewall_models"])