from rest_framework.views import APIView, Request, Response, status

class PostView(APIView):
    def post(self, request: Request) -> Response:
        serializer = self.serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)