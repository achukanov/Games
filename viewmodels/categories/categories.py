from services.categories_service import get_all_categories
from services.seo_service import get_seo
from viewmodels.basemodel import ViewModelBase


class CategoriesViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.categories = None
        self.seo = []

    async def load(self):
        self.categories = await get_all_categories()
        self.seo = await get_seo('categories')

    async def construct(self):
        await self.load()
        seo = {
            "title": self.seo.title,
            "description": self.seo.description
        }
        data = []
        for category in self.categories:
            categories_list = {
                "id": category.id,
                "category": category.category_name,
                "slug": category.slug
            }
            data.append(categories_list)
        resp = {'success': 'true', 'seo': seo, 'data': data}
        return resp
