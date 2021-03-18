"""ninjaApp URL Configuration

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
from django.urls import path
from ninja import (NinjaAPI, Schema, Path)
import datetime

api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


class PathDate(Schema):
    year: int
    month: int
    day: int
    def value(self):
        return datetime.date(self.year, self.month, self.day)


@api.get("/events/{year}/{month}/{day}")
def events(request, date: PathDate = Path(...)):
    return {"date": date.value()}




@api.get("/products")
def list_weapons(request, id: int, name: str):
    return {"id":id, "name":name}







class Order(Schema):
	user_id: int
	product_id: int
	amount: float = 1.0

@api.post("/orders/", tags=["Orders: Create"], 
	summary="Create an Order")
def create_order(request, order: Order):
    """
This endpoint will enable you to create an order
Please provide these fields:
- **user_id**: an integer of the id of the user
- **product_id**: an integer of the id of the product
- **amount**: an float representing the amount of the order
    """
    return {"success": True}


@api.post("/orders/several", tags=[
	"Orders: Create Several (Deprecated)"],
 deprecated=True)
def create_orders_several(request, order: Order):
    return {"success": True}











class ServiceUnavailableError(Exception):
    pass


# initializing handler

@api.exception_handler(ServiceUnavailableError)
def service_unavailable(request, exc):
    return api.create_response(
        request,
        {"message": "Please retry later"},
        status=503,
    )


# some logic that throws exception

@api.get("/service")
def some_operation(request):
    raise ServiceUnavailableError()





from ninja.security import APIKeyHeader


class ApiKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        if key == "supersecret":
            return key


header_key = ApiKey()


@api.get("/headerkey", auth=header_key)
def apikey(request):
    return f"Token = {request.auth}"





urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]