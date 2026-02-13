from apps.log.models import Log

class LogService:
    @staticmethod
    def create_log(user, action: str) -> Log:
        log = Log.objects.create(user=user, action=action)
        return log
    
    @staticmethod
    def get_user_logs(user) -> list[Log]:
        logs = Log.objects.filter(user=user) 
        return logs
    
    @staticmethod
    def get_log_by_id(log_id: int) -> Log: 
        try: 
            log = Log.objects.get(id=log_id)
            return log
        except Log.DoesNotExist:
            raise ValueError("Log not found")
        
    @staticmethod
    def delete_log(log_id: int) -> None:
        try: 
            log = Log.objects.get(id=log_id) 
            log.delete()
        except Log.DoesNotExist: 
            raise ValueError("Log not found")
        
    @staticmethod
    def clear_user_logs(user) -> None:
        Log.objects.filter(user=user).delete()

    @staticmethod
    def get_all_logs() -> list[Log]:
        logs = Log.objects.all() 
        return logs
    
    @staticmethod
    def get_logs_by_action(action: str) -> list[Log]:
        logs = Log.objects.filter(action=action) 
        return logs
