from .views import (
	ProductList_REST, ProductDetails_REST,
	ProductViewSet, ProductViewSet2)
from django.urls import (path)

"""

"""

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('graphql/products/query', ProductViewSet)
router.register('graphql/products/mutate', ProductViewSet)
urlpatterns= router.urls



urlpatterns.extend([
	path('rest/products/', ProductList_REST.as_view()),
	path('rest/products/<int:id>', 
		ProductDetails_REST.as_view())
])

