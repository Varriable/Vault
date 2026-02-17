from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import NotFound
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from utils.exceptions import EmailAlreadyExistsException, ObjectNotFoundException


from .serializers import UserSerializer
from services.user_service import UserService
user_service = UserService()


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            if not email or not password:
                raise ValueError("Email and password are required")
            user = authenticate(request, email=email, password=password)
            if user:
                response = Response(UserSerializer(user).data, status=status.HTTP_200_OK)
                refresh_token = RefreshToken.for_user(user)
                access_token = str(refresh_token.access_token)
                response.set_cookie(
                    key='access_token',
                    value=access_token,
                    httponly=True,
                    secure=False,
                    samesite='Lax',
                    max_age=15 * 60,  # 15 minutes
                )
                response.set_cookie(
                    key='refresh_token',
                    value=str(refresh_token),
                    httponly=True,
                    secure=False,
                    samesite='Lax',
                    max_age=24 * 60 * 60,  # 1 day
                )
                return response
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class RefreshView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return Response({"error": "Refresh token not provided"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            refresh = RefreshToken(refresh_token)
            new_access_token = str(refresh.access_token)
            response = Response({"access_token": new_access_token}, status=status.HTTP_200_OK)
            response.set_cookie(
                key='access_token',
                value=new_access_token,
                httponly=True,
                secure=False,
                samesite='Lax',
                max_age=15 * 60,  # 15 minutes
            )
            return response
        except Exception as e:
            return Response({"error": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        response = Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response

@permission_classes([AllowAny])  
class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try :
            user = user_service.create_user(**serializer.validated_data)
            return Response(UserSerializer(user).data, status=201)
        except EmailAlreadyExistsException as e:
            return Response({"message": str(e)}, status=400)

@permission_classes([IsAuthenticated])   
class UserEditView(APIView):
    def put(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = user_service.edit_user(**serializer.validated_data)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        except ObjectNotFoundException as e:
                return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)

@permission_classes([IsAuthenticated])
class UserDeleteView(APIView):
    def delete(self, request):
        try:
            user_id = request.data.get('user_id')
            user_service.delete_user(user_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectNotFoundException as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)

@permission_classes([IsAuthenticated])       
class UserListView(APIView):
    def get(self, request):
        users = user_service.get_all_users()
        return Response(UserSerializer(users, many=True).data, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])   
class MeView(APIView):
    def get(self, request):
        user_id = request.data.get('user_id')
        try:
            user = user_service.get_user(user_id)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        except NotFound as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)

@permission_classes([IsAuthenticated])
class UserDetailView(APIView):
    def get(self, request):
        try:
            user_id = request.data.get('user_id')
            user = user_service.get_user(user_id)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        except NotFound as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)