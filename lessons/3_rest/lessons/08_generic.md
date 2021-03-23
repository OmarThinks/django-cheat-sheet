# 8) Generic Views:


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














































# 2) Attributes:


- **`queryset`**
- **`serializer_class`**
- **`lookup_field`**
- **`pagination_class`**
- **`filter_backends`**
















































# 3) Methods:




- **`get_queryset(self)`**
For example:
<b>

```python
def get_queryset(self):
    user = self.request.user
    return user.accounts.all()
```
</b>



- **`get_object(self)`**

- **`filter_queryset(self, queryset)`**
- **`get_serializer_class(self)`**
- **`get_serializer_class(self)`**


      
- **`perform_create(self, serializer)`**
- **`perform_update(self, serializer)`**
- **`perform_destroy(self, instance)`**











































# 4) Creating Custom Mixins:



<b>



```python
class MultipleFieldLookupMixin:

    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj
```





```python
class BaseRetrieveView(MultipleFieldLookupMixin,
        generics.RetrieveAPIView):
    pass

class BaseRetrieveUpdateDestroyView(MultipleFieldLookupMixin,
        generics.RetrieveUpdateDestroyAPIView):
    pass
```


</b>
