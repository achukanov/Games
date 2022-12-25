import fastapi
from fastapi import Request
from services.users_service import *

router = fastapi.APIRouter()


@router.post('/news', include_in_schema=False)
async def subscribe(request: Request):
    form = await request.form()
    email = form.get('email')
    account = await subscribe(email)
    if account:
        return fastapi.responses.JSONResponse({'success': 'true'})
    else:
        return fastapi.responses.JSONResponse({'success': 'false'})



@router.post('/feedback', include_in_schema=False)
async def feedback(request: Request):
    form = await request.form()
    first_name = form.get('firstName')
    email = form.get('email')
    email = form.get('email')
    email = form.get('email')
    account = await subscribe(email)
    if account:
        return fastapi.responses.JSONResponse({'success': 'true'})
    else:
        return fastapi.responses.JSONResponse({'success': 'false'})