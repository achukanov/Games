import fastapi
from fastapi import Request
from viewmodels.game.game_view_model import GameViewModel

router = fastapi.APIRouter()


@router.get('/games/{game_id}', include_in_schema=False)
async def details(game_id: str, request: Request):
    vm = GameViewModel(game_id, request)
    await vm.load()

    return fastapi.responses.JSONResponse(vm.to_dict())
