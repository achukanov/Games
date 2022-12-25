""" feedback and subscription"""
from models import db_session
from models.models import Subscribers


# TODO: добавить форму обратной связи

async def subscribe(email: str) -> bool:
    subscriber = Subscribers()
    subscriber.email = email

    async with db_session.create_async_session() as session:
        session.add(subscriber)
        await session.commit()
    return True
