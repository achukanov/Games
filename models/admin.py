from models.models import *
from sqladmin import Admin, ModelView


class UserAdmin(ModelView, model=User):
    can_create = False
    can_export = False
    can_edit = False
    name_plural = 'Профили'
    page_size_options = [5, 25, 50]
    column_list = [User.id,
                   User.name,
                   User.email,
                   User.created_date,
                   User.last_login,
                   User.url_profile_image,
                   User.is_active]
    column_searchable_list = [User.name, User.email]
    column_sortable_list = [User.name, User.created_date, User.last_login]
    column_default_sort = "created_date"


class CategoriesAdmin(ModelView, model=Categories):
    can_export = False
    name_plural = 'Категории'
    page_size_options = [5, 25, 50]
    column_list = [Categories.id,
                   Categories.category_name,
                   Categories.slug,
                   Categories.games]
    column_searchable_list = [Categories.category_name]
    column_sortable_list = [Categories.category_name,
                            Categories.id]
    column_default_sort = "category_name"


class TagsAdmin(ModelView, model=Tags):
    can_export = False
    name_plural = 'Тэги'
    page_size_options = [5, 25]
    column_list = [Tags.id,
                   Tags.tag_name,
                   Tags.games]
    column_searchable_list = [Tags.tag_name]
    column_sortable_list = [Tags.id,
                            Tags.tag_name]
    column_default_sort = "tag_name"


class GamesAdmin(ModelView, model=Games):
    can_export = False
    name_plural = 'Игры'
    page_size_options = [5, 25, 50]
    column_list = [Games.id,
                   Games.is_published,
                   Games.created_date,
                   Games.last_updated,
                   Games.title,
                   Games.slug,
                   Games.text,
                   Games.description,
                   Games.rating,
                   Games.language,
                   Games.size,
                   Games.url_download,
                   Games.url_torrent,
                   Games.url_video,
                   Games.is_videogame,
                   Games.categories,
                   Games.publisher,
                   Games.tags]
    column_searchable_list = [Games.title,
                              Games.id]
    column_sortable_list = [Games.is_published,
                            Games.created_date,
                            Games.last_updated]
    column_default_sort = "created_date"


class PublishersAdmin(ModelView, model=Publishers):
    can_export = False
    name_plural = 'Издатели'
    page_size_options = [5, 25]
    column_list = [Publishers.id,
                   Publishers.publisher_name,
                   Publishers.is_published,
                   Publishers.url_publisher_homepage]
    column_searchable_list = [Publishers.publisher_name]
    column_sortable_list = [Publishers.id,
                            Publishers.publisher_name]
    column_default_sort = "publisher_name"


class GalleryAdmin(ModelView, model=Gallery):
    can_export = False
    name_plural = 'Галерея'
    page_size_options = [5, 25]
    column_list = [Gallery.id,
                   Gallery.game_id,
                   Gallery.game,
                   Gallery.url_image]
    column_searchable_list = [Gallery.game]

    '''Выдет ошибку при column_sortable_list и column_default_sort'''
    # column_sortable_list = [Gallery.game_id,
    #                         Gallery.game]
    # column_default_sort = "game"


class SimilarGamesAdmin(ModelView, model=SimilarGames):
    can_export = False
    name_plural = 'Похожие игры'
    page_size_options = [5, 25]
    column_list = [SimilarGames.id,
                   SimilarGames.game_id,
                   SimilarGames.game,
                   SimilarGames.url_similar_game]
    column_searchable_list = [SimilarGames.game]
    # column_sortable_list = [SimilarGames.game_id,
    #                         SimilarGames.game]
    # column_default_sort = "game"


class LanguagesAdmin(ModelView, model=Languages):
    can_export = False
    name_plural = 'Языки'
    page_size_options = [5, 25]
    column_list = [Languages.id,
                   Languages.language]


def create_admin(app, engine):
    admin = Admin(app, engine)
    admin.add_view(UserAdmin)
    admin.add_view(GamesAdmin)
    admin.add_view(CategoriesAdmin)
    admin.add_view(TagsAdmin)
    admin.add_view(PublishersAdmin)
    admin.add_view(GalleryAdmin)
    admin.add_view(SimilarGamesAdmin)
    admin.add_view(LanguagesAdmin)
