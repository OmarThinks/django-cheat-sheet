# 4) Views:


## 1) APIView:

### 1-1) APIView class:


<b>

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
```

</b>



### 1-2) APIView methods of request method:


The **`APIView`** will contain the methods that will handle the
request by type:

- **`get`**
- **`post`**
- ect.


The `get` method will handle the request method of `get` when 
it is being sent to the server.  
The same thing with the `post` method.





### 1-3) APIView attributes:

- **`authentication_classes`**
- **`permission_classes`**
- **`throttle_classes`**
- **`renderer_classes`**
- **`parser_classes`**
- **`content_negotiation_class`**



In these attributes, you can set the values of how to 
authenticate all the endpoints of this view, how to throttle, ect.











### 1-4) Dispatch methods:


These methods will be executed before or after the 
response of the endpoint.


- **`initial(self, request, *args, **kwargs)`**
	- used to enforce permissions and throttling, and 
	perform content negotiation.
- **`handle_exception(self, exc)`**
- **`handle_exception(self, exc)`**
- **`initialize_request(self, request, *args, **kwargs)`**
- **`finalize_response(self, request, response, *args, **kwargs)`**


































## 1) APIView:





### 1-2) APIView Signature:

<b>

```python
@api_view(http_method_names=['GET'])
```

</b>

The **default request method** for this endpoint is **`GET`**.  
You can add any request methods for the same endpoint.










### 1-2) Example:


<b>

```python
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})
```

</b>

This view will **use the default** renderers, parsers, 
authentication classes etc specified in the settings.













