"""
Here are the serializers of the Product model
"""

from rest_framework import serializers
from .models import Product



class ProductSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField()
	in_stock = serializers.BooleanField(required=False)
	owner = serializers.IntegerField(read_only=True)
	
	def create(self, validated_data):
		"""
		Create and return a new `Product` instance, given the validated data.
		"""
		return Product.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Product` instance, given the validated data.
		"""
		instance.name = validated_data.get(
			'name', instance.name)
		instance.in_stock = validated_data.get(
			'in_stock', instance.in_stock)
		instance.save()
		return instance













