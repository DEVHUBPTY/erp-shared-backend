# ERP Shared Backend

Paquete compartido entre microservicios del ERP que contiene schemas, funciones, enums y utilidades comunes.

## Instalación

### Desde el repositorio local
```bash
# Instalar en modo desarrollo
poetry install

# O instalar directamente desde el directorio
pip install -e .
```

### Desde un repositorio remoto (cuando lo publiques)
```bash
pip install erp-shared
```

## Uso

```python
# Importar el módulo completo
import shared

# Importar módulos específicos
from shared import schemas, functions, enum, error, db

# Importar clases específicas
from shared.schemas.auth import User
from shared.functions.security import create_access_token
from shared.enum.order import OrderStatus
```

## Estructura del Paquete

```
shared/
├── __init__.py          # Configuración principal del paquete
├── db/                  # Utilidades de base de datos
├── enum/                # Enumeraciones comunes
├── error/               # Manejo de errores
├── functions/           # Funciones utilitarias
│   ├── api.py          # Funciones de API
│   ├── dev.py          # Funciones de desarrollo
│   └── security.py     # Funciones de seguridad
└── schemas/             # Esquemas Pydantic
    ├── auth/           # Esquemas de autenticación
    ├── cart.py         # Esquemas de carrito
    ├── order.py        # Esquemas de órdenes
    ├── product.py      # Esquemas de productos
    └── user.py         # Esquemas de usuario
```

## Desarrollo

### Instalar dependencias de desarrollo
```bash
poetry install --with dev
```

### Ejecutar tests
```bash
poetry run pytest
```

### Construir el paquete
```bash
poetry build
```

## Versión

Versión actual: 0.1.0

## Autor

captainsparrow10 <javier1009rm@gmail.com>
