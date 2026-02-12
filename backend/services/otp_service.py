from ..apps.secret.models import Otp
from ..utils.email import send_otp_email

class OtpService:
    @staticmethod
    def create_otp(user, secret) -> Otp:
        code = Otp.generate_code()
        otp = Otp.objects.create(user=user, secret=secret, code=code)
        return otp
        
    @staticmethod
    def get_user_otps(user) -> list[Otp]:
        otps = Otp.objects.filter(user=user) 
        return otps
    
    @staticmethod
    def get_otp_by_id(otp_id: int) -> Otp: 
        try: 
            otp = Otp.objects.get(id=otp_id)
            return otp
        except Otp.DoesNotExist:
            raise ValueError("OTP not found")
        
    @staticmethod
    def email_otp(user_email: str, otp_code: int) -> str:
        send_otp_email(user_email, otp_code)

    @staticmethod
    def validate_otp(user, code: int, secret=None) -> bool:
        try:
            if secret:
                otp = Otp.objects.get(user=user, code=code, secret=secret)
            else:
                otp = Otp.objects.get(user=user, code=code)
            return True
        except Otp.DoesNotExist:
            return False
