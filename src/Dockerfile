FROM python:latest

RUN mkdir /src
COPY  .  /src

WORKDIR /src


RUN pip install -r requirements.txt


CMD  gunicorn -w 4 --bind 0.0.0.0:8000  shop.wsgi 

 
