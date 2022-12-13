from typing import Optional
from models import db_session
from models.models import *
from sqlalchemy.future import select
from sqlalchemy import func
import sqlalchemy.orm
from typing import List, Optional
from sqlalchemy.orm import joinedload


async def is_videogame() -> bool:
    async with db_session.create_async_session() as session:
        query = select(func.count(Games.is_videogame))
        results = await session.execute(query)
        return results.scalar()


async def get_title() -> str:
    async with db_session.create_async_session() as session:
        query = select(func.count(Games.title))
        results = await session.execute(query)
        return results.scalar()


async def get_categories_by_game(game_id) -> List[Categories]:
    async with db_session.create_async_session() as session:
        cats = session.query(Categories). \
            options(joinedload(Categories.games)). \
            where(Games.id == game_id)

        return list({c.category_name for c in cats})
