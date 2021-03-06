# django-cheat-sheet

<b>

```bash
pip install django
django-admin startproject <app name> # Create a django app
cd <app name> # Get to the directory
python manage.py runserver
```

</b>



## 1) Create application:

<b>

```bash
pip install django
django-admin startproject <app name> # Create a django app
cd <app name> # Get to the directory
python manage.py runserver
```

</b>


Now, in the browser open this link:  
<b>
<a href="http://127.0.0.1:8000/" target="_blank">
http://127.0.0.1:8000/</a>
</b>  


To close the server : **`ctrl`** + **`c`**.






## 2) views and urls:



<b>
	


`views.py`
```python
from django.http import HttpResponse

def about(request):
	return HttpResponse("About")

def homepage(request):
	return HttpResponse("Home Page")
```





`urls.py`
```python
from django.contrib import admin
from django.urls import path
from .views import (about, homepage)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('about/', about),
]
```

</b>



In the browser open these links:

<b>

<a href="http://127.0.0.1:8000" target="_blank">
http://127.0.0.1:8000</a>
<br>
<a href="http://127.0.0.1:8000/about" target="_blank">
http://127.0.0.1:8000/about</a>
<br>

<a href="http://127.0.0.1:8000/admin" target="_blank">
http://127.0.0.1:8000/admin</a>



</b>  











## 3) Django Apps:







