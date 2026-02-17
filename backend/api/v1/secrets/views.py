from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from utils.exceptions import ObjectNotFoundException

from .serializers import SecretSerializer
from services.secret_service import SecretService
secretService = SecretService()

class SecretCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SecretSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            secret = secretService.create_secret(**serializer.validated_data, user=request.user)
            return Response({"message": "Secret created successfully", "secret": secret}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
    
class SecretEditView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = SecretSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            secret = secretService.edit_secret(**serializer.validated_data)
            return Response({"message": "Secret updated successfully", "secret": secret}, status=status.HTTP_200_OK)
        except ObjectNotFoundException as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
    
class SecretDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, secret_id):
        try:
            secretService.delete_secret(secret_id)
            return Response({"message": "Secret deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except ObjectNotFoundException as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
class UserSecretsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.data.get("user_id", request.user.id) 
        secrets = secretService.get_user_secrets(user_id)
        return Response(SecretSerializer(secrets, many=True).data, status=status.HTTP_200_OK)
    
class SecretDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            secret_id = request.data.get("secret_id")
            secret = secretService.get_secret_by_id(secret_id)
            return Response(SecretSerializer(secret).data, status=status.HTTP_200_OK)
        except ObjectNotFoundException as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
class SecretListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        secrets = secretService.get_all_secrets()
        return Response(SecretSerializer(secrets, many=True).data, status=status.HTTP_200_OK)
