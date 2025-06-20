from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


# ResponseAPI 
class CartProductResponse(BaseModel):
    id: int
    product_id: str
    quantity: int
    unit_price: float
    unit_negotiable_price: Optional[float] = None
    total_price: float
    total_negotiable_price: Optional[float] = None
    model_config = ConfigDict(from_attributes=True)

class CartResponse(BaseModel):
    id: int
    seller_id: int
    customer_id: int
    cart_id: str
    seller_notes: Optional[str]
    product_list: List[CartProductResponse]
    created_at: datetime
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True) 

# Create Cart Product DTO
class CreateCartProduct(BaseModel):
    product_id: str
    quantity: int
    unit_price: Optional[float] = None
    unit_negotiable_price: Optional[float] = None
    total_price: Optional[float] = None
    total_negotiable_price: Optional[float] = None
    
class CreateCartDTO(BaseModel):
    seller_id: int
    customer_id: int
    seller_notes: Optional[str] = None
    product_list: List[CreateCartProduct]

# Update Cart DTO
class AddCartProductDTO(BaseModel):
    product_id: str
    quantity: int
    unit_price: Optional[float] = None
    unit_negotiable_price: Optional[float] = None
    total_price: Optional[float] = None
    total_negotiable_price: Optional[float] = None

# Delete Cart Response DTO
    
class RemoveCartProductDTO(BaseModel):
    product_id: str
    cart_id: str