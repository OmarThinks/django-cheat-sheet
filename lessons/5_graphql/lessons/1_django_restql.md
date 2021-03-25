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

# 3) Example:

<b>


CLI: Bash Commands

```bash
django-admin startproject tutorial
cd tutorial
python manage.py startapp products
```


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


```
tutorial/settings.py
```
```python
INSTALLED_APPS = [
    ... ,
    'products'
]
```

`tutorial/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include("products.urls")),
]
```


`products/views.py`
```python
from .models import Product
from rest_framework import serializers
from django_restql.mixins import DynamicFieldsMixin

class ProductSerializer(DynamicFieldsMixin, 
	serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"

```



`products/urls.py`
```python
from .views import (ProductSerializer)

```






Bash

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
winpty python manage.py createsuperuser # For windows OS
# username: admin, password: admin
```



</b>


























