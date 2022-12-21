import fastapi
from fastapi import Request
from services.games_service import get_top_games
from viewmodels.game.game_view_model import GameViewModel


# from typing import Optional

router = fastapi.APIRouter()

# TODO: переделать роуты под слаги
@router.get('/top', include_in_schema=False)
async def top_games() -> fastapi.responses.JSONResponse:
    games = await get_top_games()
    data = []

    if games:
        for game in games:
            game_list = {
                "id": game.id,
                "title": game.title,
                "slug": game.slug,
                "image": game.url_image
            }
            data.append(game_list)

        response = {
            'success': 'true',
            'data': data
        }

        return fastapi.responses.JSONResponse(response)
    else:
        return fastapi.responses.JSONResponse({'success': 'false'})


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
    language = vm.language

    if vm:
        success = 'true'
        seo = {
            "title": game.title,
            "description": game.description
        }
        og = {
            "title": game.title,
            "type": "article",
            "video": game.url_video,
            "url": 'https://small-game.com/games/' + game_id,
            "image": game.url_image
        },
        data = {'seo': seo,
                'og': og,
                "videoGame": game.is_videogame,
                "categories": categories,
                "title": game.title,
                "slug": game.slug,
                "image": game.url_image,
                "text": game.text,
                "gallery": gallery,
                "tags": tags,
                "rating": game.rating,
                "namePublisher": publisher.publisher_name,
                "lang": language.language,
                "size": str(game.size) + ' Mb',
                "urlPublisher": "gregarious-loophole.net",
                "urlDownload": game.url_download,
                "urlTorrent": game.url_torrent,
                "video": game.url_video,
                "linkGames": link_games
                }
        resp = {'success': success, 'data': data}
        return fastapi.responses.JSONResponse(resp)
    else:
        return fastapi.responses.JSONResponse({'success': 'false'})
