"""
Module de configuration pour l'application MongoDB
"""

# Import direct des éléments principaux pour faciliter l'utilisation
from .auth_config import MONGODB_CONFIG, ROLES_CONFIG, USERS_CONFIG, MESSAGES

# Définition de ce qui est accessible depuis l'extérieur
__all__ = ['MONGODB_CONFIG', 'ROLES_CONFIG', 'USERS_CONFIG', 'MESSAGES']
