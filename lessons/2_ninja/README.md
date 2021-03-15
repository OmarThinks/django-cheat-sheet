# 2) Django Ninja



## 1) Hello, Ninja!


<b>

```bash
pip install django-ninja
django-admin startproject ninjaApp # Create a django app
cd ninjaApp # Get to the directory
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
winpty python manage.py createsuperuser #Windows
python manage.py runserver
```

</b>

username:admin  
password:admin


<b>

`ninjaApp/urls.py`
```python
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
```

</b>

In your browser test this address:

<b>

http://127.0.0.1:8000/api/add?a=1&b=2

</b>

The result will be:

```json
{"result": 3}
```









## 2) Interactive API docs:



In your browser, go to this location:  


<b>
<a href="http://127.0.0.1:8000/api/docs">
http://127.0.0.1:8000/api/docs
</a>
</b>



















## 3) API Endpoints:

You need to know what is the **request method**, these are 
examples of the request methods:  
- GET
- POST
- PUT
- DELETE
- Patch
- ...

<b>

```python
@api.get("/path")
def get_operation(request):
    ...
```

</b>


































