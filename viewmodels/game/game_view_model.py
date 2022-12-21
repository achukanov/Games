from typing import List

from fastapi import Request

from viewmodels.shared.viewmodel import ViewModelBase
from services.games_service import *


class GameViewModel(ViewModelBase):
    def __init__(self, game_id: str, request: Request):
        super().__init__(request)
        self.game_id = game_id
        self.game: Optional[Games] = None
        self.categories: list[Any] = []
        self.gallery: list[Any] = []
        self.tags: list[Any] = []
        self.link_games: list[Any] = []
        self.publisher: Optional[Publishers] = None
        self.language: Optional[Languages] = None

    async def load(self):
        self.game = await get_game_by_id(self.game_id)
        self.categories = await get_categories_by_game_id(self.game_id)
        self.gallery = await get_gallery_by_game_id(self.game_id)
        self.tags = await get_tags_by_game_id(self.game_id)
        self.link_games = await get_link_games_by_game_id(self.game_id)
        self.publisher = await get_publisher_by_game_id(self.game_id)
        self.language = await get_language_by_game_id(self.game_id)
