from typing import Optional, List, Any
from models import db_session
from models.models import *
from sqlalchemy.future import select
from typing import List, Optional


async def get_all_categories() -> list[Categories]:
    async with db_session.create_async_session() as session:
        query = select(Categories)
        result = await session.execute(query)
        return result.scalars()


async def get_all_publishers() -> list[Publishers]:
    async with db_session.create_async_session() as session:
        query = select(Publishers)
        result = await session.execute(query)
        return result.scalars()


async def get_category_by_slug(category_slug: str) -> Optional[Categories]:
    async with db_session.create_async_session() as session:
        query = select(Categories).filter(Categories.slug == category_slug)
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def get_categories_pages() -> []:
    categories = await get_all_categories()
    res = []
    for c in categories:
        async with db_session.create_async_session() as session:
            query = select(Games).join(Games.categories).filter(Categories.slug == c.slug)
            result = await session.execute(query)
            pages_count = 0
            r = result.scalars()
            for _ in r:
                pages_count += 1
            for p in range(pages_count + 1):
                res.append({"category": c.slug, "page": p})
    return res


# async def get_categories_by_game_id(category_id: str) -> list[Any]:
#     async with db_session.create_async_session() as session:
#         query = select(Categories).join(Categories.games).filter(Games.id == game_id)
#         result = await session.execute(query)
#         return list({c.category_name for c in result.scalars()})
#
#
# async def get_gallery_by_game_id(category_id: str) -> list[Any]:
#     async with db_session.create_async_session() as session:
#         query = select(Gallery) \
#             .filter(Gallery.game_id == game_id)
#         results = await session.execute(query)
#         images = results.scalars()
#         return list({i.url_image for i in images})
#
#
# async def get_tags_by_game_id(game_id: str) -> list[Any]:
#     async with db_session.create_async_session() as session:
#         query = select(Tags).join(Tags.games).filter(Games.id == game_id)
#         result = await session.execute(query)
#         return list({c.tag_name for c in result.scalars()})
#
#
# async def get_link_games_by_game_id(game_id: str) -> list[Any]:
#     async with db_session.create_async_session() as session:
#         query = select(SimilarGames) \
#             .filter(SimilarGames.game_id == game_id)
#         results = await session.execute(query)
#         urs = results.scalars()
#         return list({u.url_similar_game for u in urs})
#
#
# async def get_publisher_by_game_id(game_id: str) -> list[Any]:
#     async with db_session.create_async_session() as session:
#         query = select(Publishers).join(Games.publisher).filter(Games.id == game_id)
#         result = await session.execute(query)
#         return result.scalar_one_or_none()
#
#
# async def get_language_by_game_id(game_id: str) -> list[Any]:
#     async with db_session.create_async_session() as session:
#         query = select(Languages).join(Games.language).filter(Games.id == game_id)
#         result = await session.execute(query)
#         return result.scalar_one_or_none()
