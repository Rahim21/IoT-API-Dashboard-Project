FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Exposer le port
EXPOSE 5031

CMD ["python", "publisher.py"]
