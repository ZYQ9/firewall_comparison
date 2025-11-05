from typing import List,Optional
from pydantic import BaseModel, Field
from datetime import date

# Firewall Model Schema
class FirewallModelBase(BaseModel):
    model_number: str = Field(..., description="The model number of the firewall")
    vendor: str = Field(..., description="The vendor of the firewall")
    firewall_throughput: float = Field(..., description="The firewall throughput in Gbps")
    ips_throughput: float = Field(..., description="The IPS throughput in Gbps")
    threat_prevention_throughput_gbps: Optional[float] = Field(None, example=10.0, description="Full security profile throughput (Threat + Malware + IPS)")
    concurrent_sessions: Optional[int] = Field(None, example=2000000, description="Max concurrent sessions")
    ssl_inspection_throughput_gbps: Optional[float] = Field(None, example=0.0, description="SSL inspection throughput (Gbps)")
    interfaces: str = Field(None, example="10x GE RJ45, 2x 10G SFP+")

class FirewallModelCreate(FirewallModelBase):
    vendor_id: int = Field(..., example=1)

class FirewallModelUpdate(FirewallModelBase):
    pass 

class FirewallModelOut(FirewallModelBase):
    id: int
    vendor: str = Field(..., description="The name of the vendor")

    class Config:
        orm_mode = True

# Comparison Schema
class ComparisonRequest(BaseModel):
    fwmodel_ids: List[int] = Field(..., description="List of firewall model IDs to compare")

class ComparisonResult(BaseModel):
    model_number: str
    vendor: str
    firewall_throughput: Optional[float]
    ips_throughput: Optional[float]
    threat_prevention_throughput_gbps: Optional[float]
    ssl_inspection_throughput_gbps: Optional[float]
    concurrent_sessions: Optional[int]
    interfaces: Optional[str]

    class Config:
        orm_mode = True