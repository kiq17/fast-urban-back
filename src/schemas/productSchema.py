from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Product(BaseModel):
    nome: str
    descricao: str
    preco: float
    quantidade: int
    coverImg: str
    categoria: str

class ProductRes(Product):
    a_venda: bool
    created_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True
    
class ProductImage(BaseModel):
    image_url: str

    class Config:
        orm_mode = True