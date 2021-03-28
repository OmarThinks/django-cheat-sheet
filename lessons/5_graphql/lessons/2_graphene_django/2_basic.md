# 2) Basic Tutorial:


# 1) Creating an application:

Here we will craete aan application and call it **`ingredients`**

<b>

```bash
django-admin startproject cookbook
cd cookbook
django-admin startapp ingredients
```

Creating the models


```python
# cookbook/ingredients/models.py
from django.db import models

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

from django.contrib import admin

admin.site.register(Category)
admin.site.register(Ingredient)
```



```python
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
```



Installing the app

```python
# cookbook/settings.py

INSTALLED_APPS = [
    ...
    # Install the ingredients app
    'django.contrib.staticfiles',
    "graphene_django",
    "ingredients",
]
```


Migrating:

```bash
python manage.py makemigrations
python manage.py migrate
```



Create a super user:



```bash
python manage.py createsuperuser # Linux
winpty python manage.py createsuperuser # Windows
```

username: admin  
password: admin





`cookbook/urls.py`
```python
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql", GraphQLView.as_view(graphiql=True,
    	schema = schema)),
]
```



Running the server:

```bash
python manage.py runserver
```

Create some data by going to  http://127.0.0.1:8000/admin/


</b>












# 2) Testing the application:



http://127.0.0.1:8000/graphql



<b>



Request:
```graphql
{
  allIngredients {
    id
    name
  }
}
```



Response:

```json
{
  "data": {
    "allIngredients": [
      {
        "id": "1",
        "name": "Rice"
      },
      {
        "id": "2",
        "name": "Hot Sause"
      }
    ]
  }
}
```

---




















Request:
```graphql
query {
  categoryByName(name: "Meat") {
    id
    name
    ingredients {
      id
      name
    }
  }
}
```



Response:

```json
{
  "data": {
    "categoryByName": {
      "id": "2",
      "name": "Meat",
      "ingredients": [
        {
          "id": "3",
          "name": "Cow Meat"
        },
        {
          "id": "4",
          "name": "Fish"
        },
        {
          "id": "8",
          "name": "Penguin"
        }
      ]
    }
  }
}
```

---










Request:
```graphql
query {
  allIngredients {
    id
    name
    category {
      id
      name
    }
  }
}
```



Response:

```json
{
  "data": {
    "allIngredients": [
      {
        "id": "1",
        "name": "Rice",
        "category": {
          "id": "3",
          "name": "Vegan"
        }
      },
      {
        "id": "2",
        "name": "Hot Sause",
        "category": {
          "id": "1",
          "name": "Spicy"
        }
      }
    ]
  }
}
```





























</b>


































