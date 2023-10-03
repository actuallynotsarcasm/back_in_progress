from typing import Union
from pydantic import BaseModel


class CarModel(BaseModel):
    car_slug: str
    brand: str
    model: str
    complement: str
    photo_id: Union[int, None] = None
    price: int
    trade_in_profit: int
    credit_profit: int


class DealerModel(BaseModel):
    dealer_slug: str
    name: str
    address: str


class ModeratorModel(BaseModel):
    dealer_id: int
    name: str
    surname: str
