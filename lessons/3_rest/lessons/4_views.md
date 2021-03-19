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

1. **`get`**
2. **`post`**
3. ect.


The `get` method will handle the request method of `get` when 
it is being sent to the server.  
The same thing with the `post` method.





### 1-3) APIView attributes:





