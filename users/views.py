from rest_framework.views import APIView, Request, Response, status

from utils.common_views import PostView
from utils.details_views import GetDetailView, PatchDetailView
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner


class UserView(PostView):
    queryset = User.objects.all()        
    serializer = UserSerializer


class UserDetailView(GetDetailView, PatchDetailView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()        
    serializer = UserSerializer

    def delete(self, request: Request, pk: int) -> Response:
        """
        Deleçao de usuário
        """
        user = get_object_or_404(User, pk=pk)

        self.check_object_permissions(request, user)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework.views import APIView, Request, Response, status

# from utils.common_views import PostView
# from .models import User
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from .serializers import UserSerializer
# from .permissions import IsAccountOwner
# from utils.details_views import OnlyDeleteDetailView, OnlyGetDetailView, OnlyPatchDetailView


# class UserView(PostView):
#     queryset = User.objects.all()        
#     serializer = UserSerializer


# class UserDetailView(OnlyGetDetailView, OnlyPatchDetailView, OnlyDeleteDetailView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAccountOwner]
    
#     view_queryset = User.objects.all()
#     view_serializer = UserSerializer
