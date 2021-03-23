# 6-6) Serializers:

**Fields**.


## 1) How to use Fields:

<b>

```python
from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
```
</b>



## 2) Fields:

These are some of the fields with their 
**signature** (Default values):






<b>


```python
# Boolean Fields
BooleanField()
NullBooleanField()


# String Fields
CharField(max_length=None, min_length=None, 
	allow_blank=False, trim_whitespace=True)
EmailField(max_length=None, min_length=None, allow_blank=False)
RegexField(regex, max_length=None, min_length=None, allow_blank=False)
SlugField(max_length=50, min_length=None, allow_blank=False)
URLField(max_length=200, min_length=None, allow_blank=False)
FilePathField(path, match=None, recursive=False, allow_files=True,
 allow_folders=False, required=None, **kwargs)
IPAddressField(protocol='both', unpack_ipv4=False, **options)


# Numeric Fields
IntegerField(max_value=None, min_value=None)
FloatField(max_value=None, min_value=None)
DecimalField(max_digits, decimal_places, 
	coerce_to_string=None, max_value=None, min_value=None)


# Date and time fields
DateTimeField(format=api_settings.DATETIME_FORMAT, 
	input_formats=None, default_timezone=None)
DateField(format=api_settings.DATE_FORMAT, input_formats=None)
TimeField(format=api_settings.TIME_FORMAT, input_formats=None)
DurationField(max_value=None, min_value=None)


# Choice selection fields
ChoiceField(choices)
MultipleChoiceField(choices)


# File upload fields
FileField(max_length=None, allow_empty_file=False, 
	use_url=UPLOADED_FILES_USE_URL)
ImageField(max_length=None, allow_empty_file=False, 
	use_url=UPLOADED_FILES_USE_URL)
```


</b>


Please note, that the fields' inputs may change over time, 
and there are also many details in the fields.  
So when you need any information about fields, you can 
always check the usage in the formal documentation of Fields.

