from django.urls import path
from .views import (articles_list_page)

urlpatterns = [
    path('', articles_list_page),
]
