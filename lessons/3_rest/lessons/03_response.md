# 3) Responses:

## 1) Signature:

<b>

```python
from rest_framework.response import Response

#Singnature
Response(data, status=None, template_name=None, headers=None, content_type=None)
```

</b>



## 2) Arguments:


### **`data`** : The serialized data for the response.
### **`status`** : A status code for the response.
### **`template_name`** : A template name to use 
if `HTMLRenderer` is selected.
### **`headers`** : A dictionary of HTTP headers to use in the response.
### **`content_type`** : The content type of the response.






















