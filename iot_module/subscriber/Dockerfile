FROM python:3.8-slim

WORKDIR /app

RUN pip install paho-mqtt==1.6.1

COPY ./subscriber.py .

CMD ["python", "subscriber.py"]
