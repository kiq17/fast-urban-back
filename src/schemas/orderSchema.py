from pydantic import BaseModel
from .productSchema import Product
from .userSchema import User

class Order(BaseModel):
    user_id: User

    class Config:
        orm_mode = True