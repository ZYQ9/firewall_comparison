from sqlalchemy.orm import Session
from typing import List, Optional
from models import FirewallModel
from core import schemas

# POST Functions
def create_firewall_model(db: Session, fwmodel: schemas.FirewallModelCreate) -> FirewallModel:
    db_fwmodel = FirewallModel(
        model_number=fwmodel.model_number,
        vendor=fwmodel.vendor_id,
        firewall_throughput=fwmodel.firewall_throughput,
        ips_throughput=fwmodel.ips_throughput,
        threat_prevention_throughput_gbps=fwmodel.threat_prevention_throughput_gbps,
        concurrent_sessions=fwmodel.concurrent_sessions,
        ssl_inspection_throughput_gbps=fwmodel.ssl_inspection_throughput_gbps,
        interfaces=fwmodel.interfaces,
    )
    db.add(db_fwmodel)
    db.commit()
    db.refresh(db_fwmodel)
    return db_fwmodel

# GET Functions
def get_firewall_model(db: Session, fwmodel_id: str) -> Optional[FirewallModel]:
    """
    Retrieve a firewall model by its ID.
    """
    return db.query(FirewallModel).filter(FirewallModel.model_number == fwmodel_id).first()

def get_firewall_models(db: Session, skip: int=0, limit: int=100) -> List[FirewallModel]:
    """
    Retrieve a list of firewall models with pagination.
    """
    return db.query(FirewallModel).offset(skip).limit(limit).all()

def get_firewall_models_by_vendor(db: Session, vendor_id: str) -> List[FirewallModel]:
    """
    Retrieve all firewall models for a specific vendor
    """
    return (
        db.query(FirewallModel)
        .filter(FirewallModel.vendor == vendor_id)
        .all()
    )

def search_firewall_models(db: Session, search_term: str) -> List[FirewallModel]:
    """
    Search across vendor name, model number, and interfaces for keyword
    """
    return (
        db.query(FirewallModel)
        .filter(
            (FirewallModel.vendor.ilike(f"%{search_term}%"))
            | (FirewallModel.model_number.ilike(f"%{search_term}%"))
            | (FirewallModel.interfaces.ilike(f"%{search_term}%"))
        )
        .all()
    )

# DELETE Functions
def delete_firewall_model(db: Session, fwmodel_id: str) -> bool:
    """
    Delete a firewall model by its model number.
    """
    fwmodel = db.query(FirewallModel).filter(FirewallModel.model_number == fwmodel_id).first()
    if fwmodel:
        db.delete(fwmodel)
        db.commit()
        return True
    return False
