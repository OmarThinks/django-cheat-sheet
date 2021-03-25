from .models import Product
from rest_framework import serializers
from django_restql.mixins import DynamicFieldsMixin
from rest_framework import viewsets
from django_restql.mixins import EagerLoadingMixin

class ProductSerializer(#DynamicFieldsMixin, 
	serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"







class ProductViewSet(EagerLoadingMixin, viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    # The Interpretation of this is 
    # Select `course` only if program field is included in a query
    
    """select_related = {
        "program": "course"
    }"""

    # The Interpretation of this is 
    # Prefetch `course__books` only if program or program.books 
    # fields are included in a query
    """prefetch_related = {
        "program.books": "course__books"
    }"""


