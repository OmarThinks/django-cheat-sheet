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



