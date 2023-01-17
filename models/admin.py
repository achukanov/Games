from models.models import *
from sqladmin import Admin, ModelView

''' icon = https://fontawesome.com/'''

""" Заполнить в админке таблицу SEO """
""" categories, publishers, categories_slug, games_slug """
class UsersAdmin(ModelView, model=Users):
    can_create = False
    can_export = False
    can_edit = False
    name = 'Профиль'
    name_plural = 'Профили'
    icon = "fa-solid fa-user"
    page_size_options = [5, 25, 50]
    column_list = [Users.id,
                   Users.name,
                   Users.email,
                   Users.created_date,
                   Users.last_login,
                   Users.url_profile_image,
                   Users.is_active]
    column_searchable_list = [Users.name, Users.email]
    column_sortable_list = [Users.name, Users.created_date, Users.last_login]
    column_default_sort = "created_date"


class CategoriesAdmin(ModelView, model=Categories):
    can_export = False
    name_plural = 'Категории'
    icon = "fa-solid fa-bars"
    page_size_options = [5, 25, 50]
    column_list = [Categories.id,
                   Categories.category_name,
                   Categories.slug,
                   Categories.games]
    column_searchable_list = [Categories.category_name]
    column_sortable_list = [Categories.category_name,
                            Categories.id]
    column_default_sort = "category_name"


# class TagsAdmin(ModelView, model=Tags):
#     can_export = False
#     name_plural = 'Тэги'
#     icon = "fa-solid fa-hashtag"
#     page_size_options = [5, 25]
#     column_list = [Tags.id,
#                    Tags.tag_name,
#                    Tags.games]
#     column_searchable_list = [Tags.tag_name]
#     column_sortable_list = [Tags.id,
#                             Tags.tag_name]
#     column_default_sort = "tag_name"


class GamesAdmin(ModelView, model=Games):
    can_export = False
    name_plural = 'Игры'
    icon = "fa-solid fa-gamepad"
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
                   # Games.tags,
                   ]
    column_searchable_list = [Games.title,
                              Games.id]
    column_sortable_list = [Games.is_published,
                            Games.created_date,
                            Games.last_updated]
    column_default_sort = "created_date"


class PublishersAdmin(ModelView, model=Publishers):
    can_export = False
    name_plural = 'Издатели'
    icon = "fa-solid fa-pen"
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
    icon = "fa-solid fa-image"
    page_size_options = [5, 25]
    column_list = [Gallery.id,
                   Gallery.game_id,
                   Gallery.url_image]
    column_searchable_list = [Gallery.game_id]

    '''Выдет ошибку при column_sortable_list и column_default_sort'''
    # column_sortable_list = [Gallery.game_id,
    #                         Gallery.game]
    # column_default_sort = "game"


class SimilarGamesAdmin(ModelView, model=SimilarGames):
    can_export = False
    name_plural = 'Похожие игры'
    icon = "fa-solid fa-thumbs-up"
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
    icon = "fa-solid fa-language"
    page_size_options = [5, 25]
    column_list = [Languages.id,
                   Languages.language]


class CommentsAdmin(ModelView, model=Comments):
    can_export = False
    name_plural = 'Комментарии'
    icon = "fa-solid fa-comments"
    page_size_options = [5, 25]
    column_list = [Comments.id,
                   Comments.content]


class FeedbackAdmin(ModelView, model=Feedback):
    can_export = False
    name_plural = 'Обратная связь'
    icon = "fa-solid fa-comment-dots"
    page_size_options = [5, 25]
    column_list = [Feedback.id,
                   Feedback.created_date,
                   Feedback.first_name,
                   Feedback.email,
                   Feedback.title,
                   Feedback.message]
    column_default_sort = "created_date"


class SEOAdmin(ModelView, model=Seo):
    can_export = False
    name_plural = 'Описание страницы'
    icon = "fa-solid fa-tag"
    page_size_options = [5, 25]
    column_list = [Seo.id,
                   Seo.last_updated,
                   Seo.page,
                   Seo.title,
                   Seo.description]
    column_default_sort = "page"


class SubscribersAdmin(ModelView, model=Subscribers):
    can_export = False
    name_plural = 'Подписки'
    icon = "fa-solid fa-at"
    page_size_options = [5, 25]
    column_list = [Subscribers.id,
                   Subscribers.created_date,
                   Subscribers.last_updated,
                   Subscribers.email,
                   Subscribers.is_subscribe]
    column_default_sort = "created_date"


def create_admin(app, engine):
    admin = Admin(app, engine)
    admin.add_view(UsersAdmin)
    admin.add_view(GamesAdmin)
    admin.add_view(CategoriesAdmin)
    # admin.add_view(TagsAdmin)
    admin.add_view(PublishersAdmin)
    admin.add_view(GalleryAdmin)
    admin.add_view(SimilarGamesAdmin)
    admin.add_view(LanguagesAdmin)
    admin.add_view(CommentsAdmin)
    admin.add_view(FeedbackAdmin)
    admin.add_view(SEOAdmin)
    admin.add_view(SubscribersAdmin)
