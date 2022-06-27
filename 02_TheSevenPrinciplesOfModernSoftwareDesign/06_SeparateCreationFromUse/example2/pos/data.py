from enum import Enum, auto


class PaymentStatus(Enum):
    """Payment Status"""
    OPEN = auto()
    PAID = auto()
