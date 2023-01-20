import fastapi
from fastapi import Request, Query
from services.categories_service import *
from services.games_service import *

from viewmodels.categories.categories import CategoriesViewModel
from viewmodels.categories.publishers import PublishersViewModel

router = fastapi.APIRouter()


@router.get('/categories')
async def categories_and_publishers(group: str | None = 'genres') -> fastapi.responses.JSONResponse:
    if group == 'genres':
        vm = CategoriesViewModel()
        content = await vm.construct()
    elif group == 'publishers':
        vm = PublishersViewModel()
        content = await vm.construct()
    else:
        content = {'success': 'false', 'data': 'null', 'message': 'Incorrect input after "?group=" in url'}
    if not content:
        content = {'success': 'false', 'data': 'null', 'message': 'Cant find content, server error'}
    return fastapi.responses.JSONResponse(content=content)


@router.get('/categories/pages')
async def categories_pages():
    data = await get_categories_pages()
    if data:
        response = {'success': 'true', 'data': data}
    else:
        response = {'success': 'false'}
    return fastapi.responses.JSONResponse(response)


@router.get('/categories/{slug}')
async def categories_slug(slug: str, page: str | None = None) -> fastapi.responses.JSONResponse:
    category = await get_category_by_slug(slug)
    games = await get_games_by_category_and_page(category, page)
    data = []
    seo = {
        "title": 'seo.title',
        "description": 'seo.description'
    }
    if games:
        for game in games:
            categories = await get_categories_by_game_id(str(game.id))
            comments_count = await get_comments_count_by_game_id(str(game.id))
            success = 'true'
            game_list = {
                'id': game.id,
                "categories": categories,
                "title": game.title,
                "slug": game.slug,
                "image": game.url_image,
                "description": game.description,
                "tags": categories,
                "rating": game.rating,
                "comments": comments_count,
                "video": game.url_video,
            }
            data.append(game_list)
        resp = {
            'success': 'true',
            'nameCategory': category.category_name,
            'slugCategory': category.slug,
            'seo': seo,
            'countPage': 17,
            'page': page if page else 1,
            'data': data
        }
        return fastapi.responses.JSONResponse(resp)
    else:
        return fastapi.responses.JSONResponse(status_code=404, content={'success': 'false'})
