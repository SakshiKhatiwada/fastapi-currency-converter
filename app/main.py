from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.config import settings
from .api.c_converter import router as converter_router


app = FastAPI(title=settings.site_title, version=settings.site_version)

app.include_router(converter_router)


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>Currency Converter API</title>
        </head>
        <body>
            <h1>This is Currency Converter API created with FastAPI.</h1>
            <p><a href="/docs">Go to Swagger Docs</a></p>
        </body>
    </html>
    """


@app.get("/check", tags=["API"])
async def site_check():
    return {"status": "ok"}
