from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
from app.core.config import settings
from app.api.endpoints import router
from app.core.rate_limiter import limiter
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events."""
    # Startup
    logger.info("Starting up Trade Opportunities API...")
    yield
    # Shutdown
    logger.info("Shutting down Trade Opportunities API...")

app = FastAPI(
    title="Trade Opportunities API",
    description="API for analyzing market data and providing trade opportunity insights for Indian sectors",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Include routers
app.include_router(router, prefix="/api/v1")

@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Trade Opportunities API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoint": "GET /api/v1/analyze/{sector}"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}