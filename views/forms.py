import fastapi
from fastapi import Request
from services.users_service import subscribe, feedback

router = fastapi.APIRouter()


# TODO: Добавить проверку инъекций
@router.post('/news')
async def sub(request: Request):
    form = await request.form()
    email = form.get('email')
    account = await subscribe(email)
    if account and form:
        return fastapi.responses.JSONResponse({'success': 'true'})
    else:
        return fastapi.responses.JSONResponse({'success': 'false'})


@router.post('/feedback')
async def feed(request: Request):
    form = await request.form()
    first_name = form.get('firstName')
    email = form.get('email')
    title = form.get('title')
    message = form.get('massage')
    account = await feedback(first_name, email, title, message)
    if account and form:
        return fastapi.responses.JSONResponse({'success': 'true'})
    else:
        return fastapi.responses.JSONResponse({'success': 'false'})
