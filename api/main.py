from fastapi import FastAPI
import auth.router

app = FastAPI()
app.include_router(auth.router.router)


@app.get("/")
async def hc():
    return "server is running"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
