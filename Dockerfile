# FROM python:3.8-slim-buster
FROM python:3.10.0-alpine3.15

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY src src
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "executable" ]


EXPOSE 5000

ENTRYPOINT ['python3']
CMD ['app.py']

