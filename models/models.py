import datetime
# from typing import List

import sqlalchemy as db
import sqlalchemy.orm as orm
from sqlalchemy import event
import sqlalchemy.ext.declarative
from slugify import slugify
from models.modelbase import SqlAlchemyBase

# SqlAlchemyBase = sqlalchemy.ext.declarative.declarative_base()

# GamesTags = db.Table('games_tags',
#                      SqlAlchemyBase.metadata,
#                      db.Column('id', db.Integer, primary_key=True, index=True),
#                      db.Column('game_id', db.Integer, db.ForeignKey('games.id')),
#                      db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')))

class GamesTags(SqlAlchemyBase):
    __tablename__ = 'games_tags',
    id: int = db.Column(db.Integer, primary_key=True)
    game_id: int = db.Column(db.Integer, db.ForeignKey("games.id")),
    tag_id: int = db.Column(db.Integer, db.ForeignKey("tags.id"))


class GamesCategories(SqlAlchemyBase):
    __tablename__ = 'games_categories',
    id: int = db.Column(db.Integer, primary_key=True)
    game_id: int = db.Column(db.Integer, db.ForeignKey("games.id")),
    category_id: int = db.Column(db.Integer, db.ForeignKey("categories.id"))


class Games(SqlAlchemyBase):
    __tablename__ = 'games'

    id: int = db.Column(db.Integer, primary_key=True)
    is_published: bool = db.Column(db.Boolean, default=True, index=True)
    created_date: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    last_updated: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    """Title - заголовок объекта"""
    title: str = db.Column(db.String(50), nullable=False, unique=True)
    slug: str = db.Column(db.String(50), unique=True)
    """Description - описание объекта"""
    text: str = db.Column(db.String, nullable=True)
    description: str = db.Column(db.String(50))
    rating: int = db.Column(db.SmallInteger, default=0)
    language: str = db.Column(db.String(50), nullable=True)
    size: int = db.Column(db.Integer)
    url_download: str = db.Column(db.String(50))
    url_torrent: str = db.Column(db.String(50))
    url_video: str = db.Column(db.String(50))
    is_videogame: bool = db.Column(db.Boolean, index=True)

    '''Зависимости'''
    # category_id: int = db.Column(db.Integer, db.ForeignKey("categories.id"))
    # category = orm.relationship('Categories')

    # tag_id: int = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("tags.id"))
    # tag = orm.relationship('Tags')

    publisher_id: int = db.Column(db.Integer, db.ForeignKey("publishers.id"))
    publisher = orm.relationship('Publishers')

    # '''https://ploshadka.net/sqlalchemy-many-to-many/'''
    # tags = orm.relationship('Tags', secondary=GamesTags, backref='Games')

    '''https://michaelcho.me/article/using-model-callbacks-in-sqlalchemy-to-generate-slugs'''

    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)


event.listen(Games.title, 'set', Games.generate_slug, retval=False)


class Categories(SqlAlchemyBase):
    __tablename__ = 'categories'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name: str = db.Column(db.String(50), nullable=False, unique=True)
    slug: str = db.Column(db.String(50), unique=True)

    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)


event.listen(Categories.category_name, 'set', Categories.generate_slug, retval=False)



class Tags(SqlAlchemyBase):
    __tablename__ = 'tags'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_name: str = db.Column(db.String(20), nullable=False, unique=True)

    # games = orm.relationship('Games', secondary=GamesTags, backref=orm.backref('tags', lazy='dynamic'))


class Publishers(SqlAlchemyBase):
    __tablename__ = 'publishers'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    publisher_name: str = db.Column(db.String(20), nullable=False, unique=True)
    is_published: bool = db.Column(db.Boolean, default=True, index=True)
    url_publisher_homepage: str = db.Column(db.String(50))

    # category_id: int = db.Column(db.Integer, db.ForeignKey("categories.id"))
    # category = orm.relationship('Categories')


class Gallery(SqlAlchemyBase):
    __tablename__ = 'media'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)

    game_id: int = db.Column(db.Integer, db.ForeignKey("games.id"))
    game = orm.relationship('Games')

    url_image = db.Column(db.String(50))


class SimilarGames(SqlAlchemyBase):
    __tablename__ = 'similar_games'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)

    game_id: int = db.Column(db.Integer, db.ForeignKey("games.id"))
    game = orm.relationship('Games')

    url_similar_game: str = db.Column(db.String(50))


class Comments(SqlAlchemyBase):
    __tablename__ = 'comments'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)

    game_id: int = db.Column(db.Integer, db.ForeignKey("games.id"))
    game = orm.relationship('Games')

    content: str = db.Column(db.String, nullable=False)
    created_date: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    last_updated: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    is_published: bool = db.Column(db.Boolean, default=True, index=True)


class Users(SqlAlchemyBase):
    __tablename__ = 'users'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String)
    email: str = db.Column(db.String, index=True, unique=True)
    hash_password: str = db.Column(db.String)
    created_date: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    last_login: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
    url_profile_image: str = db.Column(db.String)
    is_active: bool = db.Column(db.Boolean, default=True)
