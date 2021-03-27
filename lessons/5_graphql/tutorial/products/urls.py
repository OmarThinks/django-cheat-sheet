from .views import (
	ProductList_REST, ProductDetails_REST,
	Product_GraphQL)
from django.urls import (path)

"""

"""

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('graphql/products/query', Product_GraphQL)
urlpatterns= router.urls



urlpatterns.extend([
	path('rest/products/', ProductList_REST.as_view()),
	path('rest/products/<int:id>', 
		ProductDetails_REST.as_view())
])

