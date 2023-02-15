from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ListCategoriesView.as_view(), name='ListCategories'),
]