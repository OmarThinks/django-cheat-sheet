# 10) Filtering:






# 1) Current User:
<b>

```python
from myapp.models import Purchase
from myapp.serializers import PurchaseSerializer
from rest_framework import generics

class PurchaseList(generics.ListAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        user = self.request.user
        return Purchase.objects.filter(purchaser=user)
```
</b>





# 2) URL:
<b>

`urls.py`
```python
re_path('^purchases/(?P<username>.+)/$', PurchaseList.as_view()),
```
```python
class PurchaseList(generics.ListAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Purchase.objects.filter(purchaser__username=username)
```
</b>







# 3) Query Paramters:
<b>


```python
class PurchaseList(generics.ListAPIView):
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        queryset = Purchase.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(purchaser__username=username)
        return queryset
```
</b>







