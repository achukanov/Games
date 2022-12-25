import fastapi
from fastapi import Request, Query
from services.categories_service import *
from services.games_service import *
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


@router.get('/categories/{slug}', include_in_schema=False)
async def games_by_category(slug: str, page: str | None = 1):
    games, count = await get_games_and_count_page_by_category_slug_and_page(slug, page)
    category = await get_category_by_slug(slug)
    if games and category:
        data = []
        seo = {
            "title": "title",
            "description": "description"
        }
        for game in games:
            categories = await get_categories_by_game_id(str(game.id))
            tags = await get_tags_by_game_id(str(game.id))
            comments_count = await get_comments_count_by_game_id(str(game.id))
            games_list = {
                "id": game.id,
                "categories": categories,
                "title": game.title,
                "slug": game.slug,
                "image": game.url_image,
                "description": game.description,
                "tags": tags,
                "rating": game.rating,
                "comments": comments_count,
                "video": game.url_video
            }
            data.append(games_list)

        response = {
            'success': 'true',
            'nameCategory': category.category_name,
            'slugCategory': category.slug,
            'seo': seo,
            'countPage': count,
            'page': page,
            'data': data
        }

        return fastapi.responses.JSONResponse(response)
    else:
        return fastapi.responses.JSONResponse({'success': 'false'})
