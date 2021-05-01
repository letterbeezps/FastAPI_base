from fastapi import APIRouter
from fastapi import Depends, HTTPException

from typing import Optional

from app.view_models.base import Item
from app.view_models.base import ModelName
from app.models import Session

from app.models.base import BaseTable as MBaseTable
from app.view_models.base import BaseTableCreate as VMBaseTableCreate
from app.view_models.base import BaseTableModel as VMBaseTableModel 
from app.controller import base as Cbase

def get_db():
    db = Session()
    yield db
    # try:
    #     yield db
    # finally:
    #     db.close()

baseRouter = APIRouter()

#################################################################
# create base
@baseRouter.post('/base/db/create_base', response_model=VMBaseTableModel)
def create_base(base: VMBaseTableCreate, db: Session = Depends(get_db)):
    db_base = Cbase.get_base_by_name(db, base_name=base.name)
    if db_base:
        raise HTTPException(status_code=404, detail="name already exited")
    return Cbase.create_base(db, base)

###################################################################
@baseRouter.get('/base')
async def base():
    return {"msg": "test base"}

####################################################################
# path parmaters
@baseRouter.get("/base/items/{item_id}")
# path parameter will pass to func as the argument item_id
# declare the type of path parameter 
async def read_item(item_id: int, q: Optional[str] = None):
    if q:
        return {'item_id': item_id, "q": q}
    return {"item_id": item_id}

####################################################################
# parameter is file_path
@baseRouter.get('/base/files/{file_path:path}')
async def read_file(file_path: str):
    return {"file_path": file_path}

@baseRouter.get("/base/model/{model_name}")
# create a parameter with a type annotation use the enum class
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


####################################################################
# query parameters
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# /base/items/?skip=0&limit=10
@baseRouter.get("/base/fakedb/items")
async def read_item_query(skip: int, limit: int = 10):
    return fake_items_db[skip : skip + limit]

####################################################################
# declare a request body
@baseRouter.post("/base/item_query/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict