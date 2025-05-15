from fastapi import FastAPI
from app.config import settings
from .api.c_converter import router as converter_router


app = FastAPI(title=settings.site_title, version=settings.site_version)

app.include_router(converter_router)


@app.get("/", tags=["API"])
async def site_check():
    return {"status": "ok"}
