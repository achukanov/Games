# import fastapi
# from fastapi import Request
# from viewmodels.category.category_view_model import CategoryViewModel
#
# # from typing import Optional
#
# router = fastapi.APIRouter()
#
#
# @router.get('/categories/{category_id}', include_in_schema=False)
# async def details(category_id: str, request: Request) -> fastapi.responses.JSONResponse:
#     vm = CategoryViewModel(category_id, request)
#     await vm.load()
#
#     if vm:
#         # TODO: узнать у Кости про title и description
#         seo = {
#             "title": "title",
#             "description": "description"
#         }
#
#         response_json = {
#             'success': 'true',
#             "nameCategory": vm.category.category_name,
#             "slugCategory": vm.category.slug,
#             "seo": seo,
#             "countPage": 50,
#             "page": 1,
#             "data": vm.data
#
#
#
#         return fastapi.responses.JSONResponse(response_json)
#     else:
#         return fastapi.responses.JSONResponse({'success': 'false'})
