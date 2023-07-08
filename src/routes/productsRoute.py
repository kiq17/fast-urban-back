from fastapi import APIRouter, Depends, HTTPException
from ..schemas.productSchema import Product, ProductRes, ProductImage
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from typing import List

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", status_code=201, response_model=ProductRes)
def createProduct(product: Product, db: Session = Depends(get_db)):
    p = models.Product(**product.dict())
    db.add(p)
    db.commit()
    db.refresh(p)

    return p

@router.post("/{productId}/image", status_code=201)
def addImageToProduct(productId: int, productImg: ProductImage, db: Session = Depends(get_db)):
    findProducut = db.query(models.Product).filter(models.Product.id == productId)

    if findProducut is None:
        raise HTTPException(status_code=400, detail="Produto não encontrado")
    
    p = models.ProductsImages(image_url=productImg.image_url, product_id=productId)
    db.add(p)
    db.commit()

    return {"message": "imagem adiciona ao produto"}

@router.get("/{productId}/images", response_model=List[ProductImage])
def images(productId: int, db: Session = Depends(get_db)):
    productImgs = db.query(models.ProductsImages).filter(models.ProductsImages.product_id == productId).all()

    if productImgs is None:
        raise HTTPException(status_code=400, detail="Produto não encontrado")
    
    return productImgs