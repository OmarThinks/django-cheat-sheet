# 1) django-restql


# 1) What:



This package enables you to use GrapQL with Django REST Framework 
Serializations.



# 2) Installing:

<b>

```bash
pip install django-restql
```
</b>

# 3) Example Code:


<b>



`products/models.py`
```python
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	name = models.CharField(max_length=100)
	in_stock = models.BooleanField(default=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, 
		null=False, blank=False, default=1)
```





`products/views.py`
```python
from .models import Product
from rest_framework import serializers
from django_restql.mixins import (DynamicFieldsMixin)

class ProductSerializer(DynamicFieldsMixin, 
	serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"

from rest_framework import viewsets

class Product_GraphQL(viewsets.ModelViewSet):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()
```





`products/urls.py`
```python
from .views import (Product_GraphQL)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('graphql/products', Product_GraphQL)
urlpatterns= router.urls

urlpatterns.extend([
	# Put here normal urlpatterns
])
```


</b>






















