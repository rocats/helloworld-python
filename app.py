import os
import structlog
import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import Response


app = FastAPI()


@app.post("/")
async def webhook():
    return Response(
        content="",
        status_code=status.HTTP_204_NO_CONTENT,
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    logger = structlog.get_logger()
    logger.info(f"App loaded, listen on port {port}")
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True, workers=1)
