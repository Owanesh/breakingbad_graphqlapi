from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = automap_base()
engine = create_engine("sqlite:///database.sqlite")
Session = sessionmaker(bind=engine)
Base.prepare(engine, reflect=True)


def select_all(class_map) -> list:
    session = Session()
    return session.query(Base.classes[class_map.__tablename__]).all()
