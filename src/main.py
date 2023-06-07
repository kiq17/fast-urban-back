from fastapi import FastAPI
from .routes import usersRoute, ordersRoute, productsRoute


app = FastAPI()

app.include_router(usersRoute.router)
app.include_router(ordersRoute.router)
app.include_router(productsRoute.router)

