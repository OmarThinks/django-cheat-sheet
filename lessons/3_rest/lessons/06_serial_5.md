# 6-5) Serializers: Part 5:

**Methods and attributes**.







## 1) Attributes:
This is a list of the default attributes of the serializer model:



- **`.data`**: Returns the outgoing primitive representation
    - The output is in the form of a dictionary
- **`.validated_data `**: Returns the validated incoming data
- **`.errors`**: Returns any errors during validation




## 2) Methods:
This is a list of the default methods of the serializer model:






- **`.is_valid()`** - Deserializes and validates incoming data
    - returns **`True`** or **`False`**
- **`.save()`**: Persists the validated data into an object instance
- **`.create()` and `.update()`**: Override either or both of these to support saving instances

















Before using `.errors`, you need to use `.is_valid()`

