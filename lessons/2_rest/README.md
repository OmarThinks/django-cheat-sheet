# 2) Django REST Framework



## 1) Create app:


<b>

```bash
pip install django
pip install djangorestframework
pip freeze --local > requirements.txt
django-admin startproject restApp # Application name
cd restApp # Application name
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
winpty python manage.py createsuperuser #Windows
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


</b>






