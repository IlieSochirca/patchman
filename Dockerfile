# pull base image for this project
FROM python:3.8-alpine as base
FROM base as builder

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 #Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONUNBUFFERED 1

WORKDIR /local

COPY blog/requirements.txt src/requirements.txt

# install project dependencies

RUN pip install --upgrade pip
RUN pip install --user -r src/requirements.txt

# Inherit from previously built image
FROM base

WORKDIR /src

COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH


COPY ./blog /src

COPY ./blog/entrypoint.sh /src/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

CMD gunicorn --reload --workers=3 --worker-tmp-dir /dev/shm blog.wsgi:application --bind :7070