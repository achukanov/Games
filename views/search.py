import fastapi
from services.games_service import get_games_from_search, get_categories_by_game_id, get_tags_by_game_id, \
    get_comments_count_by_game_id
router = fastapi.APIRouter()


# TODO: Добавить защиту от инъекций
@router.get('/search')
async def search_games(q: str | None = None) -> fastapi.responses.JSONResponse:
    games = await get_games_from_search(q) #Выдает IteratorResult, даже если не найдено
    data = []
    response = {}
    for game in games:
        print('if games:')
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
    if response:
        return fastapi.responses.JSONResponse(response)
    else:
        return fastapi.responses.JSONResponse(status_code=404, content={'success': 'false'})

