# 3) Relay:


# 1 Example:




<b>


```python
# cookbook/schema.py
import graphene

class HelloQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

from graphene_django import DjangoObjectType
from ingredients.models import Category, Ingredient


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

class MainQuery(HelloQuery,ModelsQuery):
    # This is the query of the server
    # It inherets from all the queries
    # To form the query that the server will handle
    pass

schema = graphene.Schema(query=MainQuery)
```


</b>



































