from ..apps.log.models import Log

def get_log_by_id(log_id: int) -> Log:
    try: 
        return Log.objects.get(id=log_id) 
    except Log.DoesNotExist: 
        return None

def get_all_logs() -> list[Log]:
    return list(Log.objects.all())

def get_logs_by_user_id(user_id: int) -> list[Log]:
    return list(Log.objects.filter(user_id=user_id))

def get_logs_by_action(action: str) -> list[Log]: 
    return list(Log.objects.filter(action=action))
