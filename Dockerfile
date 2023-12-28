#                      _       
#   _ __ ___   ___ __ _| |_ ___ 
#  | '__/ _ \ / __/ _` | __/ __|
#  | | | (_) | (_| (_| | |_\__ \
#  |_|  \___/ \___\__,_|\__|___/
#
#  https://github.com/rocats/apigateway-interceptor
#
#  Copyright (C) 2023 @rocats
#
#  This is a self-hosted software, liscensed under the Apache License. 
#  See /License for more information.

ARG PYTHON_VERSION
ARG APP_DIR="/app"

FROM python:${PYTHON_VERSION}-slim-bullseye as builder

ARG APP_DIR

WORKDIR ${APP_DIR}

ADD requirements.txt .

RUN python3 -m venv venv && \
    venv/bin/pip install -r requirements.txt

ADD app.py .

ENTRYPOINT [ "./venv/bin/python" ]
CMD [ "app.py" ]
