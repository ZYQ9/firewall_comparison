from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.dialects.postgresql import UUID as PGUUID
import uuid

from core.database import Base

class FirewallModel(Base):
    __tablename__ = "firewall_models"

    id: Mapped[uuid.UUID] = mapped_column(
        PGUUID(as_uuid=True), #Updating to use PostgreSQL UUID type
        primary_key=True,
        index=True,
        default=uuid.uuid4,
    )

    model_number: Mapped[str] = mapped_column(index=True)
    vendor: Mapped[str] = mapped_column(index=True)
    firewall_throughput: Mapped[float] = mapped_column()
    ips_throughput: Mapped[float] = mapped_column()
    threat_prevention_throughput_gbps: Mapped[float | None] = mapped_column(nullable=True)
    concurrent_sessions: Mapped[int | None] = mapped_column(nullable=True)
    ssl_inspection_throughput_gbps: Mapped[float | None] = mapped_column(nullable=True)
    interfaces: Mapped[str | None] = mapped_column(nullable=True)
