from sqlalchemy.orm import Session
from typing import List, Optional
from models import FirewallModel
from core.schemas import schemas

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