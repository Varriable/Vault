from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated


from .serializers import UserSerializer
from services.user_service import UserService
user_service = UserService()

@permission_classes([AllowAny])  
class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            user = user_service.create_user(user_data)
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])   
class UserEditView(APIView):
    def put(self, request, user_id):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            try:
                user = user_service.edit_user(user_id, user_data)
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
class UserDeleteView(APIView):
    def delete(self, request, user_id):
        try:
            user_service.delete_user(user_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

@permission_classes([IsAuthenticated])       
class UserListView(APIView):
    def get(self, request):
        users = user_service.get_all_users()
        return Response(UserSerializer(users, many=True).data, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])   
class MeView(APIView):
    def get(self, request):
        user = request.user
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
class UserDetailView(APIView):
    def get(self, request, user_id):
        try:
            user = user_service.get_user(user_id)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)