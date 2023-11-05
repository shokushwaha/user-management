from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from fastapi_utils.tasks import repeat_every
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",  # Adjust with your front-end application URL
    # Add additional allowed origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

limiter = RateLimiter(store="memory", key_func=lambda: "global", rate="5/minute")

app.state.limiter = limiter

app.include_router(user_router, prefix="/users", tags=["users"])

@app.on_event("startup")
@repeat_every(seconds=60)
async def cleanup_limiter():
    await limiter.cleanup()

@app.middleware("http")
async def add_rate_limiter_header(request, call_next):
    response = await call_next(request)
    response.headers['X-RateLimit-Limit'] = str(limiter.rate)
    return response
