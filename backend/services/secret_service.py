from ..apps.secret.models import Secret

class SecretService:
    @staticmethod
    def create_secret(user, title: str, key: str) -> Secret:
        secret = Secret.objects.create(user=user, title=title, key=key)
        return secret
    
    @staticmethod
    def edit_secret(secret_id: int, title: str = None, key: str = None) -> Secret:
        try:
            secret = Secret.objects.get(id=secret_id)
            if title: secret.title = title 
            if key: secret.key = key 
            secret.save() 
            return secret 
        except Secret.DoesNotExist: 
            raise ValueError("Secret not found")
    
    @staticmethod
    def delete_secret(secret_id: int) -> None:
        try: 
            secret = Secret.objects.get(id=secret_id) 
            secret.delete()
        except Secret.DoesNotExist: 
            raise ValueError("Secret not found")
        
    @staticmethod
    def get_user_secrets(user_id: int) -> list[Secret]:
        secrets = Secret.objects.filter(user_id=user_id) 
        return secrets
    
    @staticmethod
    def get_secret_by_id(secret_id: int) -> Secret: 
        try: 
            secret = Secret.objects.get(id=secret_id)
            return secret
        except Secret.DoesNotExist:
            raise ValueError("Secret not found")
        
    @staticmethod
    def get_all_secrets() -> list[Secret]:
        secrets = Secret.objects.all() 
        return secrets
    
    @staticmethod
    def get_secrets_by_user_id(user_id: int) -> list[Secret]:
        secrets = Secret.objects.filter(user_id=user_id) 
        return secrets
