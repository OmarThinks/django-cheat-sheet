# 2-4) ObjectType:



# 1) Intro:


**A Graphene ObjectType is the building block used to define the relationship between Fields in your Schema and how their data is retrieved.**


# 2) Basics:

1. Each **`ObjectType`** is a Python class that inherits 
from **`graphene.ObjectType`**
2. Each attribute of the ObjectType represents a **`Field`**
3. Each **`Field`** has a **resolver method** to fetch data 
	**(or Default Resolver)**



# 3) Example:

<b>

```python
from graphene import ObjectType, String

class Person(ObjectType):
    first_name = String()
    last_name = String()
    full_name = String()

    # 'first_name' and 'last_name' have defualt resolver
    def resolve_full_name(parent, info):
        return f"{parent.first_name} {parent.last_name}"
```
</b>












# 4) Resolver Parameters:

## 4-1) Parent Value Object (`parent` or `root`):
## 4-2) Execution Info:
## 4-3) GraphQL Arguments (`**kwargs`):




# 5) Convenience Features of Graphene Resolvers:

## 5-1) Implicit staticmethod:
## 5-2) Default Resolver:




# 6) Advanced:


## 6-1) GraphQL Argument defaults:
## 6-2) Resolvers outside the class:
## 6-3) Instances as value objects:
## 6-2) Field camelcasing:

