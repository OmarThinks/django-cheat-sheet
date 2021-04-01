# 1-1) Fields:



## 1) Object:


<b>

```graphql
{
  hero {
    name
  }
}
```

```json
{
  "data": {
    "hero": {
      "name": "R2-D2"
    }
  }
}
```
</b>


You just asked for the name of the product only.




## 2) Sub-Object:

<b>

```graphql
{
  hero {
    name,id
    friends{
      id
    }
  }
}
```






```json
{
  "data": {
    "hero": {
      "name": "R2-D2",
      "id": "2001",
      "friends": [
        {
          "id": "1000"
        },
        {
          "id": "1002"
        },
        {
          "id": "1003"
        }
      ]
    }
  }
}
```

</b>


Here you asked for the `id` and `name` of the `hero`.  
And the `friends` of the `hero`.  
`friends` is a list of objects.  

So for each friend you asked for the `id`.




## 3) Comments:


<b>

```graphql
{
  hero {
    # This is a comment
    name
  }
}
```
</b>