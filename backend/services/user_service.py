from apps.user.models import User
from utils.exceptions import EmailAlreadyExistsException, ObjectNotFoundException

class UserService:
    @staticmethod
    def create_user(name: str, email: str, password: str) -> User:
        if User.objects.filter(email=email).exists():
            raise EmailAlreadyExistsException("Email already exists")
        user = User.objects.create_user(name = name , email=email, password=password) 
        return user
    
    @staticmethod
    def edit_user(user_id: int, name: str = None, email: str = None, password: str = None) -> User:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist: raise ObjectNotFoundException("User not found")
        if email: user.email = email 
        if password: user.set_password(password) 
        if name: user.name = name
        user.save() 
        return user 
    

    @staticmethod
    def delete_user(user_id: int) -> None:
        try: 
            user = User.objects.get(id=user_id)
        except User.DoesNotExist: raise ObjectNotFoundException("User not found") 
        user.is_active = False
        user.save()
    
    # Admin Methods
    @staticmethod
    def get_user(user_id: int) -> User:
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist: raise ObjectNotFoundException("User not found")
        
    @staticmethod
    def get_all_users() -> list[User]:
        return User.objects.filter(is_active=True)