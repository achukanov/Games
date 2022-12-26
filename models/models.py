import datetime
from models.modelbase import SqlAlchemyBase
import sqlalchemy as db
from sqlalchemy.orm import relationship
from sqlalchemy import event
from slugify import slugify

# metadata = db.MetaData()

GamesTags = db.Table('games_tags',
                     SqlAlchemyBase.metadata,
                     db.Column('id', db.Integer, primary_key=True, index=True),
                     db.Column('game_id', db.Integer, db.ForeignKey('games.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')))

GamesCategories = db.Table('games_categories',
                           SqlAlchemyBase.metadata,
                           db.Column('id', db.Integer, primary_key=True, index=True),
                           db.Column('game_id', db.Integer, db.ForeignKey('games.id')),
                           db.Column('category_id', db.Integer, db.ForeignKey('categories.id')))


# class GamesTags(SqlAlchemyBase):
#     __tablename__ = 'games_tags',
#     id: int = db.Column(db.Integer, primary_key=True)
#     game_id: int = db.Column(db.Integer, db.ForeignKey("games.id")),
#     tag_id: int = db.Column(db.Integer, db.ForeignKey("tags.id"))
#
#
# class GamesCategories(SqlAlchemyBase):
#     __tablename__ = 'games_categories',
#     id: int = db.Column(db.Integer, primary_key=True)
#     game_id: int = db.Column(db.Integer, db.ForeignKey("games.id")),
#     category_id: int = db.Column(db.Integer, db.ForeignKey("categories.id"))


class Games(SqlAlchemyBase):
    __tablename__ = 'games'
    id: int = db.Column(db.Integer, primary_key=True)
    is_published: bool = db.Column(db.Boolean, default=True, index=True)
    created_date: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    last_updated: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    title: str = db.Column(db.String(50), nullable=False, unique=True)
    slug: str = db.Column(db.String(50), unique=True)
    text: str = db.Column(db.String, nullable=True)
    description: str = db.Column(db.String(100))
    rating: int = db.Column(db.SmallInteger, default=0)
    size: int = db.Column(db.Float)
    url_download: str = db.Column(db.String(100))
    url_torrent: str = db.Column(db.String(100))
    url_video: str = db.Column(db.String(100))
    url_image: str = db.Column(db.String(100))
    is_videogame: bool = db.Column(db.Boolean, index=True)
    categories = relationship("Categories", secondary="games_categories", back_populates='games')
    tags = relationship("Tags", secondary="games_tags", back_populates='games')
    publisher_id: int = db.Column(db.Integer, db.ForeignKey("publishers.id"))
    publisher = relationship('Publishers')
    language_id: int = db.Column(db.Integer, db.ForeignKey("languages.id"))
    language = relationship('Languages')
    # gallary = relationship('Gallery', cascade="all, delete, delete-orphan")
    comments = relationship('Comments', cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.title

    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)


event.listen(Games.title, 'set', Games.generate_slug, retval=False)


class Categories(SqlAlchemyBase):
    __tablename__ = 'categories'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name: str = db.Column(db.String(140))
    slug: str = db.Column(db.String(140))
    games = relationship("Games", secondary="games_categories", back_populates='categories')

    def __repr__(self):
        return self.category_name


class Tags(SqlAlchemyBase):
    __tablename__ = 'tags'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_name: str = db.Column(db.String(20), nullable=False, unique=True)
    games = relationship("Games", secondary="games_tags", back_populates='tags')

    def __repr__(self):
        return self.tag_name


class Publishers(SqlAlchemyBase):
    __tablename__ = 'publishers'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    publisher_name: str = db.Column(db.String(20), nullable=False, unique=True)
    is_published: bool = db.Column(db.Boolean, default=True, index=True)
    url_publisher_homepage: str = db.Column(db.String(50))

    def __repr__(self):
        return self.publisher_name


class Languages(SqlAlchemyBase):
    __tablename__ = 'languages'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    language: str = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return self.language


class Gallery(SqlAlchemyBase):
    __tablename__ = 'media'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id: int = db.Column(db.Integer, db.ForeignKey("games.id"))
    game = relationship('Games')
    url_image = db.Column(db.String())


class SimilarGames(SqlAlchemyBase):
    __tablename__ = 'similar_games'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id: int = db.Column(db.Integer, db.ForeignKey("games.id"))
    game = relationship('Games')
    url_similar_game: str = db.Column(db.String(50))


class Users(SqlAlchemyBase):
    __tablename__ = 'users'

    # metadata = db.MetaData()
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, doc='Имя')
    email: str = db.Column(db.String, index=True, unique=True, doc='e-mail')
    hash_password: str = db.Column(db.String)
    created_date: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True,
                                                doc='Дата регистрации')
    last_login: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True,
                                              doc='Последний вход')
    url_profile_image: str = db.Column(db.String, doc='e-mail')
    is_active: bool = db.Column(db.Boolean, default=True, doc='Активен')
    comments = relationship('Comments', cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.name


class Comments(SqlAlchemyBase):
    __tablename__ = 'comments'

    id: int = db.Column(db.Integer, primary_key=True)
    content: str = db.Column(db.String, nullable=False)
    created_date: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    last_updated: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    is_published: bool = db.Column(db.Boolean, default=True, index=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"))
    game_id: int = db.Column(db.Integer, db.ForeignKey("games.id"))

    def __repr__(self):
        return self.content


class Subscribers(SqlAlchemyBase):
    __tablename__ = 'subscribers'

    id: int = db.Column(db.Integer, primary_key=True)
    created_date: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    last_updated: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    email: str = db.Column(db.String, index=True, unique=True)
    is_subscribe: bool = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return self.email


class Feedback(SqlAlchemyBase):
    __tablename__ = 'feedback'

    id: int = db.Column(db.Integer, primary_key=True)
    created_date: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    first_name: str = db.Column(db.String)
    email: str = db.Column(db.String)
    title: str = db.Column(db.String)
    message: str = db.Column(db.String)
