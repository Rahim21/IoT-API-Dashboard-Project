# Dockerfile for API
FROM python:3.8-slim

WORKDIR .

# Copier l'ensemble du contenu local dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt


# Commande par défaut pour lancer l'application
CMD ["python", "app.py"]
