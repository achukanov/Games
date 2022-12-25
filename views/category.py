import fastapi
from fastapi import Request
from services.categories_service import *

from typing import Optional

router = fastapi.APIRouter()


# TODO: уточнить роут группировок и SEO
@router.get('/group/categories', include_in_schema=False)
async def categories_group(request: Request) -> fastapi.responses.JSONResponse:
    categories = await get_all_categories()

    if categories:
        data = []
        seo = {
            "title": "title",
            "description": "description"
        }
        for category in categories:
            categories_list = {
                "id": category.id,
                "category": category.category_name,
                "slug": category.slug
            }
            data.append(categories_list)

        response = {
            'success': 'true',
            'seo': seo,
            'data': data
        }

        return fastapi.responses.JSONResponse(response)
    else:
        return fastapi.responses.JSONResponse({'success': 'false'})
