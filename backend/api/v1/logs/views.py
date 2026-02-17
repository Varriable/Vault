from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.views import APIView

from utils.exceptions import ObjectNotFoundException
from .serializers import LogSerializer
from apps.log.models import Log
from services.log_service import LogService
from services.user_service import UserService
logService = LogService()
userService = UserService()

class LogCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user_id=serializer.validated_data['user_id']
            user = userService.get_user(user_id)
            logService.create_log(
                user=user,
                action=serializer.validated_data['action']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class UserLogsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.data.get('user_id') if request.data.get('user_id') else request.user.id
        logs = logService.get_user_logs(user_id)
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LogDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            log_id = request.data.get('log_id')
            log = logService.get_log_by_id(log_id)
            serializer = LogSerializer(log)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectNotFoundException as e:
            return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)

class LogDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        try:
            log_id = request.data.get('log_id')
            logService.delete_log(log_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectNotFoundException as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        
class ClearUserLogsView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user_id = request.data.get('user_id') if request.data.get('user_id') else request.user.id
        logService.clear_user_logs(user_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AllLogsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logs = logService.get_all_logs()
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class LogsByActionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        action = request.data.get('action')
        logs = logService.get_logs_by_action(action)
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)