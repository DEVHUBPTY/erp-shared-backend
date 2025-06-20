from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class CreatePermissionDTO(BaseModel):
    path: str = Field(..., example="/api/products")
    method: str = Field(..., example="GET")
    description: str = Field(..., example="List all products")

    


class UpdatePermissionDTO(BaseModel):
    path: Optional[str] = Field(None, example="/api/products")
    method: Optional[str] = Field(None, example="POST")
    description: Optional[str] = Field(None, example="Create a new product")



class PermissionResponse(BaseModel):
    id: int
    path: str
    method: str
    description: str

    model_config = ConfigDict(from_attributes=True)