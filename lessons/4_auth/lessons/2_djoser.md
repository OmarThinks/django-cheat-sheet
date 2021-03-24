# 2) Djoser:

# 1) Configuration:

## 1-1) Installation:

<b>

```bash
pip install -U djoser
pip install -U djangorestframework_simplejwt
pip install -U social-auth-app-django
```


## 1-2) `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.auth',
    (...),
    'rest_framework',
    'djoser',
    (...),
]
```


## 1-3) Endpoints:

```python
# User Endpoints
/users/
/users/me/
/users/confirm/
/users/resend_activation/

# Password
/users/set_password/
/users/reset_password/
/users/reset_password_confirm/

# Username
/users/set_username/
/users/reset_username/
/users/reset_username_confirm/

# Token
/token/login/ (Token Based Authentication)
/token/logout/ (Token Based Authentication)

# JWT
/jwt/create/ (JSON Web Token Authentication)
/jwt/refresh/ (JSON Web Token Authentication)
/jwt/verify/ (JSON Web Token Authentication)
```


</b>





