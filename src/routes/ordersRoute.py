from fastapi import APIRouter, Depends
from .. import auth, database, models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/{productId}")
def createOrder(productId: int, userId: int = Depends(auth.getCurrentUser), db: Session = Depends(database.get_db)):

    o = models.Order(user_id=userId.id, product_id=productId)
    db.add(o)
    db.commit()

    return {"message": "Compra confirmada"}

