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













"""
Serialization
Part 1
Serializing objects
"""

class ProductClass:
	def __init__(self, name, owner=1, in_stock=True):
		
		self.name = name
		self.owner = owner
		self.in_stock = in_stock

p = ProductClass(name='Stawberry', owner=1, in_stock=True)




from rest_framework import serializers

class ProductSerializerTest(serializers.Serializer):
	name = serializers.CharField()
	owner = serializers.IntegerField()
	in_stock = serializers.BooleanField()


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer

class SerializerViewSet(viewsets.ViewSet):
	"""
	Learing serializers!
	"""
	def serializing(self, request):
		# Here we will Test serialization
		p = ProductClass(name=123, owner="123", in_stock= True)
		p_serialized = ProductSerializerTest(p)
		data = p_serialized.data
		json = JSONRenderer().render(p_serialized.data)

		print(data, flush=True)
		# {'name': '123', 'owner': 123, 'in_stock': True}
		print(json, flush=True)
		# b'{"name":"123","owner":123,"in_stock":true}'
		return Response({"data": data, "json": json, 
			"details": "Serializing, note, data has been casted to"+
			" the right types."})
		"""
{
	"data": {
		"name": "123",
		"owner": 123,
		"in_stock": true
	},
	"json": "{\"name\":\"123\",\"owner\":123,\"in_stock\":true}",
	"details": "Serializing, note, data has been casted to the right types."
}
		"""

	def deserializing_1(self, request):
		# Here we will Test deserialization
		data = {"name":1234, "owner":"12", "in_stock": 1,
		"useless": "this useless field will no appear"}
		p_deserialized = ProductSerializerTest(data=data)

		is_valid = p_deserialized.is_valid()
		errors = p_deserialized.errors
		data = p_deserialized.data
		print(is_valid, flush=True)
		# True
		print(errors, flush=True)
		# {}
		print(data, flush=True)
		# {'name': '1234', 'owner': 12, 'in_stock': True}
		return Response({"is_valid": is_valid, "errors": errors,
			"data":data, 
			"details":"Deserializing, Note, data has been"+
			" casted to types, and useless"+
			" field has not appeared."})
		"""
{
	"is_valid": true,
	"errors": {},
	"data": {
		"name": "1234",
		"owner": 12,
		"in_stock": true
	},
	"details": "Deserializing, Note, data has been casted to types, and useless field has not appeared."
}
		"""

	def deserializing_2(self, request):
		# Here we will Test deserialization with errors
		data = {"name":1234, "owner":"Can't be casted to int"}
		p_deserialized = ProductSerializerTest(data=data)

		is_valid = p_deserialized.is_valid()
		errors = p_deserialized.errors
		data = p_deserialized.data
		
		print(is_valid, flush=True)
		# False
		print(errors, flush=True)
		"""
		{'owner': 
			[
				ErrorDetail(string='A valid integer is required.', 
				code='invalid')
			], 
		'in_stock': 
			[
				ErrorDetail(
				string='This field is required.', 
				code='required')
			]
		}
		"""
		print(p_deserialized.data, flush=True)
		# {'name': 1234, 'owner': "Can't be casted to int"}
		return Response({"data":data,"is_valid": is_valid, 
			"errors": errors, 
			"details":"Deserializing withh errors"})
		"""
{
	"data": {
		"name": 1234,
		"owner": "Can't be casted to int"
	},
	"is_valid": false,
	"errors": {
		"owner": [
			"A valid integer is required."
		],
		"in_stock": [
			"This field is required."
		]
	},
	"details": "Deserializing withh errors"
}
		"""

s_a1 = SerializerViewSet.as_view({'get': 'serializing'})
s_a2 = SerializerViewSet.as_view({'get': 'deserializing_1'})
s_a3 = SerializerViewSet.as_view({'get': 'deserializing_2'})











































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


























































