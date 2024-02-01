FROM python:3.8

WORKDIR /app

# Copier l'ensemble du contenu local dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port
EXPOSE 5020

CMD ["python", "app.py"]