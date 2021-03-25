"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]


"""
"username": "abc",
"password": "123abc789"
"""



"""
{
    "refresh": "
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjc2OTU0MSwianRpIjoiM2I0MzNlNzEzYzA4NDllMDhlOTE5MmIyM2IwNTI0ZTgiLCJ1c2VyX2lkIjoyfQ.0734x1f1qFb2zr64wU7IsUv4j4qzHo3G1SsP0Ccahzw
",
    "access": "
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2NjgzNDQxLCJqdGkiOiIyNGVjN2RmN2MxZjc0ZmU3OGU4YTg0MTJkZThkZTRhZiIsInVzZXJfaWQiOjJ9.Eo5xjDWWSLY90y1iblch8WvN0exMKbJDlHta6il6Vcc
"
}
"""

"""
Header
{
  "typ": "JWT",
  "alg": "HS256"
}


Payload
{
  "token_type": "access",
  "exp": 1616683441,
  "jti": "24ec7df7c1f74fe78e8a8412de8de4af",
  "user_id": 2
}
"""

