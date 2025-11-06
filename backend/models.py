from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from core.database import Base

class FirewallModel(Base):
    __tablename__ = "firewall_models"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    model_number: Mapped[str] = mapped_column(index=True)
    vendor: Mapped[int] = mapped_column(index=True)
    firewall_throughput: Mapped[float] = mapped_column()
    ips_throughput: Mapped[float] = mapped_column()
    threat_prevention_throughput_gbps: Mapped[float | None] = mapped_column(nullable=True)
    concurrent_sessions: Mapped[int | None] = mapped_column(nullable=True)
    ssl_inspection_throughput_gbps: Mapped[float | None] = mapped_column(nullable=True)
    interfaces: Mapped[str | None] = mapped_column(nullable=True)