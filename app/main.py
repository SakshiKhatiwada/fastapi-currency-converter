from fastapi import FastAPI
from app.config import settings


app = FastAPI(title=settings.site_title, version=settings.site_version)


@app.get("/", tags=["API"])
async def site_check():
    return {"status": "ok"}