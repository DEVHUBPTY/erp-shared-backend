from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional


class CreateUserDTO(BaseModel):
    user_id: str = Field(..., example="user_123")
    email: EmailStr
    password: str

class UpdateUserDTO(BaseModel):
    user_id: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    user_id: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)  