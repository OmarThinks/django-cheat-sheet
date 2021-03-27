from .models import Product
from rest_framework import serializers
from django_restql.mixins import DynamicFieldsMixin
from rest_framework import viewsets
from django_restql.mixins import EagerLoadingMixin

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"




from rest_framework import serializers
from django.contrib.auth.models import User
from django_restql.mixins import (DynamicFieldsMixin, 
	NestedCreateMixin,NestedUpdateMixin)



class ProductSerializer(DynamicFieldsMixin, 
	serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"



from rest_framework import generics




class ProductList_REST(generics.ListCreateAPIView):
	"""
	RESTful API endpoint to get list of products
	"""
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductDetails_REST(generics.RetrieveUpdateDestroyAPIView):
	"""
	RESTful API endpoint to get details, update or 
	delete a specific product
	"""
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	lookup_field = "id"



class Product_GraphQL(DynamicFieldsMixin, viewsets.ModelViewSet):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()

