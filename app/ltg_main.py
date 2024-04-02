from fastapi import FastAPI

ltg_app = FastAPI()


@ltg_app.get("/test/")
async def get_test():
    return "Hello Tester"