# 7) Validators:


# 1) Example:


<b>

`views.py`

```python
class ProductSerializer_3(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


from rest_framework import generics
from .models import Product

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer_3
    permission_classes = []

    """
    def perform_create(self, serializer):
        ...
    def get_queryset(self):
        ...
    """


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer_3
    permission_classes = []
    lookup_field = "id"

    """
    def get_queryset(self):
        ...
    """
```


`urls.py`

```python
from .views import (ProductList, ProductDetails)
from django.urls import (path)

urlpatterns = [
    ...,
    path('', ProductList.as_view()),
    path('<int:id>', ProductDetails.as_view()),
]
```


</b>



































