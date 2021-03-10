# django-cheat-sheet

<b>

```bash
pip install django
django-admin startproject <app name> # Create a django app
cd <app name> # Get to the directory
python manage.py runserver
python manage.py startapp <new app name>
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











## 3) HTML Templates:




<b>
	


`templates/home.html`
```html
This is home template, Welcome my freind.
```


`simpleApp/views.py`
```python
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	#return HttpResponse("Home Page")
	return render(request, "home.html")
```





`simpleApp/urls.py`
```python
from django.contrib import admin
from django.urls import path
from .views import (homepage)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
]
```


`simpleApp/settings.py`
```python
TEMPLATES = [
    { 'DIRS': ["templates"], },
]
```

</b>




































## 4) Django Apps:



<b>

```bash
python manage.py startapp <new app name>
```


```bash
python manage.py startapp articles
```

</b>

This comman will create a folder called `articles` and fill it
with files.  
This is a new sub application inside your big application.




<b>

`articles/templates/articles/articles_list.html`
```html
Articles list are here
```


`articles/views.py`
```python
from django.shortcuts import render

def articles_list_page(request):
	return render(request, "articles/articles_list.html")
```



`articles/urls.py`
```python
from django.urls import path
from .views import (articles_list_page)

urlpatterns = [
    path('', articles_list_page),
]
```




`sampleApp/settings.py`
```python
INSTALLED_APPS = [
    ...,
    "articles",
    # We just added the articles application
]
```


`sampleApp/urls.py`
```python
from django.contrib import admin
from django.urls import (path, include)

urlpatterns = [
    path('', homepage),
    path('articles/',include("articles.urls")),
    # We just added the articles app urls
]
```

</b>















## 5) Models:



<b>

`articles/models.py`
```bash
from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=100) 
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	# On creating a new article, the new date will be automatically
	# set to now
	# Add author later
	# Add thumbnail later
```



</b>
















