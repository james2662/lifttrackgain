from fastapi import FastAPI

api = FastAPI(
    debug=True,
    version="0.0.1",
    redoc_url=None,
)


@api.get("/")
async def root(): 
    return {"message": "Hello World!"}