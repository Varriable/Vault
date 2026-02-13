from ..apps.user.models import User

class UserService:
    @staticmethod
    def create_user(email: str, password: str) -> User:
        user = User.objects.create_user(email=email, password=password) 
        return user
    
    @staticmethod
    def edit_user(user_id: int, email: str = None, password: str = None) -> User:
        try:
            user = User.objects.get(id=user_id)
            if email: user.email = email 
            if password: user.set_password(password) 
            user.save() 
            return user 
        except User.DoesNotExist: 
            raise ValueError("User not found")
    

    @staticmethod
    def delete_user(user_id: int) -> None:
        try: 
            user = User.objects.get(id=user_id) 
            user.is_active = False
            user.save()
        except User.DoesNotExist: 
            raise ValueError("User not found")
        
    @staticmethod
    def get_user(user_id: int) -> User:
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValueError("User not found")
        
    @staticmethod
    def get_all_users() -> list[User]:
        return User.objects.filter(is_active=True)