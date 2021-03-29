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

    def __str__(self):
        return self.name
"""
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











# Here are the mutations:




class CategoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        id = graphene.ID()

    # The class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(pk=id)
        category.name = name
        category.save()
        # Notice we return an instance of this mutation
        return CategoryMutation(category=category)







class IngredientMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        notes = graphene.String(required=True)
        category = graphene.Int(required=True)
        id = graphene.ID()

    # The class attributes define the response of the mutation
    ingredient = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls, root, info, name,category_id, notes, id):
        ingredient = Ingredient.objects.get(pk=id)
        ingredient.name = name
        ingredient.category_id = category_id
        ingredient.notes = notes
        ingredient.save()
        # Notice we return an instance of this mutation
        return IngredientMutation(ingredient=ingredient)







class ModelsMutation(graphene.ObjectType):
    create_category = CategoryMutation.Field()
    create_ingredient = IngredientMutation.Field()

"""
class ModelsMutation(
    CategoryMutation,
    IngredientMutation, # Add your Mutation objects here
    graphene.ObjectType
):
    pass
"""













class MainQuery(HelloQuery,ModelsQuery):
    # This is the query of the server
    # It inherets from all the queries
    # To form the query that the server will handle
    pass

schema = graphene.Schema(query=MainQuery, mutation=ModelsMutation)

