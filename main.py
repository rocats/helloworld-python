import json
import structlog
from fastapi import FastAPI, Request, status
from fastapi.responses import Response
from cloudevents.http import from_http

app = FastAPI()
logger = structlog.get_logger()


@app.post("/")
async def webhook(request: Request):
    try:
        body = json.dumps(await request.json())
        logger.debug(body)
        event = from_http(dict(request.headers), body)

        logger.debug("Function loaded")
        logger.debug(f"Received event with ID: {event['id']} and data {event.data}")
        logger.debug(f"Cloudevent: {event}")
        logger.info("hello world!")

        return Response(
            content="",
            status_code=status.HTTP_204_NO_CONTENT,
        )

    except Exception as err:
        logger.error(str(err))
