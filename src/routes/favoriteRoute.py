from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .. import auth, models
from ..database import get_db

router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.post("/toggle/{productId}")
def toggleFavorite(productId: int, user: int = Depends(auth.getCurrentUser), db: Session= Depends(get_db)):
    findProduct = db.query(models.Product).filter(models.Product.id == productId).first()

    if findProduct is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    checkAction = db.query(models.FavoriteProducts).filter(models.FavoriteProducts.product_id == productId, models.FavoriteProducts.user_id == user.id)

    itemFavorite = checkAction.first()
    
    if itemFavorite is None:
        f = models.FavoriteProducts(product_id=productId, user_id=user.id)
        db.add(f)
        db.commit()
        return JSONResponse(status_code=201, content={"message": "adicionado ao favorito"})
    else:
        checkAction.delete(synchronize_session=False)
        db.commit()
        return JSONResponse(status_code=200, content={"message": "favorito removido"})