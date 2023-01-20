from services.games_service import get_game_by_slug, get_categories_by_game_id, get_gallery_by_game_id, \
    get_link_games_by_game_id, get_publisher_by_game_id, get_language_by_game_id
from services.seo_service import get_seo
from viewmodels.basemodel import ViewModelBase


class GameViewModel(ViewModelBase):
    def __init__(self, slug: str):
        super().__init__()
        self.slug = slug
        self.game = None
        self.id = str
        self.categories = None
        self.seo = None
        self.gallery = None
        self.link_games = None
        self.publisher = None
        self.language = None

    async def load(self):
        self.game = await get_game_by_slug(self.slug)
        self.id = str(self.game.id)
        self.categories = await get_categories_by_game_id(str(self.id))
        self.gallery = await get_gallery_by_game_id(self.id)
        self.link_games = await get_link_games_by_game_id(self.id)
        self.publisher = await get_publisher_by_game_id(self.id)
        self.language = await get_language_by_game_id(self.id)
        self.seo = await get_seo('games_slug')

    async def construct(self):
        await self.load()
        if self.game.is_videogame:
            type = 'video'
            video = self.game.url_video
        else:
            type = 'article'
            video = None

        seo = {
            "title": self.seo.title,
            "description": self.seo.description
        }
        og = {
            "title": self.game.title,
            "type": type,
            "video": video,
            "url": 'https://small-game.com/games/' + str(self.id),
            "image": self.game.url_image
        },
        data = {'seo': seo,
                'og': og,
                "videoGame": 'false' if self.game.is_videogame else 'true',
                "categories": self.categories,
                "title": self.game.title,
                "slug": self.game.slug,
                "image": self.game.url_image,
                "text": self.game.text,
                "gallery": self.gallery,
                "tags": self.categories,
                "rating": self.game.rating,
                "namePublisher": self.publisher.publisher_name,
                "lang": self.language.language,
                "size": str(self.game.size) + ' Mb',
                "urlPublisher": "gregarious-loophole.net",
                "urlDownload": self.game.url_download,
                "urlTorrent": self.game.url_torrent,
                "video": self.game.url_video,
                "linkGames": self.link_games
                }
        resp = {'success': 'true', 'data': data}
        return resp
