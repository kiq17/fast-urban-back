from fastapi import APIRouter, Body, Depends, HTTPException
from ..schemas.productSchema import Product, ProductRes, ProductImage
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from typing import List
from datetime import datetime

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/list/{page}/{perPage}", response_model=List[ProductRes])
def getProducts(page: int, perPage: int, db: Session = Depends(get_db)):
    if page == 1:
        page = 0
    produtcs = db.query(models.Product).limit(perPage).offset(page).all()

    return produtcs


@router.post("/", status_code=201, response_model=ProductRes)
def createProduct(product: Product, db: Session = Depends(get_db)):
    p = models.Product(**product.dict())
    db.add(p)
    db.commit()
    db.refresh(p)

    return p

@router.post("/image/{productId}", status_code=201)
def addImageToProduct(productId: int, productImg: ProductImage, db: Session = Depends(get_db)):
    findProducut = db.query(models.Product).filter(models.Product.id == productId)

    if findProducut is None:
        raise HTTPException(status_code=400, detail="Produto não encontrado")
    
    p = models.ProductsImages(image_url=productImg.image_url, product_id=productId)
    db.add(p)
    db.commit()

    return {"message": "imagem adiciona ao produto"}

@router.get("/images/{productId}", response_model=List[ProductImage])
def images(productId: int, db: Session = Depends(get_db)):
    productImgs = db.query(models.ProductsImages).filter(models.ProductsImages.product_id == productId).all()

    if productImgs is None:
        raise HTTPException(status_code=400, detail="Produto não encontrado")
    
    return productImgs

@router.put("/edit/{productId}", response_model=ProductRes)
def editProduct(productId: int, product: dict = Body(...), db: Session = Depends(get_db)):
    productQuery = db.query(models.Product).filter(models.Product.id == productId)

    findProduct = productQuery.first()

    if findProduct is None:
        raise HTTPException(status_code=400, detail="Produto não encontrado")

    dictProduct = findProduct.__dict__

    # checando se valores existem
    for keyP in product:
        if dictProduct.get(keyP) is None:
            raise HTTPException(status_code=400, detail="Elemento enviado é inválido")
            
    # transferindo valores
    for key in dictProduct:
        for keyB in product:
            if keyB == key:
                dictProduct[keyB] = product[key]

    dictProduct.pop("id")
    dictProduct["update_at"] = datetime.now()
    
    productQuery.update(dictProduct, synchronize_session=False)

    db.commit()

    return dictProduct
            

   
