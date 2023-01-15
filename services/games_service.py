from infrastructure.word_cases import word_cases
from models import db_session
from models.models import *
from sqlalchemy.future import select
from typing import Optional


async def get_game_by_slug(game_slug: str) -> Optional[Games]:
    async with db_session.create_async_session() as session:
        query = select(Games).filter(Games.slug == game_slug)
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def get_all_game_slugs() -> list[Games.slug]:
    async with db_session.create_async_session() as session:
        query = select(Games)
        result = await session.execute(query)
        return list({g.slug for g in result.scalars()})


async def get_top_games() -> list[Games]:
    async with db_session.create_async_session() as session:
        """ Максимум 12 элементов! """
        query = select(Games).order_by(Games.rating.desc()).limit(12)
        result = await session.execute(query)
        return result.scalars()


async def get_new_games() -> list[Games]:
    async with db_session.create_async_session() as session:
        """ Максимум 12 элементов! """
        query = select(Games).order_by(Games.created_date).limit(12)
        result = await session.execute(query)
        return result.scalars()


async def get_categories_by_game_id(game_id: str) -> list[str]:
    async with db_session.create_async_session() as session:
        query = select(Categories).join(Categories.games).filter(Games.id == game_id)
        result = await session.execute(query)
        return list({c.category_name for c in result.scalars()})


async def get_gallery_by_game_id(game_id: str) -> list[str]:
    async with db_session.create_async_session() as session:
        query = select(Gallery) \
            .filter(Gallery.game_id == game_id)
        results = await session.execute(query)
        images = results.scalars()
        return list({i.url_image for i in images})


async def get_tags_by_game_id(game_id: str) -> list[str]:
    async with db_session.create_async_session() as session:
        query = select(Tags).join(Tags.games).filter(Games.id == game_id)
        result = await session.execute(query)
        return list({c.tag_name for c in result.scalars()})


async def get_link_games_by_game_id(game_id: str) -> list[str]:
    async with db_session.create_async_session() as session:
        query = select(SimilarGames) \
            .filter(SimilarGames.game_id == game_id)
        results = await session.execute(query)
        urs = results.scalars()
        return list({u.url_similar_game for u in urs})


async def get_publisher_by_game_id(game_id: str) -> Optional[Publishers]:
    async with db_session.create_async_session() as session:
        query = select(Publishers).join(Games.publisher).filter(Games.id == game_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def get_language_by_game_id(game_id: str) -> Optional[Languages]:
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

        comment_case = await word_cases(str(comments_count))
        result = str(comments_count) + ' ' + comment_case
        return result


async def get_games_from_search(search: str) -> list[Games]:
    search_word = "%" + search + "%"
    async with db_session.create_async_session() as session:
        """ Максимум 30 элементов! """
        query = select(Games).filter(Games.slug.like(search_word)).limit(30)
        result = await session.execute(query)
        return result.scalars()


async def get_games_and_count_page_by_category_slug_and_page(slug: str, page: str | None) -> \
        tuple[Optional[Games], int]:
    async with db_session.create_async_session() as session:
        """ Максимум 30 элементов! """
        lim = 30
        ofst = 0
        if int(page) > 1:
            lim = int(page) * lim
            ofst = (int(page) - 1) * lim

        query = select(Games).join(Games.categories).filter(Categories.slug == slug).offset(ofst).limit(lim)
        result = await session.execute(query)

        query2 = select(Games).join(Games.categories).filter(Categories.slug == slug)
        result2 = await session.execute(query2)
        count = 0
        for i in result2.scalars():
            count += 1

        return result.scalars(), count
