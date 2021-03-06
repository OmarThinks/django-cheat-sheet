# 2-2) Scalars:






# 1) Intro:

Scalars of the Query  
= Attribute of the Class  
= Field of the Model




# 2) Scalar Attributes:

All these attributes are optional:






- **`name`**:
    - datatype: `string`
    - override the name of the field
    - default : camelCase of the attribute
    - Examples:
        - **`product_name = graphene.String() # name=productName`**
        - **`product_name = graphene.String(name = "product_name")`**



- **`required`**:
    - datatype: `boolean`
    - Is this field required or not
    - default : **`False`**

- **`default_value`**:
    - datatype: `any`
    - Provide a default value for the Field.





- **`description`**:
    - datatype: `string`
    - A description of the type to show in the GraphiQL browser



























# 2) Built-In Scalars:

<b>

```python
class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'

schema = Schema(query=Query)
```



- `graphene.String`
- `graphene.Int`
- `graphene.Float`
- `graphene.Boolean`
- `graphene.ID`

---

- `graphene.Date`
- `graphene.DateTime`
- `graphene.Time`


---

- `graphene.Decimal`
- `graphene.JSONString`
- `graphene.Base64`




</b>



