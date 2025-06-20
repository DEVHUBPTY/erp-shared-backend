from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import  Optional
from datetime import datetime


class CreateUserDTO(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=8)
    phone: Optional[str] = None
    address: Optional[str] = None

class UpdateUserDTO(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8)
    phone: Optional[str] = None
    address: Optional[str] = None

class AccountStatusResponse(BaseModel):
    balance: float
    is_delinquent: bool
    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    id: int
    user_id: str
    name: str
    email: EmailStr
    phone: Optional[str]
    address: Optional[str]
    account_status: Optional[AccountStatusResponse]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)



