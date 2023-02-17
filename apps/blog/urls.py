from django.urls import path
from .views import BlogListView, ListPostsByCategoryView

urlpatterns = [
    path('list/', BlogListView.as_view(), name='BlogList'),
    path('list/by_category', ListPostsByCategoryView.as_view(), name='ListPostsBy'),
]
