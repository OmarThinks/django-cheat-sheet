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


usual_urlpatterns = [
	# Put here normal urlpatterns	
]

urlpatterns.extend(usual_urlpatterns)
```


</b>







# 3) Example Query Requests:



## 3-1) Getting list of products:


<b>

Request

```bash
curl --location --request GET 'http://127.0.0.1:8000/graphql/products/'
```


Response:


```json
[
    {
        "id": 1,
        "name": "784213248343",
        "in_stock": true,
        "owner": 1
    },
    {
        "id": 2,
        "name": "trbxcty",
        "in_stock": true,
        "owner": 1
    }
]
```







## 3-2) Sending a query with products list:



Request

```bash
curl --location -g --request GET 'http://127.0.0.1:8000/graphql/products/?query={id}'
```


Response:


```json
[
    {
        "id": 1
    },
    {
        "id": 2
    }
]
```


The query is sent as a query parameter.









# 4) Example Mutation Requests:








## 4-1) Adding a Product:


<b>

Request

```bash
curl --location --request POST 'http://127.0.0.1:8000/graphql/products/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"Lab Top",
    "in_stock":false
}'
```


Response:


```json
{
    "id": 6,
    "name": "Lab Top",
    "in_stock": false,
    "owner": 1
}
```









## 4-2) Modifing a Product:


<b>

Request

```bash
curl --location --request PUT 'http://127.0.0.1:8000/graphql/products/6/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "i Phone",
    "in_stock": false
}'
```


Response:


```json
{
    "id": 6,
    "name": "i Phone",
    "in_stock": false,
    "owner": 1
}
```











## 4-3) Deleting a product:


<b>

Request

```bash
curl --location --request DELETE 'http://127.0.0.1:8000/graphql/products/6/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "784213248343"
}'
```


Response:


```json

```


The response is empty.



















</b>
