import fastapi
from fastapi import Request
from viewmodels.game.game_view_model import GameViewModel
# from typing import Optional

router = fastapi.APIRouter()


@router.get('/games/{game_id}', include_in_schema=False)
async def details(game_id: str, request: Request) -> fastapi.responses.JSONResponse:
    vm = GameViewModel(game_id, request)
    await vm.load()
    game = vm.game
    gallery = vm.gallery
    categories = vm.categories
    tags = vm.tags
    link_games = vm.link_games
    publisher = vm.publisher
    # print('gallery------', gallery)
    resp = {}

    if vm:
        seo = {
            "title": game.title,
            "description": game.description
        }
        og = {
            "title": game.title,
            "type": "article",
            "video": game.url_video,
            "url": 'https://small-game.com/games/' + game_id,
            # "image": game.url_image
        },
        data = {'seo': seo,
                'og': og,
                "videoGame": game.is_videogame,
                "categories": categories,
                "title": game.title,
                "slug": game.slug,
                # "image": game.url_image,
                "text": game.text,
                "gallery": gallery,
                "tags": tags,
                "rating": game.rating,
                "namePublisher": publisher.publisher_name,
                # "lang": game.language,
                "size": str(game.size) + ' Mb',
                "urlPublisher": "gregarious-loophole.net",
                "urlDownload": game.url_download,
                "urlTorrent": game.url_torrent,
                "video": game.url_video,
                "linkGames": link_games
                }
        resp = {'success': 'true', 'data': data}

    return fastapi.responses.JSONResponse(resp)
