# 9) Throttling:


# 1) Throttling policy:


## 1-1) Using settings.py:

Here you will set the default throttling policy.


<b>

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}
```
</b>

The rate descriptions used in `DEFAULT_THROTTLE_RATES` may 
include **`second`**, **`minute`**, **`hour`** or **`day`** 
as the throttle period.





## 1-2) Using `APIView`:

<b>

```python
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

class ExampleView(APIView):
    throttle_classes = [UserRateThrottle]
    ...
```
</b>


## 1-3) Using `@api_view`:

<b>

```python
@api_view(['GET'])
@throttle_classes([UserRateThrottle])
def example_view(request, format=None):
    ...
```
</b>

































# 2) AnonRateThrottle:
For ananymous users.

The **`AnonRateThrottle`** will only ever throttle unauthenticated users. The IP address of the incoming request is used to generate a unique key to throttle against.


# 3) UserRateThrottle:
For regestered users. 
































































