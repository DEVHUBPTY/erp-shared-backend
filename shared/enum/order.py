from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "PENDIENTE"
    CONFIRMED = "CONFIRMADO"
    PREPARING = "PREPARANDO"
    COMPLETED = "COMPLETADA"
    CANCELLED = "CANCELADA"


class PriceStatus(str, Enum):
    CURRENT = "ACTUAL"
    PROMOTION = "PROMOCION"
    NEGOTIABLE = "NEGOCIABLE"


class PaymentMethod(str, Enum):
    CASH = "Efectivo"
    TRANSFER = "Transferencia"