FROM python:3.8-slim-buster

ENV FLASK_APP='kvservice'
ENV FLASK_ENV='development'

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "flask", "run", "--host=0.0.0.0"]
