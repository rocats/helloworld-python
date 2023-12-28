import os
import structlog
import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import Response


app = FastAPI()
logger = structlog.get_logger()


@app.post("/")
async def webhook():
    logger.info("hello world!")
    return Response(
        content="",
        status_code=status.HTTP_204_NO_CONTENT,
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    logger.info(f"App loaded, listen on port {port}")
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True, workers=1)
