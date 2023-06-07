from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    nome: str
    preco: float
    quantidade: int
    image_url: str

class ProductRes(Product):
    a_venda: bool
    created_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True