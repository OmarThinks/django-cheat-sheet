# 2-3) Lists:


# 1) Intro:
This lesson is about nesting fields or types into ecah other.  
So that we benifit from the validation of several validations in one 
field.






# 2) NonNull:

<b>

```python
import graphene

class Character(graphene.ObjectType):
    name = graphene.NonNull(graphene.String)
    # name = graphene.String(required=True)
    # These are the same
```
</b>
This means the server should return a not null string.











# 3) Lists:

<b>

```python
import graphene

class Character(graphene.ObjectType):
    appears_in = graphene.List(graphene.String)
```
</b>
This means the server should return a list of the string type.











# 4) NonNull Lists:

<b>

```python
import graphene

class Character(graphene.ObjectType):
    appears_in = graphene.List(graphene.NonNull(graphene.String))
```
</b>
The server should return a list of strings, 
each one of them is Not null.

