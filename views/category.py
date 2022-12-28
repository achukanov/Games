import fastapi
from fastapi import Request, Query
from services.categories_service import *
from services.games_service import *
from services.seo_service import get_seo
from typing import Optional

router = fastapi.APIRouter()


# TODO: уточнить роут группировок и SEO
@router.get('/categories')
async def categories_and_publishers(group: str | None = 'genres') -> fastapi.responses.JSONResponse:
    seo = {}
    data = []
    if group == 'genres':
        categories = await get_all_categories()
        seo = await get_seo('categories')
        if categories:
            data = []
            for category in categories:
                categories_list = {
                    "id": category.id,
                    "category": category.category_name,
                    "slug": category.slug
                }
                data.append(categories_list)
        if seo:
            seo = {
                "title": seo.title,
                "description": seo.description
            }

    elif group == 'publishers':
        publishers = await get_all_publishers()
        seo = await get_seo('publishers')
        if publishers:
            data = []
            for publisher in publishers:
                publishers_list = {
                    "id": publisher.id,
                    "publisher": publisher.publisher_name,
                    "slug": publisher.slug
                }
                data.append(publishers_list)
        if seo:
            seo = {
                "title": seo.title,
                "description": seo.description
            }
    else:
        return fastapi.responses.JSONResponse({'success': 'false'})
    # if not seo:
    #     seo = 'false'
    response = {
        'success': 'true',
        'seo': seo,
        'data': data
    }
    return fastapi.responses.JSONResponse(response)


@router.get('/categories/pages')
async def categories_pages():
    data = await get_categories_pages()
    response = {
        'success': 'true',
        'data': data
    }
    return fastapi.responses.JSONResponse(response)
