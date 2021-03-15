# 2) Django Ninja



## 1) Create app:


<b>

```bash
pip install django-ninja
django-admin startproject <app name> # Create a django app
cd <app name> # Get to the directory
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

`restApp/settings.py`
```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
]
```



```bash
python manage.py runserver
```

























