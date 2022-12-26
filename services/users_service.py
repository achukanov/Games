from models import db_session
from models.models import Subscribers, Feedback


async def subscribe(email: str) -> bool:
    subscriber = Subscribers()
    subscriber.email = email

    async with db_session.create_async_session() as session:
        session.add(subscriber)
        await session.commit()
    return True


async def feedback(first_name: str, email: str, title: str, message: str) -> bool:
    feed = Feedback()
    feed.first_name = first_name,
    feed.email = email,
    feed.title = title,
    feed.message = message

    async with db_session.create_async_session() as session:
        session.add(feed)
        await session.commit()
    return True
