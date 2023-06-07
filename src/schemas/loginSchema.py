from pydantic import BaseModel, EmailStr
from typing import Optional

class Login(BaseModel):
    email: EmailStr
    senha: str

class LoginRes(BaseModel):
    token: str 
    user: str
    token_type: str

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    id: Optional[str] = None