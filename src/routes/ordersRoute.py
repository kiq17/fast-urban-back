from fastapi import APIRouter, Depends
from .. import auth, database, models
from sqlalchemy.orm import Session
from ..schemas.productSchema import ProductRes
from typing import List

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/{productId}")
def createOrder(productId: int, userId: int = Depends(auth.getCurrentUser), db: Session = Depends(database.get_db)):

    o = models.Order(user_id=userId.id, product_id=productId)
    db.add(o)
    db.commit()

    return {"message": "Compra confirmada"}

@router.get("/", response_model=List[ProductRes])
def totalOrders(userId: int = Depends(auth.getCurrentUser), db: Session = Depends(database.get_db)):

    result = db.query(models.Product).join(models.Order,
        models.Order.product_id == models.Product.id
    ).filter(models.Order.user_id == userId.id).all()

    return result
