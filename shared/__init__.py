"""
ERP Shared Package

Paquete compartido entre microservicios del ERP.
Contiene schemas, funciones, enums y utilidades comunes.

Uso:
    import shared
    from shared import schemas, functions, enum, error, db
"""

__version__ = "0.1.0"
__author__ = "captainsparrow10"
__email__ = "javier1009rm@gmail.com"

# Importar módulos principales para facilitar el acceso
from . import schemas
from . import functions
from . import enum
from . import error
from . import db

# Importar clases y funciones más comunes para acceso directo
try:
    from .schemas.auth.user import User
    from .schemas.auth.authentication import Token, TokenData
    from .functions.security import create_access_token, verify_token
    from .enum.order import OrderStatus
except ImportError:
    # Si algún módulo no está disponible, no fallar
    pass

__all__ = [
    # Módulos principales
    "schemas",
    "functions", 
    "enum",
    "error",
    "db",
    # Metadatos
    "__version__",
    "__author__",
    "__email__",
    # Clases comunes (si están disponibles)
    "User",
    "Token", 
    "TokenData",
    "create_access_token",
    "verify_token",
    "OrderStatus",
]

# Mensaje de confirmación solo en desarrollo
import os
if os.getenv("ERP_SHARED_DEBUG"):
    print("Shared module loaded ✅")