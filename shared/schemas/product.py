from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date

# --------------------
# CATEGORY
# --------------------
class CategoryCreateDTO(BaseModel):
    name: str

class CategoryUpdateDTO(BaseModel):
    name: Optional[str] = None

class CategoryResponse(CategoryCreateDTO):
    id: int
    model_config = ConfigDict(from_attributes=True)

# --------------------
# SUPPLIER
# --------------------
class SupplierCreateDTO(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None

class SupplierUpdateDTO(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class SupplierResponse(SupplierCreateDTO):
    id: int
    model_config = ConfigDict(from_attributes=True)

# --------------------
# PRODUCT
# --------------------
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    barcode: str
    image: str
    price: float
    stock: int
    expiration: Optional[date] = None

class CreateProductDTO(ProductBase):
    category_id: int
    supplier_id: int

class UpdateProductDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    barcode: Optional[str] = None
    image: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    expiration: Optional[date] = None
    category_id: Optional[int] = None
    supplier_id: Optional[int] = None

class ProductResponse(ProductBase):
    id: int
    category_id: int
    supplier_id: int
    model_config = ConfigDict(from_attributes=True)