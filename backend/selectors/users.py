from ..apps.user.models import User

def get_user_by_id(user_id: int) -> User:
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None
    
def get_user_by_email(email: str) -> User:
    try:
        return User.objects.get(email=email) 
    except User.DoesNotExist: 
        return None

def get_all_users() -> list[User]:
    return list(User.objects.all())

