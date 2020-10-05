
from models_relationships import Base

from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, bindparam, sql
import strawberry
from strawberry.arguments import is_unset
from sqlalchemy.sql import text


engine = create_engine("sqlite:///database.sqlite")
Session = sessionmaker(bind=engine)
Base.prepare(engine, reflect=True)


def _clean_filter(filters: strawberry.input) -> dict:
    clear_filter = filters.__dict__ 
    for key in list(clear_filter):
        if is_unset(clear_filter[key]):
            del(clear_filter[key])
    return clear_filter


def select_all(class_map) -> list:
    session = Session()
    return session.query(Base.classes[class_map.__tablename__]).all()


def select_by_field(class_map, filters: strawberry.input) -> list:
    session = Session()
    model = Base.classes[class_map.__tablename__]
    print(filters)
    results = session.query(model).filter_by(**_clean_filter(filters)).all()
    return results


def _select_character_by_name(class_map, list_of_names) -> list:
    session = Session()
    model = Base.classes[class_map.__tablename__]
    results = session.query(model).filter(model.name.in_(list_of_names)).all()
    return results
