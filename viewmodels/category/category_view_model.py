from typing import List

from fastapi import Request

from viewmodels.shared.viewmodel import ViewModelBase
from services.games_service import *


class CategoryViewModel(ViewModelBase):
    def __init__(self, category_id: str, request: Request):
        super().__init__(request)
        self.category_id = category_id
        self.category: Optional[Categories] = None

        self.categories: list[Any] = []
        self.gallery: list[Any] = []
        self.tags: list[Any] = []
        self.link_games: list[Any] = []
        self.publisher: Optional[Publishers] = None
        self.language: Optional[Languages] = None

    async def load(self):
        self.category = await get_categories_by_game_id(self.category_id)
        self.categories = await get_categories_by_game_id(self.game_id)
        self.gallery = await get_gallery_by_game_id(self.game_id)
        self.tags = await get_tags_by_game_id(self.game_id)
        self.link_games = await get_link_games_by_game_id(self.game_id)
        self.publisher = await get_publisher_by_game_id(self.game_id)
        self.language = await get_language_by_game_id(self.game_id)
