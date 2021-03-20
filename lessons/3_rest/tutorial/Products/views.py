from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product








from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class HelloViewSet(viewsets.ViewSet):
	"""
	Hello, World!

	"""
	def h1(self, request):
		return Response({"message": "Hello1, 1!"})

	def h2(self, request):
		return Response({"message": "Hello, 2!"})

	@action(detail = False, methods=["post"], permission_classes =[],
		authentication_classes=[])
	def h3(self, request):
		return Response({"message": "Hello, 3!"})

h1 = HelloViewSet.as_view({'get': 'h1'})
h2 = HelloViewSet.as_view({'get': 'h2', 'post': 'h3'})


















class ProductClass:
    def __init__(self, name, owner=1, 
    	in_stock=True, created=datetime.now()):
        self.name = name
        self.owner = owner
        self.in_stock = in_stock
        self.created = created

p = ProductClass(name='Stawberry', owner=1, in_stock=True)































