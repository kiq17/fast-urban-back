from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    nome: str
    email: EmailStr
    senha: str


# extender classe basta passar User no parametro
class UserRes(BaseModel):
    id: int
    nome: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True