# 7) Validators:


# 1) How to use:


<b>

```python
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
class CustomerReportSerializer(serializers.ModelSerializer):
    reference = CharField(
    	validators=[UniqueValidator(queryset=
    	CustomerReportRecord.objects.all())])
```

</b>



# 2) Unique:

## 2-1) `UniqueValidator`:
### Example:
<b>

```python
from rest_framework.validators import UniqueValidator

slug = SlugField(
    max_length=100,
    validators=[UniqueValidator(queryset=BlogPost.objects.all())]
)
```
</b>

### Parameters:
- **`queryset`** 
	- **required**
	- This is the queryset against which uniqueness should be enforced.
- **`message`** 
	- The error message that should be used when validation fails.
- **`lookup`**
	- The lookup used to find an existing instance with the value 
		being validated. Defaults to `exact`.





## 2-2) `UniqueTogetherValidator`:
### Example:
<b>

```python
from rest_framework.validators import UniqueTogetherValidator

class ExampleSerializer(serializers.Serializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=ToDoItem.objects.all(),
                fields=['list', 'position']
            )
        ]
```
</b>












# 3) Defaults:


## 3-1) `CurrentUserDefault`:
<b>

```python
owner = serializers.HiddenField(
	default=serializers.CurrentUserDefault()
)
```
</b>


## 3-2) `CreateOnlyDefault`:

This will only be used during the creation of the field.  
But it will be omitted during updates

<b>

```python
created_at = serializers.DateTimeField(
    default=serializers.CreateOnlyDefault(timezone.now)
)
```
</b>












































