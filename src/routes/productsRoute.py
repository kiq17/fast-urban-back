from fastapi import APIRouter, Depends
from ..schemas.productSchema import Product, ProductRes
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", status_code=201, response_model=ProductRes)
def createProduct(product: Product, db: Session = Depends(get_db)):
    p = models.Product(**product.dict())
    db.add(p)
    db.commit()
    db.refresh(p)

    return p