def Debug(func):
    ''' @Debug Decorator '''
    from functools import wraps
    from colorama import Fore
    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(Fore.CYAN + f'Calling {func.__name__}({signature})' + Fore.RESET)
        value = func(*args, **kwargs)
        print(Fore.CYAN + f'{func.__name__!r} returned {value!r}' + Fore.RESET)
        return value
    return wrapper_debug

def header(text=""):
    width = 40
    top_dressing = '='
    bot_dressing = '='
    left_dressing = '||'
    right_dressing = '||'

    left_spacer = " "
    right_spacer = " "

    left_spacing = int((width - len(text))/2) - len(left_dressing)
    right_spacing = int((width - len(text))/2) + ((width - len(text))%2) - len(right_dressing)

    head = ""
    head += (top_dressing * width) + '\n'
    head += left_dressing + left_spacer * left_spacing + text + right_spacer * right_spacing + right_dressing + '\n'
    head += (bot_dressing * width) + '\n'
    return head

def checkdir(dir, new_folder):
    from os.path import join, isdir
    from os import mkdir
    ### Usage: checkdir('/mnt/drive/FOLDER', 'New Folder')
    ### Checks the dir for a particular folder and if it does not exist, create it
    folder = join(dir, new_folder)
    try:
        if not isdir(folder):
            mkdir(folder)
            return True
    except:
        return False

def checkcommand(command):
    from subprocess import run, DEVNULL
    if command == 'ffmpeg':
        cmd = ['ffmpeg', '-version', '-loglevel quiet']
    else:
        cmd = [command, '--version']
    ret = run(cmd, stdout=DEVNULL, stderr=DEVNULL, stdin=DEVNULL)
    return ret
