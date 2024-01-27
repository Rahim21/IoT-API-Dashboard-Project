FROM python:3.8-slim

WORKDIR /app

RUN pip install paho-mqtt==1.6.1

COPY ./publisher.py .

CMD ["python", "publisher.py"]
