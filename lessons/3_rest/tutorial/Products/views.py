from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product


"""
import json
from pydantic import BaseModel, ValidationError ,validator
from pydantic.schema import schema











from enum import Enum
from pydantic import BaseModel, Field


class FooBar(BaseModel):
	count: int
	size: float = None


class Gender(str, Enum):
	male = 'male'
	female = 'female'
	other = 'other'
	not_given = 'not_given'


class MainModel(BaseModel):
	This is the description of the main model

	foo_bar: FooBar = Field(...)
	gender: Gender = Field(None, alias='Gender')
	snap: int = Field(
		42,
		title='The Snap',
		description='this is the value of snap',
		gt=30,
		lt=50,
	)

	class Config:
		title = 'Main'
	@validator('foo_bar')
	def name_must_contain_space(cls, v):
		if ' ' not in v:
			raise ValidationError('must contain a space')
		return v


# this is equivalent to json.dumps(MainModel.schema(), indent=2):













"""






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

	@action(detail = False, methods=["post"],
		authentication_classes=[])
	def h3(self, request):
		return Response({"message": "Hello, 3!"})

h1 = HelloViewSet.as_view({'get': 'h1'})
h2 = HelloViewSet.as_view({'get': 'h2', 'post': 'h3'})














