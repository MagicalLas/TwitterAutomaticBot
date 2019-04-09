FROM python:3.7

COPY . .

RUN pip install tweepy
RUN pip install sanic
