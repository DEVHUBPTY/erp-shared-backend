"""
ERP Shared Package

Paquete compartido entre microservicios del ERP.
Contiene schemas, funciones, enums y utilidades comunes.
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

__all__ = [
    "schemas",
    "functions", 
    "enum",
    "error",
    "db",
    "__version__",
    "__author__",
    "__email__"
]

print("Shared module loaded ✅")