FROM python:3.11.1-slim-buster

COPY . /app

WORKDIR /app

RUN pip install -U pip pdm packaging==21.3 --no-cache-dir
RUN pdm install
RUN python -m compileall -f -j4 -- *

EXPOSE 8000

CMD pdm run gunicorn server:app --config gunicorn.conf.py
