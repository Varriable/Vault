from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import LogSerializer
from ....apps.log.models import Log
from ....services.log_service import LogService
from ....services.user_service import UserService
logService = LogService()
userService = UserService()

class LogListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            user_id=serializer.validated_data['user_id']
            user = userService.get_user(user_id)
            logService.create_log(
                user=user,
                action=serializer.validated_data['action']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLogsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = userService.get_user(user_id)
        logs = logService.get_user_logs(user)
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LogDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, log_id):
        try:
            log = logService.get_log_by_id(log_id)
            serializer = LogSerializer(log)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

class LogDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, log_id):
        try:
            logService.delete_log(log_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        
class ClearUserLogsView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, user_id):
        user = userService.get_user(user_id)
        logService.clear_user_logs(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AllLogsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logs = logService.get_all_logs()
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class LogsByActionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, action):
        logs = logService.get_logs_by_action(action)
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)