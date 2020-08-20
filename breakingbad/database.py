from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import strawberry
from strawberry.arguments import is_unset
Base = automap_base()
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
    results = session.query(model).filter_by(**_clean_filter(filters)).all()
    return results
