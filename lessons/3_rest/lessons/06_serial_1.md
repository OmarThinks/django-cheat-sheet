# 6-1) Serializers:

**Objects** serialization and deserialization.



## 1) What is serializing:

- **`Serializing`**: allowing complex data such as querysets 
and model instances to be converted to native Python datatypes
- **`Deserializing`**: allowing parsed data to be converted back 
into complex types, after first validating the incoming data



## 2) Example:


<b>

`views.py`

```python
class ProductClass:
	def __init__(self, name, owner=1, in_stock=True):
		self.name = name
		self.owner = owner
		self.in_stock = in_stock

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
```


`urls.py`

```python
from .views import (s_a1, s_a2, s_a3)
from django.urls import (path)

urlpatterns = [
	path('s_a1', s_a1),
	path('s_a2', s_a2),
	path('s_a3', s_a3),
]
```

</b>

