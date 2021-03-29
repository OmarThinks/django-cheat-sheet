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
import graphene
from graphene import ObjectType

class Query(ObjectType):
    goodbye = graphene.String()

    def resolve_goodbye(root, info):
        return 'See ya!'
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



