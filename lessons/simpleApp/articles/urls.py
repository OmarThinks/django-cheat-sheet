from django.urls import path
from .views import (articles_list_page, article_page)

urlpatterns = [
    path('', articles_list_page),
    path('<int:id>', article_page),
]
