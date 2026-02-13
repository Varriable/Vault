from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import SecretSerializer
from services.secret_service import SecretService
secretService = SecretService()

class SecretCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SecretSerializer(data=request.data)
        if serializer.is_valid():
            secret_data = serializer.validated_data
            secret = secretService.create_secret(request.user, secret_data['title'], secret_data['key'])
        return Response({"message": "Secret created successfully", "secret": secret}, status=status.HTTP_201_CREATED)
    
class SecretEditView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, secret_id):
        serializer = SecretSerializer(data=request.data)
        if serializer.is_valid():
            secret_data = serializer.validated_data
            try:
                secret = secretService.edit_secret(secret_id, secret_data.get('title'), secret_data.get('key'))
                return Response({"message": "Secret updated successfully", "secret": secret}, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SecretDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, secret_id):
        try:
            secretService.delete_secret(secret_id)
            return Response({"message": "Secret deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
class UserSecretsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        secrets = secretService.get_user_secrets(request.user.id)
        return Response(SecretSerializer(secrets, many=True).data, status=status.HTTP_200_OK)
    
class SecretDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, secret_id):
        try:
            secret = secretService.get_secret_by_id(secret_id)
            return Response(SecretSerializer(secret).data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
class SecretListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        secrets = secretService.get_all_secrets()
        return Response(SecretSerializer(secrets, many=True).data, status=status.HTTP_200_OK)
    
class SecretsByUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        secrets = secretService.get_secrets_by_user_id(user_id)
        return Response(SecretSerializer(secrets, many=True).data, status=status.HTTP_200_OK)