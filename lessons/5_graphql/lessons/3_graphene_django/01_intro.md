# 1) Intro:


# 1) What ?

**`graphene-django`** is a package that enables you to use 
graphql (graphene) with django.



# 2) How to use:

<b>

```bash
pip install graphene-django
```




`settings.py`

```python
INSTALLED_APPS = [
    ...
    "django.contrib.staticfiles", # Required for GraphiQL
    "graphene_django"
]

GRAPHENE = {
    "SCHEMA": "django_root.schema.schema"
    # There is another way to declare the schema,
    # We will explain it in the next code
}

```
</b>

This **`GRAPHENE["SCHEMA"]`** variable in **settings.py** needs
 to be explained:
- **`SCHEMA`**: points to the location of the schema variable
	- **`django_root`**: The name of the application containing the 
		schema variable  
		It will probably be the main django application  
		You can replace it by the name of the main app in your 
		project
	- **`schema`**: there is a file called **`schema.py`** that
		contains the **`schema`** variable.
	- **`schema`**: this is the name of the variable that 
		contains the schema.

<b>

`urls.py`
```python
from django.urls import path
from graphene_django.views import GraphQLView

from .schema import schema

urlpatterns = [
    # ...
    path("graphql", GraphQLView.as_view(graphiql=True)),
    # path("graphql", GraphQLView.as_view(graphiql=True,
    # schema=schema))
    # This is another way to declare the schema
]
```
</b>



- **`graphiql`**
	- **`True`**: To enable GraphiQL API browser
	- **`False`**: To disable GraphiQL API browser







<b>

Very basic schema.  
`schema.py`

```python
import graphene

class HelloQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

class MainQuery(HelloQuery, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    # This is the query of the server
    # It inherets from all the queries
    # To form the query that the server will handle
    pass

schema = graphene.Schema(query=MainQuery)
```
</b>


In your application there will be **lots of small queries**.  
Each query may represent a model.  
For example:
- ProductsQuery
- UsersQuery
- OrdersQuery

**But there is only ony Main query that the server will handle.  
This main query inherts form all the small queries creating the 
GraphQL server.**
















# 3) Using Graphql:



1. Open the server
2. Open the browers http://127.0.0.1:8000/graphql
3. Type This code:

<b>

```graphql
{
  hello
}
```
</b>



4. You will get this response:

<b>

```json
{
  "data": {
    "hello": "Hi!"
  }
}
```
</b>




