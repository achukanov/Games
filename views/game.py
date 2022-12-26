import fastapi
from fastapi import Request

from models.models import Games
from services.games_service import *
from services.seo_service import get_seo
from viewmodels.game.game_view_model import GameViewModel
from infrastructure.word_cases import word_cases

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


@router.get('/new', include_in_schema=False)
async def new_games() -> fastapi.responses.JSONResponse:
    games = await get_new_games()
    data = []

    if games:
        for game in games:
            categories = await get_categories_by_game_id(str(game.id))
            tags = await get_tags_by_game_id(str(game.id))
            comments_count = await get_comments_count_by_game_id(str(game.id))
            game_list = {
                "id": game.id,
                "categories": categories,
                "videoGame": 'true' if game.is_videogame else 'false',
                "title": game.title,
                "slug": game.slug,
                "image": game.url_image,
                "tags": tags,
                "rating": game.rating,
                "comments": comments_count
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
    seo = await get_seo('games_slug')
    if vm:
        success = 'true'
        seo = {
            "title": seo.title,
            "description": seo.description
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
                "videoGame": 'true' if game.is_videogame else 'false',
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


# TODO: Добавить проверку инъекций
@router.get('/search', include_in_schema=False)
async def search_games(q: str | None = None) -> fastapi.responses.JSONResponse:
    games = await get_games_from_search(q)
    data = []

    if games:
        for game in games:
            game_id = game.id
            categories = await get_categories_by_game_id(str(game_id))
            tags = await get_tags_by_game_id(str(game.id))
            comments_count = await get_comments_count_by_game_id(str(game.id))
            game_list = {
                "id": game.id,
                "categories": categories,
                "title": game.title,
                "slug": game.slug,
                "image": game.url_image,
                "tags": tags,
                "rating": game.rating,
                "comments": comments_count,
                "video": game.url_video
            }
            data.append(game_list)

        response = {
            'success': 'true',
            'data': data
        }

        return fastapi.responses.JSONResponse(response)
    else:
        return fastapi.responses.JSONResponse({'success': 'false'})
