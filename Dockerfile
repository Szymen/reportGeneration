FROM python:3.9.9-buster
#
#RUN apk --no-cache add musl-dev linux-headers g++

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && \
    pip3 install -r requirements.txt


COPY Report.py Prettyfier.py