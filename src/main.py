from fastapi import FastAPI
from .routes import usersRoute, ordersRoute, productsRoute
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usersRoute.router)
app.include_router(ordersRoute.router)
app.include_router(productsRoute.router)

