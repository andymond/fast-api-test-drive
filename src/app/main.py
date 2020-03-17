from fastapi import FastAPI

from app.api import ping
from app.db import engine, metadata, database

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.onvent("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)
