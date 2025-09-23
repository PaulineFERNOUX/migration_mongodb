FROM python:3.12-slim

WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de configuration
COPY pyproject.toml poetry.lock ./

# Installer Poetry
RUN pip install poetry

# Configurer Poetry
RUN poetry config virtualenvs.create false

# Installer les dépendances poetry
RUN poetry install --no-root

# Copier le code source
COPY . .

# Ajouter /app au PYTHONPATH pour que Python trouve le module config
ENV PYTHONPATH=/app

# Commande par défaut
CMD ["python", "scripts/migration.py"]