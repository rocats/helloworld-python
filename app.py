import os
import structlog
import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()


@app.post("/")
async def webhook():
    return JSONResponse(
        content=jsonable_encoder({"message": "hello world!"}),
        status_code=status.HTTP_200_OK,
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    logger = structlog.get_logger()
    logger.info(f"App loaded, listen on port {port}")
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True, workers=1)
