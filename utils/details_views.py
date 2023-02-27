from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404

from users.models import User

class GetDetailView(APIView):
    def retrieve(self, request: Request, pk) -> Response:
        queryset = get_object_or_404(self.view_queryset, pk=pk)
        
        serializer = self.serializer(queryset)
        
        return Response(serializer.data, status.HTTP_201_CREATED)

class PatchDetailView(APIView):
    def update(self, request: Request, pk) -> Response:
        queryset = get_object_or_404(self.view_queryset, pk=pk)
        
        serializer = self.serializer(queryset, request.data, partial=True)
        
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    
#     from rest_framework.views import APIView, Request, Response, status
# from django.shortcuts import get_object_or_404

# from users.models import User

# class GetDetailView:
#     def retrieve(self, request: Request, pk: int) -> Response:
#         queryset = get_object_or_404(self.view_queryset, pk=pk)
        
#         serializer = self.view_serializer(queryset)
        
#         return Response(serializer.data, status.HTTP_201_CREATED)

# class PatchDetailView:
#     def update(self, request: Request, pk: int) -> Response:
#         queryset = get_object_or_404(self.view_queryset, pk=pk)
        
#         serializer = self.serializer(queryset, request.data, partial=True)
        
#         serializer.is_valid(raise_exception=True)
        
#         serializer.save()
        
#         return Response(serializer.data, status.HTTP_201_CREATED)

# class DeleteDetailView:
#     def destroy(self, request: Request, pk: int) -> Response:
#         queryset = get_object_or_404(self.view_queryset, pk=pk)
        
#         queryset.delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class OnlyGetDetailView(GetDetailView, APIView):
#     def get(self, request: Request, pk: int) -> Response:
#         return super().retrieve(request, pk)

# class OnlyPatchDetailView(PatchDetailView, APIView):
#     def patch(self, request: Request, pk: int) -> Response:
#         return super().update(request, pk)

# class OnlyDeleteDetailView(DeleteDetailView, APIView):
#     def delete(self, request: Request, pk: int) -> Response:
#         return super().destroy(request, pk)