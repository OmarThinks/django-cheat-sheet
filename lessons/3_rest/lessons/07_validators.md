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

## 2-1) UniqueValidator:

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




















