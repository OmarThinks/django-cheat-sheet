# 1) Intro


## 1) Create the App:


Here we will install requirements and create the first app.

<b>

```bash
pip install django
pip install djangorestframework
django-admin startproject tutorial  # Create the app
cd tutorial # Get to the directory
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
winpty python manage.py createsuperuser #Windows
python manage.py runserver
```

</b>



username:admin  
password:admin





`settings.py`

<b>

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

</b>








## 2) Create a product app:


Here we will create a `Product` app so that we can 
play around with.

<b>

```bash
 python manage.py startapp products
```
`products/models.py`

```python
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
	name = models.CharField(max_length=1)
	in_stock = models.BooleanField(default=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, 
		null=False, blank=False, default=1)
```



`tutorial/urls.py`

```python
from django.contrib import admin
from django.urls import (path, include)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include("Products.urls")),
]
```


</b>























