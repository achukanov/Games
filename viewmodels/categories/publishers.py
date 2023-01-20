from services.categories_service import get_all_publishers
from services.seo_service import get_seo
from viewmodels.basemodel import ViewModelBase


class PublishersViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.categories = None
        self.seo = []

    async def load(self):
        self.publishers = await get_all_publishers()
        self.seo = await get_seo('publishers')

    async def construct(self):
        await self.load()
        seo = {
            "title": self.seo.title,
            "description": self.seo.description
        }
        data = []
        for publisher in self.publishers:
            categories_list = {
                "id": publisher.id,
                "category": publisher.publisher_name,
                "slug": publisher.slug
            }
            data.append(categories_list)
        resp = {'success': 'true', 'seo': seo, 'data': data}
        return resp
