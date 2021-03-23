# 6-3) Serializers: **Validation** of serialization:


## 1) Validation Types:

### 1-1) Types of fields

<b>

```python
class NumberSerializer(serializers.Serializer):
	myNum = serializers.IntegerField()
```
</b>

Here Of you input to the `email` field a string that is invalid,
this will fail in case of validation.



### 1-2) Field-Level Validation

To validte using the field, 
- create a method in the serializer that has a name like this:

**`validate_<Field_name>`**

Example:
<b>

```python
class NumberSerializer(serializers.Serializer):
	myNum = serializers.IntegerField()
	
	def validate_myNum(self, value):
		if value <= 0:
			raise serializers.ValidationError(
				"myNum must be a positive number")
```

</b>


This will be validated automatically in case of validation 
unless the the field `required` was equal to `False`, and the 
this value was not input.


### 1-3) Custom Validation (Validators)

<b>

```python
def validate_myNum(value):
	if value <= 0:
		raise serializers.ValidationError(
			"myNum must be a positive number")

class NumberSerializer(serializers.Serializer):
	myNum = serializers.IntegerField(validators=[validate_myNum])
```

</b>

Note: There are built-in validators, that we will discuss later
 in the **Validators** section.





### 1-4) Object-Level Validation


<b>

```python
class NumberSerializer(serializers.Serializer):
	myNum = serializers.IntegerField()
	
	def validate_myNum(self, data):
		if data["myNum"] <= 0:
			raise serializers.ValidationError(
				"myNum must be a positive number")
```

</b>












## 2) How to validate:


1. Execute the **`.is_valid()`** method
2. Get the **`.errors`** attribute


**`is_valid()`** returns **`True`** or **`False`**.  
**`errors`** return a dictionary like this:  


```python
{
	"field_1": "error message 1",
	"field_2": "error message 2",
	...
}
```





<b>

```python
if serializer.is_valid():
	serializer.save()
else:
	return serializer.errors
```

</b>

### 3) `is_valid()` parameters:

<b>

```python
# Return a 400 response if the data was invalid.
serializer.is_valid(raise_exception=True)
```
</b>

The default value of `raise_exception` = `False`










































































