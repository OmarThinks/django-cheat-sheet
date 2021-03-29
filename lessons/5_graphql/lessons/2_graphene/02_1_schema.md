# 2-1) Schema:



# 1) Introduction:


Before we start, the shema is the final product of the GraphQL 
server.  
So when interacting with a graphQL server, you are interacting with 
the schema.  
Schemas have components, each component needs to be explianed.  
So it will take time to understand these components.  
In this lesson, we will talk beriefly about the components 
of the schema.

This is a schema example:


```python
schema(
	query = MyRootQuery, # Madnatory
	mutation = MyRootMutation, # Optional, default = None
    subscription=MyRootSubscription, #Optional, default = None
    # types=[SomeExtraObjectType, ],
    auto_camelcase=False # Optional, default = True
)
```


# 2) What:

**Schema** = The **definition** of **Types** and 
**Relationships** in the API



<b>

```python
my_schema = Schema(
    query=MyRootQuery,
    mutation=MyRootMutation,
    subscription=MyRootSubscription
)
```
</b>



- **`query`**: 
	- **Madnatory**
	- **Query fetches data**
- **`mutauion`**: 
	- Optional
	- **Mutation changes data and retrieves the changes**
- **`subscription`**: 
	- Optional
	- **Subscription sends changes to clients in real-time**



# 3) Executing a query:

<b>

```python
query_string = 'query whoIsMyBestFriend { myBestFriend { lastName } }'
my_schema.execute(query_string)
```
</b>

We execute the query using the **`execute`** method.





# 4) Types:


Sometimes the schema can not access all the types.  
In this case we need to use the **`types` argument** 
<b>

```python
my_schema = Schema(
    query=MyRootQuery,
    types=[SomeExtraObjectType, ]
)
```
</b>





# 5) Auto cammelCase Fields:


**`snake_case` -> `camelCase`**  
**`last_name` -> `lastName`**  

By default, field name will be converted to camel case.  
But you can break this:

## 5-1) Using `name` parameter of the field:
<b>

```python
class Person(graphene.ObjectType):
    last_name = graphene.String()
    other_name = graphene.String(name='_other_Name')
```

```grapgql
{
    lastName
    _other_Name
}
```

</b>

## 5-2) Turn off `camelCase` in the schema

You can **turn off the auto camel case**.

<b>

```python
my_schema = Schema(
    query=MyRootQuery,
    auto_camelcase=False,
)
```

</b>













