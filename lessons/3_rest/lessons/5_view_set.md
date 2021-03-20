# 5) ViewSet:

## 1) What is ViewSet:

Using **`ViewSet`** lets you write all the logic that is related
 to each other in one class, then reuse it how you want.



## 2) Example:

<b>

`views.py`
```python
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class HelloViewSet(viewsets.ViewSet):
    """
    Hello, World!

    """
    def h1(self, request):
        return Response({"message": "Hello1, 1!"})

    def h2(self, request):
        return Response({"message": "Hello, 2!"})

    @action(detail = False, authentication_classes=[])
    def h3(self, request):
        return Response({"message": "Hello, 3!"})

h1 = HelloViewSet.as_view({'get': 'h1'})
h2 = HelloViewSet.as_view({'get': 'h2', 'post': 'h3'})
```





`urls.py`
```python
from .views import (h1,h2)

urlpatterns = [
    ... ,
    path('h1/', h1),
    path('h2/', h2),
]
```

</b>















## 3) `@action`:



With **`@action`** decorator you can specify a speific request 
for this endpoint, you can also add some auth.  

### `@action` arguments:



- **`detail`**:
    - **required**
    - a boolean telling whther this should return detailed 
        or a list of data
- **`methods`**:
    - **optional**, default = **`["get"]`**
    - a list of the methods of this endpoint


  
  
  
- **`renderer_classes`**:
    - **optional**
- **`parser_classes`**:
    - **optional**
- **`authentication_classes`**:
    - **optional**
- **`throttle_classes`**:
    - **optional**
- **`permission_classes`**:
    - **optional**
- **`content_negotiation_class`**:
    - **optional**






























































