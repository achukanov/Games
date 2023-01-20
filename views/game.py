import fastapi
from services.games_service import *
from services.seo_service import get_seo
from viewmodels.games.game import GameViewModel
from fastapi.requests import Request

router = fastapi.APIRouter()


@router.get('/games/pages')
async def games_pages() -> fastapi.responses.JSONResponse:
    slugs = await get_all_game_slugs()
    if slugs:
        success = 'true',
        data = []
        for slug in slugs:
            slugs_list = {
                "slug": slug
            }
            data.append(slugs_list)
        resp = {'success': success, 'data': data}
        return fastapi.responses.JSONResponse(resp)
    else:
        return fastapi.responses.JSONResponse(status_code=404, content={'success': 'false'})


@router.get('/games/new')
async def new_games() -> fastapi.responses.JSONResponse:
    games = await get_new_games()
    data = []

    if games:
        for game in games:
            categories = await get_categories_by_game_id(str(game.id))
            # tags = await get_tags_by_game_id(str(game.id))
            comments_count = await get_comments_count_by_game_id(str(game.id))
            game_list = {
                "id": game.id,
                "categories": categories,
                "videoGame": 'true' if game.is_videogame else 'false',
                "title": game.title,
                "slug": game.slug,
                "image": game.url_image,
                # "tags": categories,
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
        return fastapi.responses.JSONResponse(status_code=404, content={'success': 'false'})


@router.get('/games/top')
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
        return fastapi.responses.JSONResponse(status_code=404, content={'success': 'false'})


# @router.get('/games/{slug}')
# async def games_slug(slug: str) -> fastapi.responses.JSONResponse:
#     game = await get_game_by_slug(slug)
#     id = str(game.id)
#     categories = await get_categories_by_game_id(str(id))
#     gallery = await get_gallery_by_game_id(id)
#     # tags = await get_tags_by_game_id(id)
#     link_games = await get_link_games_by_game_id(id)
#     publisher = await get_publisher_by_game_id(id)
#     language = await get_language_by_game_id(id)
#     seo = await get_seo('games_slug')
#     if game:
#         success = 'true'
#         seo = {
#             "title": seo.title,
#             "description": seo.description
#         }
#         og = {
#             "title": game.title,
#             "type": "article",
#             "video": game.url_video,
#             "url": 'https://small-game.com/games/' + id,
#             "image": game.url_image
#         },
#         data = {'seo': seo,
#                 'og': og,
#                 "videoGame": 'true' if game.is_videogame else 'false',
#                 "categories": categories,
#                 "title": game.title,
#                 "slug": game.slug,
#                 "image": game.url_image,
#                 "text": game.text,
#                 "gallery": gallery,
#                 # "tags": categories,
#                 "rating": game.rating,
#                 "namePublisher": publisher.publisher_name,
#                 "lang": language.language,
#                 "size": str(game.size) + ' Mb',
#                 "urlPublisher": "gregarious-loophole.net",
#                 "urlDownload": game.url_download,
#                 "urlTorrent": game.url_torrent,
#                 "video": game.url_video,
#                 "linkGames": link_games
#                 }
#         resp = {'success': success, 'data': data}
#         return fastapi.responses.JSONResponse(resp)
#     else:
#         return fastapi.responses.JSONResponse(status_code=404, content={'success': 'false'})


@router.get('/games/{slug}')
async def games_slug(slug: str, request: Request) -> fastapi.responses.JSONResponse:
    vm = GameViewModel(slug)
    content = await vm.construct()
    if not content:
        content = {'success': 'false'}
    return fastapi.responses.JSONResponse(content=content)
