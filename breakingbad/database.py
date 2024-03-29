from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData
import strawberry
from strawberry.arguments import is_unset

engine = create_engine("sqlite:///database.sqlite3", echo=True)
metadata = MetaData(engine)
Session = sessionmaker(bind=engine)


def _clean_filter(filters: strawberry.input) -> dict:
    clear_filter = filters.__dict__
    for key in list(clear_filter):
        if is_unset(clear_filter[key]):
            del clear_filter[key]
    return clear_filter


def element_exist(class_map, identifier: int) -> bool:
    if identifier < 0:
        return False
    session = Session()
    res = session.query(class_map).filter(class_map.identifier() == identifier).one()
    return True if res else False


def select_all(class_map, limit: int = None, offset: int = None) -> list:
    session = Session()

    res = (
        session.query(class_map)
        .filter(class_map.identifier() >= offset)
        .limit(limit)
        .all()
        if limit
        else session.query(class_map).filter(class_map.identifier() >= offset).all()
        if offset
        else session.query(class_map).all()
    )
    return res


def select_by_field(
    class_map, filters: strawberry.input, limit: int = None, offset: int = None
) -> list:
    session = Session()
    results = session.query(class_map).filter_by(**_clean_filter(filters)).all()
    return results


def _select_character_by_name(class_map, list_of_names) -> list:
    session = Session()
    results = session.query(class_map).filter(class_map.name.in_(list_of_names)).all()
    return results
