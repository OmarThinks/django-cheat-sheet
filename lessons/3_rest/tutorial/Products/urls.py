from .views import (h1, h2, HelloViewSet)
from django.urls import (path)

urlpatterns = [
    path('h1', h1),
    path('h2', h2)
]
