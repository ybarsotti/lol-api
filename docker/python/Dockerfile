FROM python:3.8

RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . .

CMD sleep 360h