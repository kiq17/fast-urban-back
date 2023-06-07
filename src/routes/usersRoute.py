from fastapi import APIRouter, Depends, HTTPException
from ..schemas.userSchema import User, UserRes
from ..schemas.loginSchema import Login, LoginRes
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, utils, auth
from typing import List
from datetime import datetime

router = APIRouter(prefix="/users", tags=["users"])



@router.post("/login", response_model=LoginRes)
def userLogin(user: Login, db: Session = Depends(get_db)):
    findUser = db.query(models.User).filter(models.User.email == user.email).first()

    if findUser is None:
        raise HTTPException(status_code=400, detail="Email ou senha inválidos")

    checkPass = utils.verify(user.senha, findUser.senha)

    if not checkPass:
        raise HTTPException(status_code=400, detail="Email ou senha inválidos")

    acessToken = auth.createToken(data={"user_id": findUser.id})

    return {"user": findUser.nome, "token": acessToken, "token_type": "Bearer"}


# passar como parametro o schema para validar 
@router.get("/", response_model=List[UserRes])
def getUser(db: Session = Depends(get_db)):

    users = db.query(models.User).all()

    return users


@router.post("/", status_code=201, response_model= UserRes)
def createUser(user: User, db: Session = Depends(get_db)):

    findUser = db.query(models.User).filter(models.User.email == user.email).first()

    if findUser: 
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    # hash senha função do arquivo utils
    hashedPass = utils.hash(user.senha)
    user.senha =  hashedPass
    
    # em vez de passar nome=user.nome etc
    # ** é como desustrurar um objeto js user dict tranforma em objeto
    u = models.User(**user.dict())
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

@router.put("/{id}", response_model=UserRes)
def editUser(id: int, user: User, db: Session = Depends(get_db)):
    userQuery = db.query(models.User).filter(models.User.id == id)

    findUser = userQuery.first()

    if findUser is None:
        raise HTTPException(status_code=404, detail="Usário não existe")
    
    newUser = user.dict()
    newUser["update_at"] = datetime.now()

    userQuery.update(newUser, synchronize_session=False)

    db.commit()

    return userQuery.first()

@router.get("/{id}", response_model=UserRes)
def getUserId(id: int, db: Session = Depends(get_db)):
    findUser = db.query(models.User).filter(models.User.id == id).first()

    if findUser is None:
        raise HTTPException(status_code=404, detail="Usário não existe")
    
    return findUser