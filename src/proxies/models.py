from typing import Optional

from sqlmodel import SQLModel, Field


class Proxy(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, unique=True)
    ip: str = Field(unique=True, nullable=False)
    port: int = Field(nullable=False)
    country: str = Field(default="N/A")
    is_available: bool = Field(default=False)

