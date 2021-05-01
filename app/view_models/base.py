from enum import Enum
from pydantic import BaseModel


from typing import Optional
from datetime import datetime

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# View model for Basetable

class BaseTable(BaseModel):
    name: str
    text: str

class BaseTableCreate(BaseTable):
    pass

# compatible with orm
class BaseTableModel(BaseTable):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True