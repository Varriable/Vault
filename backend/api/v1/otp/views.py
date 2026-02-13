from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status, APIView
from rest_framework.response import Response
from .serializers import OtpSerializer
from services.otp_service import OtpService
from services.user_service import UserService
from services.secret_service import SecretService
otpService = OtpService()
userService = UserService()
secretService = SecretService()

   
class OtpApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OtpSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            user = userService.get_user(user_id)
            secret_id = serializer.validated_data['secret_id']
            secret = secretService.get_secret_by_id(secret_id) if secret_id else None
            otpService.email_otp(user, secret, self)
            return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VerifyOtpApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_id = request.data.get('user_id')
        code = request.data.get('code')
        secret_id = request.data.get('secret_id', None)

        if not user_id or not code:
            return Response({"error": "user_id and code are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = userService.get_user(user_id)
        secret = secretService.get_secret_by_id(secret_id) if secret_id else None
        is_valid = otpService.validate_otp(user, code, secret)

        if is_valid:
            return Response({"message": "OTP is valid"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "OTP is invalid"}, status=status.HTTP_400_BAD_REQUEST)