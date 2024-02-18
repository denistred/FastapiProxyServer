from pydantic import BaseModel


class ProxyModel(BaseModel):
    id: int
    ip: str
    port: int
    country: str
    is_available: bool

    class Config:
        orm_mode = True

