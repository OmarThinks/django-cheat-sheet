# 6-2) Serializers: **Models** serialization and deserialization:



## 1) What is the content:

Here we will handle serialization with an ORM model.



## 2) Example:


<b>

`models.py`

Here there is the model in the Intro lesson

```python
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	name = models.CharField(max_length=1)
	in_stock = models.BooleanField(default=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, 
		null=False, blank=False, default=1)
```



`views.py`

```python
"""
Serialization
Part 2
Models Serialization
"""
from rest_framework import serializers

class ProductSerializer_2(serializers.Serializer):
	"""
	This is the serializaer of the Product model 
	"""
	name = serializers.CharField()
	owner = serializers.IntegerField()
	in_stock = serializers.BooleanField()

	def create(self, validated_data):
		return Product(**validated_data)
		# return Comment.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.owner = validated_data.get('owner', instance.owner)
		instance.in_stock = validated_data.get(
			'in_stock', instance.in_stock)
		# instance.save()
		return instance
```

</b>

