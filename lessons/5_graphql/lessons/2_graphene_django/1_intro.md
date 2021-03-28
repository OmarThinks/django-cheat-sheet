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
}
```


`urls.py`
```python
from django.urls import path
from graphene_django.views import GraphQLView

urlpatterns = [
    # ...
    path("graphql", GraphQLView.as_view(graphiql=True)),
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

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

schema = graphene.Schema(query=Query)
```
</b>



