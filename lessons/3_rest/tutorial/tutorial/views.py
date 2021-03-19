
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework import authentication, permissions
from django.contrib.auth.models import User





class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    #authentication_classes = []
    #permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)



"""

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)



"""







class hello_world1(APIView):
    def get(self, request, format=None):
        #usernames = [user.username for user in User.objects.all()]
        return Response({"message": "Hello, world!"})

@api_view(['GET', 'POST'])
def hello_world2(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", 
        	"data": request.data})
    return Response({"message": "Hello, world!"})
