from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class CreateRoleDTO(BaseModel):
    name: str = Field(..., example="admin")


class UpdateRoleDTO(BaseModel):
    name: Optional[str] = Field(None, example="vendedor")


class RoleResponse(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True) 