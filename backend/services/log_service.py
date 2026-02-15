from apps.log.models import Log
from .user_service import UserService
from utils.exceptions import ObjectNotFoundException

class LogService:
    @staticmethod
    def create_log(user, action: str) -> Log:
        if isinstance(user, int):
            userObj = UserService.get_user(user)
        else:
            userObj = user
        log = Log.objects.create(user=userObj, action=action)
        return log
    
    @staticmethod
    def get_user_logs(user) -> list[Log]:
        if isinstance(user, int):
            userObj = UserService.get_user(user)
        else:
            userObj = user
        try:
            logs = Log.objects.filter(user=userObj)
        except Log.DoesNotExist: raise ObjectNotFoundException("No logs found for this user")

        return logs

    
    @staticmethod
    def get_log_by_id(log_id: int) -> Log: 
        try: 
            log = Log.objects.get(id=log_id)
            return log
        except Log.DoesNotExist:
            raise ObjectNotFoundException("Log not found")
        
    @staticmethod
    def delete_log(log_id: int) -> None:
        try: 
            log = Log.objects.get(id=log_id) 
            log.delete()
        except Log.DoesNotExist: 
            raise ObjectNotFoundException("Log not found")
        
    @staticmethod
    def clear_user_logs(user) -> None:
        if isinstance(user, int):
            userObj = UserService.get_user(user)
        else:
            userObj = user
        Log.objects.filter(user=userObj).delete()

    ##admin methods
    @staticmethod
    def get_all_logs() -> list[Log]:
        logs = Log.objects.all() 
        return logs
    
    @staticmethod
    def get_logs_by_action(action: str) -> list[Log]:
        logs = Log.objects.filter(action=action) 
        return logs
