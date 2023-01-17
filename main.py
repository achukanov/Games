from pathlib import Path
import fastapi
import uvicorn
from models import db_session
from views.game import router as game_router
from views.search import router as search_router
from views.category import router as category_router
from views.forms import router as form_router
from fastapi.staticfiles import StaticFiles

app = fastapi.FastAPI()  # (docs_url=None, redoc_url=None)

# TODO: множественное добавление гелереи в админке
# TODO: парсер старого сайта
# TODO: автозаполнение нового
# TODO: автослаг для полей
# TODO: тестирование
# TODO: логирование
# TODO: кеширование
# TODO: авторизация



def main():
    configure(dev_mode=True)
    # noinspection PyTypeChecker
    uvicorn.run(app, host='127.0.0.1', port=8000)


def configure(dev_mode: bool):
    configure_routes()
    configure_db(dev_mode)


def configure_db(dev_mode: bool):
    file = (Path(__file__).parent / 'db' / 'small_games_db.sqlite').absolute()
    db_session.global_init(file.as_posix(), app)


def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(game_router)
    app.include_router(category_router)
    app.include_router(form_router)
    app.include_router(search_router)


if __name__ == '__main__':
    main()
else:
    configure(dev_mode=False)
