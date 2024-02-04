FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/ /app

EXPOSE 5020

CMD ["python", "app.py"]
