from pathlib import Path

import fastapi
import uvicorn
# from starlette.staticfiles import StaticFiles

from models import db_session
# from views import account
# from views import home
# from views import packages

app = fastapi.FastAPI()  # docs_url=None, redoc_url=None)


def main():
    configure(dev_mode=True)
    # noinspection PyTypeChecker
    uvicorn.run(app, host='127.0.0.1', port=8000)


def configure(dev_mode: bool):
    # configure_templates(dev_mode)
    # configure_routes()
    configure_db(dev_mode)


def configure_db(dev_mode: bool):
    file = (Path(__file__).parent / 'db' / 'small_games_db.sqlite').absolute()
    db_session.global_init(file.as_posix())


# def configure_templates(dev_mode: bool):
#     fastapi_chameleon.global_init('templates', auto_reload=dev_mode)


# def configure_routes():
#     app.mount('/static', StaticFiles(directory='static'), name='static')
#     app.include_router(home.router)
#     app.include_router(account.router)
#     app.include_router(packages.router)


if __name__ == '__main__':
    main()
else:
    configure(dev_mode=False)
