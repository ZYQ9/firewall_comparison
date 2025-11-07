from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from core import schemas
from crud import (
    create_firewall_model,
    get_firewall_model,
    get_firewall_models,
    get_firewall_models_by_vendor,
    search_firewall_models,
    delete_firewall_model,
)
from core.database import get_db

router = APIRouter(prefix="/models", tags=["firewall_models"])

@router.post("/", response_model=schemas.FirewallModelOut, status_code=201)
async def create_model(fwmodel: schemas.FirewallModelCreate, db: Session = Depends(get_db)):
    return create_firewall_model(db, fwmodel)

@router.get("/{fwmodel_id}", response_model=schemas.FirewallModelOut)
async def read_model(fwmodel_id: UUID, db: Session = Depends(get_db)):
    db_fwmodel = get_firewall_model(db, fwmodel_id)
    if db_fwmodel is None:
        raise HTTPException(status_code=404, detail="Firewall model not found")
    return db_fwmodel

@router.get("/", response_model=List[schemas.FirewallModelOut])
async def read_models(db: Session = Depends(get_db)):
    return get_firewall_models(db)
