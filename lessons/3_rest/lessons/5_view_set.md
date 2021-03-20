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

class HelloViewSet(viewsets.ViewSet):
    """
    Hello, World!

    """
    def hello1(self, request):
        return Response({"message": "Hello1!"})

    def hello2(self, request):
        return Response({"message": "Hello!"})


hello1ViewSet = HelloViewSet.as_view({'get': 'hello1'})
hello2ViewSet = HelloViewSet.as_view({'get': 'hello2'})
```





`urls.py`
```python
from .views import (hello1ViewSet,hello2ViewSet)

urlpatterns = [
	... ,
    path('hello1ViewSet/', hello1ViewSet),
    path('hello2ViewSet/', hello2ViewSet),

]
```

</b>


















































