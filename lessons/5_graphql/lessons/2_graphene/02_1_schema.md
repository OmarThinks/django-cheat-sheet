# 2-1) Schema:



# 1) Introduction:


Before we start, the shema is the final product of the GraphQL 
server.  
So when interacting with a graphQL server, you are interacting with 
the schema.



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


























