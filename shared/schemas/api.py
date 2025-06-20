
from typing import Generic, Literal, TypeVar, Optional
from pydantic import BaseModel
T = TypeVar("T")
class ResponseAPI(BaseModel, Generic[T]):
    status: Literal["success", "error"]
    data: Optional[T] = None
    message: Optional[str] = None
    error: Optional[str] = None