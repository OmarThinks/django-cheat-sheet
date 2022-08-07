# Django Cheat Sheet


## CLI:


```bash
pip install django
django-admin startproject [project name: Example: mysite]
python manage.py runserver

python manage.py startapp [an app inside the project: example: polls]

```




## views.py:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```



## urls.py:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```


## models.py















<!--



<h2>
	<a href="lessons/1_django/README.md">
		1) Django
	</a>
</h2>


<h2>
	<a href="lessons/2_ninja/README.md">
		2) Django Ninja
	</a>
</h2>

<h2>
	<a href="lessons/3_rest/README.md">
		3) Django Rest Framework
	</a>
</h2>



<h2>
	<a href="lessons/4_auth/README.md">
		4) Django REST Framework + Authentication
	</a>
</h2>

-->


<!--


<h2>
	<a href="lessons/5_graphql/README.md">
		5) GraphQL + Django
	</a>
</h2>


-->



