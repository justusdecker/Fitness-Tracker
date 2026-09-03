from functools import wraps

def notImplementedYet(msg: str = ''):
    """
    Decorator: Wirft NotImplementedError im DEBUG-Modus.
    """
    def decorator(func):
        @wraps(func)
        def execute(*args, **kwargs):
            raise NotImplementedError(msg or f"Fucttion '{func.__name__}' is not implemented.")
        return execute
    return decorator
