from fastapi import FastAPI
from src.proxies.router import router as proxies_router
from src.auth.service import router as auth_router
from src.database import create_db_and_tables

app = FastAPI(title="Api for proxy")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(proxies_router)
app.include_router(auth_router)