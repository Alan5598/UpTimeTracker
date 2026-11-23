from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routes import checks, health
from app.util.database import dispose_engine
from app.util.errors import register_error_handlers
from app.util.logs import register_logging
from app.util.redis import close_redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await dispose_engine()
    await close_redis()


app = FastAPI(title="PulseMonitor API", version="0.1.0", lifespan=lifespan)
register_logging(app)
register_error_handlers(app)

app.include_router(health.router)
app.include_router(checks.router)
