import uvicorn
from fastapi import APIRouter, FastAPI

from app.api.handlers import user_router

app = FastAPI(title="fastapi_trening")


main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix="/user")
app.include_router(main_api_router)

if __name__ == "__main__":
    # run app on host and port
    uvicorn.run(app, host="0.0.0.0", port=8000)
