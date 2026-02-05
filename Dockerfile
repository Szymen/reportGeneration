FROM python:3.9.9-buster
#
#RUN apk --no-cache add musl-dev linux-headers g++

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y wkhtmltopdf

RUN python -m pip install --upgrade pip && \
    pip3 install -r requirements.txt

ENTRYPOINT ["python3.9", "reportGenerator.py"]

#COPY report.py Prettyfier.py