from __future__ import annotations
from sqlalchemy import Table, Column, Integer, String, JSON
from sqlalchemy.orm import mapper
from database import metadata
from schema import Character, Episode, Death, Quote

character_tbl = Table(
    Character.__tablename__,
    metadata,
    Column("char_id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("birthday", String(10)),
    Column("occupation", JSON),
    Column("img", String(200)),
    Column("status", String(15)),  # at least "presumed dead"
    Column("nickname", String(40)),
    Column("portrayed", String(50)),
    Column("serie", String(30)),
    Column("season_appearance", JSON),
    Column("better_call_saul_appearance", JSON),
)

mapper(Character, character_tbl)

episode_tbl = Table(
    Episode.__tablename__,
    metadata,
    Column("episode_id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("season", Integer),
    Column("episode", Integer),
    Column("air_date", String(200)),
    Column("series", String(35)),
    Column("characters_name", JSON),
)

mapper(Episode, episode_tbl)

quote_tbl = Table(
    Quote.__tablename__,
    metadata,
    Column("quote_id", Integer, primary_key=True),
    Column("quote", String(50)),
    Column("author_id", Integer),
    Column("series", String(35)),
)

mapper(Quote, quote_tbl)

death_tbl = Table(
    Death.__tablename__,
    metadata,
    Column("death_id", Integer, primary_key=True),
    Column("death", String(50)),
    Column("cause", String(50)),
    Column("season", Integer),
    Column("episode", Integer),
    Column("number_of_deaths", Integer),
    Column("last_words", String(35)),
    Column("responsible", String(35)),
)

mapper(Death, death_tbl)
