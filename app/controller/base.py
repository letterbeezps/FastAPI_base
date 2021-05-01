from sqlalchemy.orm import Session

from app.models.base import BaseTable as MBaseTable
from app.view_models.base import BaseTableCreate as VMBaseTableCreate

def get_base_by_id(db: Session, base_id: int):
    return db.query(MBaseTable)\
            .filter(MBaseTable.id == base_id)\
            .first()

def get_base_by_name(db: Session, base_name: str):
    return db.query(MBaseTable)\
            .filter(MBaseTable.name == base_name)\
            .first()

def get_bases(db: Session, skip: int = 0, limit: int = 10):
    return db.query(MBaseTable)\
            .offset(skip)\
            .limit(limit)\
            .all()

def create_base(db: Session, base: VMBaseTableCreate):
    db_base = MBaseTable(
        name=base.name,
        text=base.text
    )
    db.add(db_base)
    db.commit()
    db.refresh(db_base)
    return db_base

