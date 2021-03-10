# django-cheat-sheet

<b>

```bash
pip install django
django-admin startproject <app name> # Create a django app
cd <app name> # Get to the directory
python manage.py runserver
python manage.py startapp <new app name>
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
winpty python manage.py createsuperuser #Windows
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
```python
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












## 6) Migrations:



<b>

`articles/models.py`
```bash
python manage.py makemigrations
python manage.py migrate
```

</b>


- `makemigrations`: This will create the migrations files
- `migrate`: This will reflect the migration files 
to the data base


- Every time you make changes to your models, you should run these 2
lines of code.










## 7) ORM:



<b>

```python
from articles.models import Article

article = Article()
article.title = "ABC"
article.save() # This will save the article to the database
a = Article.objects.all()[0]
print(a.title) # ABC
```

</b>














## 8) Admin:



<b>

`sampleApp/urls.py`
```python
from django.contrib import admin
from django.urls import (path)

urlpatterns = [
	...,
    path('admin/', admin.site.urls),
]
```


```bash
python manage.py createsuperuser
winpty python manage.py createsuperuser #Windows
```


</b>


username: omar  
password: 123










<b>

`articles/admin.py`
```python
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

</b>

So now, when we open the admin area on the browser, it will 
show the articles.







<b>

`articles/models.py`
```python
from django.db import models

class Article(models.Model):
	...,

	def __str__(self):
		return self.title
```

</b>

This is how you control how each instace is represented in the
admin area.











## 9) Template tags:

<b>

`articles/views.py`
```python
from django.shortcuts import render
from .models import Article

def articles_list_page(request):
	articles = Article.objects.all().order_by("id")
	return render(request, "articles/articles_list.html",
		{"articles":articles})
```

</b>

To pass the data to the template.



<b>

`articles/templates/articles_list.html`
```html
<div class="aricles">
{% for article in articles %}
	<div class="aricle">
		<h1>{{ article.title }}</h1>
		<p>{{ article.slug }}, {{ article.date }}</p>
		<p>{{ article.body }}</p>
		<hr>
	</div>

{% endfor %}
</div>
```

</b>

To display passed data.















## 10) Static files:

<b>

`assets/styles.css`
```python
STATIC_URL = '/static/'

import os

STATICFILES_DIRS = (
os.path.join(BASE_DIR, "assets"),
)
```
</b>



<b>

`sampleApp/settings.py`
```python
STATIC_URL = '/static/'

import os

STATICFILES_DIRS = (
os.path.join(BASE_DIR, "assets")
)
```

</b>



<b>

`sampleApp/urls.py`
```python
from django.contrib.staticfiles.urls import (
    staticfiles_urlpatterns)

urlpatterns = [ # url patterns like normal
]

urlpatterns += staticfiles_urlpatterns()
```

</b>





Now, in the browser, open this links:
<a href="http://127.0.0.1:8000/static/style.css">
http://127.0.0.1:8000/static/style.css</a>.  
You will be able to see the style file.








## 11) Extending templates:





<b>

`templates/base_layout.py`
```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>

	<div class="wrapper">
		{% block content %}
		{% endblock %}
	</div>

	<hr>
	All inside the block
</body>
</html>
```


`articles/articles_list.html`
```html
{% extends 'base_layout.html' %}
{% block content %}

	<div class="aricles">
	{% for article in articles %}
		<div class="aricle">
			<h1>{{ article.title }}</h1>
			<p>{{ article.slug }}, {{ article.date }}</p>
			<p>{{ article.body }}</p>
			<hr>
		</div>

	{% endfor %}
	</div>

{% endblock %}
```


</b>












## 12) url Parameters:




<b>

`articles/views.py`
```python
from django.http import HttpResponse

def article_page(request,id):
	return HttpResponse(id)
```


`articles/urls.py`
```python
from django.urls import path
from .views import article_page

urlpatterns = [
    path('<int:id>', article_page),
]
```


</b>




## 13) url names:




<b>

`articles/urls.py`
```python
from django.urls import path
from .views import article_page

urlpatterns = [
    path('<int:id>', article_page, name="specific"),
]
```

</b>



Now we can redirect to this page using : `aricles:specific`.








