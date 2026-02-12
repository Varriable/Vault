from ..apps.secret.models import Secret

def get_secret_by_id(secret_id: int) -> Secret:
    try: 
        return Secret.objects.get(id=secret_id) 
    except Secret.DoesNotExist: 
        return None
    
def get_all_secrets() -> list[Secret]:
    return list(Secret.objects.all())

def get_secrets_by_user_id(user_id: int) -> list[Secret]:
    return list(Secret.objects.filter(user_id=user_id))
