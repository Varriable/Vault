from apps.secret.models import Secret

from utils.exceptions import ObjectNotFoundException

class SecretService:
    @staticmethod
    def create_secret(user, title: str, key: str) -> Secret:
        secret = Secret.objects.create(user=user, title=title, key=key)
        return secret
    
    @staticmethod
    def edit_secret(secret_id: int, title: str = None, key: str = None) -> Secret:
        try:
            secret = Secret.objects.get(id=secret_id)
        except Secret.DoesNotExist: raise ObjectNotFoundException("Secret not found")
        if title: secret.title = title 
        if key: secret.key = key 
        secret.save() 
        return secret 
    
    @staticmethod
    def delete_secret(secret_id: int) -> None:
        try: 
            secret = Secret.objects.get(id=secret_id)
        except Secret.DoesNotExist: raise ObjectNotFoundException("Secret not found") 
        secret.delete()
        
    @staticmethod
    def get_user_secrets(user_id: int) -> list[Secret]:
        secrets = Secret.objects.filter(user_id=user_id) 
        return secrets
    
    @staticmethod
    def get_secret_by_id(secret_id: int) -> Secret: 
        try: 
            secret = Secret.objects.get(id=secret_id)
        except Secret.DoesNotExist: raise ObjectNotFoundException("Secret not found")
        return secret


    #admin method   
    @staticmethod
    def get_all_secrets() -> list[Secret]:
        secrets = Secret.objects.all() 
        return secrets
    

