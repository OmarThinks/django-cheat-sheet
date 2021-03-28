# cookbook/schema.py
import graphene

class HelloQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")



from graphene_django import DjangoObjectType
from ingredients.models import Category, Ingredient

"""
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name="ingredients", 
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ModelsQuery(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientNode)
    category_by_name = graphene.Field(CategoryNode, 
        name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
"""





class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ["id", "name", "ingredients"]
        interfaces = (graphene.relay.Node, )

class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = ["id", "name", "notes", "category"]
        interfaces = (graphene.relay.Node, )



from graphene_django.filter import DjangoFilterConnectionField

class ModelsQuery(graphene.ObjectType):
    category = graphene.relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = graphene.relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)




























class MainQuery(HelloQuery,ModelsQuery, graphene.ObjectType):
    # This is the query of the server
    # It inherets from all the queries
    # To form the query that the server will handle
    pass

schema = graphene.Schema(query=MainQuery)

