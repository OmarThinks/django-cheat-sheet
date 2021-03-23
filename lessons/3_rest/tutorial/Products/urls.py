from .views import (h1, h2, s_a1, s_a2, s_a3, 
	ProductList, ProductDetails)
from django.urls import (path)

urlpatterns = [
	path('h1', h1),
	path('h2', h2),


	path('s_a1', s_a1),
	path('s_a2', s_a2),
	path('s_a3', s_a3),



	#path('s_b1', s_b1),
	path('', ProductList.as_view()),
	path('<int:id>', ProductDetails.as_view()),
]
