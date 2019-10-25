import functools
from colorama import Fore

def Debug(func):
    ''' @Debug Decorator '''
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(Fore.CYAN + f'Calling {func.__name__}({signature})' + Fore.RESET)
        value = func(*args, **kwargs)
        print(Fore.CYAN + f'{func.__name__!r} returned {value!r}' + Fore.RESET)
        return value
    return wrapper_debug
