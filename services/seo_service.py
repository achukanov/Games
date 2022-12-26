from models import db_session
from models.models import Seo
from sqlalchemy.future import select
from typing import Optional


async def get_seo(seo_page: str) -> Optional[Seo]:
    async with db_session.create_async_session() as session:
        query = select(Seo).filter(Seo.page == seo_page)
        result = await session.execute(query)
        return result.scalar_one_or_none()
