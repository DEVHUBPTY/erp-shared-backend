from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from typing import Optional, Dict, Union
from datetime import datetime, timedelta

# Configuración de JWT
SECRET_KEY = "mi_clave_super_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5
REFRESH_TOKEN_EXPIRE_DAYS = 1

# Esquema Bearer para FastAPI
security_scheme = HTTPBearer(auto_error=False)

# --------------------------------------------------
# Función para crear Access Token
# --------------------------------------------------
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# --------------------------------------------------
# Función para crear Refresh Token (sin datos sensibles)
# --------------------------------------------------
def create_refresh_token(data: dict = {}) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# --------------------------------------------------
# Decodifica y valida un JWT
# --------------------------------------------------
def decode_token(token: str) -> Dict[str, Union[str, int]]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado"
        )

# --------------------------------------------------
# Extrae el usuario actual desde el token
# --------------------------------------------------
def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security_scheme),
    request: Optional[Request] = None
) -> Dict[str, Union[str, None]]:
    token = None

    # 1. Verificar token por header (Authorization: Bearer)
    if credentials and credentials.scheme.lower() == "bearer":
        token = credentials.credentials

    # 2. O buscar token en cookies (ej: desde navegador web)
    elif request:
        token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="Token no proporcionado")

    payload = decode_token(token)

    user_id = payload.get("user_id")
    role = payload.get("role")

    if not user_id or not role:
        raise HTTPException(status_code=403, detail="Token inválido o incompleto")

    return {
        "user_id": user_id,
        "role": role,
        "access_token": token,
        "refresh_token": request.cookies.get("refresh_token") if request else None
    }