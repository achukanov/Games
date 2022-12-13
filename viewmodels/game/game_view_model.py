from typing import List

from fastapi import Request

from viewmodels.shared.viewmodel import ViewModelBase
from services.games_service import *


class GameViewModel(ViewModelBase):
    def __init__(self, game_id: str, request: Request):
        super().__init__(request)
        self.game_id = game_id
        self.video_game = None
        self.title = None
        # self.tags = []
        # self.gallery = []
        self.categories = []

    async def load(self):
        self.video_game: bool = await is_videogame()
        self.title: str = await get_title()
        self.categories: List = await get_categories_by_game(self.game_id)
        # self.user_count: int = await user_service.user_count()
        # self.package_count: int = await package_service.package_count()
        # self.packages = await package_service.latest_packages(limit=7)
