# cookbook/schema.py
import graphene

class HelloQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

from graphene_django import DjangoObjectType
from ingredients.models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

class ModelsQuery(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, 
        name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

class MainQuery(HelloQuery,ModelsQuery, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    # This is the query of the server
    # It inherets from all the queries
    # To form the query that the server will handle
    pass

schema = graphene.Schema(query=MainQuery)