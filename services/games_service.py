from typing import Optional, List, Any

import sqlalchemy

from models import db_session
from models.models import *
from sqlalchemy.future import select
from typing import List, Optional
from sqlalchemy import func

async def get_game_by_id(game_id: str) -> Optional[Games]:
    async with db_session.create_async_session() as session:
        query = select(Games).filter(Games.id == game_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def get_top_games() -> list[Games]:
    """ Максимум 12 элементов! """
    async with db_session.create_async_session() as session:
        query = select(Games).order_by(Games.rating.desc()).limit(12)
        result = await session.execute(query)
        return result.scalars()


async def get_new_games() -> list[Games]:
    """ Максимум 12 элементов! """
    async with db_session.create_async_session() as session:
        query = select(Games).order_by(Games.created_date).limit(12)
        result = await session.execute(query)
        return result.scalars()


async def get_categories_by_game_id(game_id: str) -> list[Any]:
    async with db_session.create_async_session() as session:
        query = select(Categories).join(Categories.games).filter(Games.id == game_id)
        result = await session.execute(query)
        return list({c.category_name for c in result.scalars()})


async def get_gallery_by_game_id(game_id: str) -> list[Any]:
    async with db_session.create_async_session() as session:
        query = select(Gallery) \
            .filter(Gallery.game_id == game_id)
        results = await session.execute(query)
        images = results.scalars()
        return list({i.url_image for i in images})


async def get_tags_by_game_id(game_id: str) -> list[Any]:
    async with db_session.create_async_session() as session:
        query = select(Tags).join(Tags.games).filter(Games.id == game_id)
        result = await session.execute(query)
        return list({c.tag_name for c in result.scalars()})


async def get_link_games_by_game_id(game_id: str) -> list[Any]:
    async with db_session.create_async_session() as session:
        query = select(SimilarGames) \
            .filter(SimilarGames.game_id == game_id)
        results = await session.execute(query)
        urs = results.scalars()
        return list({u.url_similar_game for u in urs})


async def get_publisher_by_game_id(game_id: str) -> list[Any]:
    async with db_session.create_async_session() as session:
        query = select(Publishers).join(Games.publisher).filter(Games.id == game_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def get_language_by_game_id(game_id: str) -> list[Any]:
    async with db_session.create_async_session() as session:
        query = select(Languages).join(Games.language).filter(Games.id == game_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def get_comments_count_by_game_id(game_id: str) -> str:
    async with db_session.create_async_session() as session:

        query = select(Comments).filter(Comments.game_id == game_id)
        result = await session.execute(query)
        comments_count = 0
        for i in result.scalars():
            comments_count += 1
        # results = await session.execute(query)
        # print(str(result))
        # print(str(result.scalars))
        return str(comments_count)

