# Django Cheat Sheet


## CLI:


```bash
pip install django
django-admin startproject [project name: Example: mysite]
cd [project name]
python manage.py runserver

python manage.py startapp [an app inside the project: example: polls]


python manage.py makemigrations
python manage.py makemigrations [app_name?: optional]
python manage.py migrate
python manage.py createsuperuser

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

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
```



## admin.py:

```python
from django.contrib import admin
# Register your models here.

from .models import Question

admin.site.register(Question)
```




## Settings:

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
	...
]
```














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



