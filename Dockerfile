# pull official base image
FROM python:3

COPY . /app

# set work directory
WORKDIR /app

# set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=/app/venv

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# install dependencies
RUN /bin/sh venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

ENV GUNICORN_CMD_ARGS="--workers 3 --bind 0.0.0.0:8000 -m 007"

CMD ["./venv/bin/gunicorn", "wsgi:app"]
