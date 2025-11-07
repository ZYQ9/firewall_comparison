from typing import List,Optional
from pydantic import BaseModel, Field
from uuid import UUID


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
    pass

class FirewallModelUpdate(FirewallModelBase):
    pass 

class FirewallModelOut(FirewallModelBase):
    id: UUID = Field(..., description="The unique identifier of the firewall model")

    class Config:
        from_attributes = True

# Comparison Schema
class ComparisonRequest(BaseModel):
    fwmodel_ids: List[UUID] = Field(..., description="List of firewall model IDs to compare")

class ComparisonResult(BaseModel):
    id: UUID
    model_number: str
    vendor: str
    firewall_throughput: Optional[float]
    ips_throughput: Optional[float]
    threat_prevention_throughput_gbps: Optional[float]
    ssl_inspection_throughput_gbps: Optional[float]
    concurrent_sessions: Optional[int]
    interfaces: Optional[str]

    class Config:
        from_attributes = True
