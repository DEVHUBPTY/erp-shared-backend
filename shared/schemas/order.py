from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime
from shared.enum.order import OrderStatus, PaymentMethod, PriceStatus

class OrderDetailResponse(BaseModel):
    id: int
    order_number: str
    product_id: str
    quantity: int
    unit_price: float
    original_total_price: float
    unit_negotiable_price: float
    total_price: float
    total_negotiable_price: float
    status: PriceStatus
    model_config = ConfigDict(from_attributes=True)  

class OrderResponse(BaseModel):
    id: int
    order_number: str
    created_at: datetime
    status: OrderStatus
    total_amount: float
    total_amount_paid: float
    total_amount_pending: float
    total_negotiable: float
    delivery_date: datetime
    payment_method: Optional[PaymentMethod] = None
    proof_of_payment: Optional[str]
    customer_id: int
    seller_id: int
    seller_notes: Optional[str]
    admin_notes: Optional[str]
    details: List[OrderDetailResponse]
    model_config = ConfigDict(from_attributes=True)  

class CreateOrderDetailDTO(BaseModel):
    product_id: str
    order_number: str
    quantity: int
    unit_price: float
    original_total_price: float
    unit_negotiable_price: float
    total_price: float
    total_negotiable_price: float
    status: PriceStatus


class CreateOrderDTO(BaseModel):
    order_number: str
    created_at: datetime
    delivery_date: datetime
    customer_id: int
    seller_id: int
    status: Optional[OrderStatus] = OrderStatus.PENDING
    total_amount: float
    total_amount_paid: float
    total_amount_pending: float
    total_negotiable: float
    payment_method: Optional[PaymentMethod]
    proof_of_payment: Optional[str]
    seller_notes: Optional[str]
    admin_notes: Optional[str]
    details: List[CreateOrderDetailDTO]
 
class UpdateOrderDTO(BaseModel):
    status: Optional[OrderStatus] = None
    payment_method: Optional[PaymentMethod] = None
    proof_of_payment: Optional[str] = None
    seller_notes: Optional[str] = None
    admin_notes: Optional[str] = None
    details: Optional[List[CreateOrderDetailDTO]] = None