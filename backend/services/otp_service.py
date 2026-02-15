from datetime import timedelta
from django.utils import timezone
import random
from apps.secret.models import Otp
from .user_service import UserService

from utils.exceptions import ObjectNotFoundException, OtpException
from utils.email import send_otp_email



class OtpService:    
    @staticmethod
    def generate_code() -> str:
        return f"{random.randint(100000, 999999):06d}"

    @staticmethod
    def create_otp(user, secret=None) -> Otp:
        if isinstance(user, int):
            userObj = UserService.get_user(user)
        else:
            userObj = user
        code = OtpService.generate_code()
        otp = Otp.objects.create(user=userObj, secret=secret, code=code)
        return otp

    @staticmethod
    def get_otp_by_id(otp_id: int) -> Otp: 
        try: 
            otp = Otp.objects.get(id=otp_id)
        except Otp.DoesNotExist: raise ObjectNotFoundException("OTP not found")
        return otp

    
    @staticmethod
    def email_otp(user, secret=None) -> str:
        otp = OtpService.create_otp(user, secret)
        if isinstance(user, int):
            userObj = UserService.get_user(user)
        else:
            userObj = user
        return send_otp_email(userObj.email, otp.code)

    @staticmethod
    def validate_otp(user, code: str, secret=None) -> bool:

        if isinstance(user, int):
            userObj = UserService.get_user(user)
        else:
            userObj = user
        code_str = str(code)
        try:
            if secret:
                otp = Otp.objects.get(user=userObj, code=code_str, secret=secret)
            else:
                otp = Otp.objects.get(user=userObj, code=code_str)
        except Otp.DoesNotExist: raise ObjectNotFoundException("OTP is invalid")
        if otp.created_at < timezone.now() - timedelta(minutes=5):
            raise OtpException("OTP has expired")
        return True
        

    #admin method    
    @staticmethod
    def get_user_otps(user) -> list[Otp]:
        if isinstance(user, int):
            userObj = UserService.get_user(user)
        else:
            userObj = user
        otps = Otp.objects.filter(user=userObj)
        return otps
    
   
