from fastapi import FastAPI
import auth.router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(auth.router.router)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hc")
async def hc():
    return "server is running"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
