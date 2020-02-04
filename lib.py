def Debug(func):
    """ @Debug Decorator """
    from functools import wraps
    from colorama import Fore

    ### Usage: @Debug
    ### A Debug decorator to debug any part of code on the fly
    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(Fore.CYAN + f"Calling {func.__name__}({signature})" + Fore.RESET)
        value = func(*args, **kwargs)
        print(Fore.CYAN + f"{func.__name__!r} returned {value!r}" + Fore.RESET)
        return value

    return wrapper_debug


def draw_header(text=""):
    ### Usage: print(header('HEADER NAME'))
    ### Returns a text block with the following config
    ### ==========
    ### ||  IE  ||
    ### ==========
    width = 40
    top_dressing = "="
    bot_dressing = "="
    left_dressing = "||"
    right_dressing = "||"

    left_spacer = " "
    right_spacer = " "

    left_spacing = int((width - len(text)) / 2) - len(left_dressing)
    right_spacing = (
        int((width - len(text)) / 2) + ((width - len(text)) % 2) - len(right_dressing)
    )

    head = ""
    head += (top_dressing * width) + "\n"
    head += (
        left_dressing
        + left_spacer * left_spacing
        + text
        + right_spacer * right_spacing
        + right_dressing
        + "\n"
    )
    head += (bot_dressing * width) + "\n"
    return head


def check_dir(dir, new_folder):
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


def check_command(command):
    ### Usage: if (checkcommand('ffmpeg')):
    ### Does a version check, calling the command without any output, returns True or False
    from subprocess import run, DEVNULL

    if command == "ffmpeg":
        cmd = ["ffmpeg", "-version", "-loglevel quiet"]
    else:
        cmd = [command, "--version"]
    ret = run(cmd, stdout=DEVNULL, stderr=DEVNULL, stdin=DEVNULL)
    return ret


def wait_for_http_callback(_port=9000, _host="127.0.0.1"):
    ### Usage: response = wait_for_http_callback(8080)
    ### Hosts a lightweight http server on a specified port and awaits 1 response before closing down and returning the response
    import cherrypy

    if _host == "localhost":
        _host = "127.0.0.1"

    cherrypy.config.update(
        {"server.socket_host": _host, "server.socket_port": _port, "log.screen": False}
    )

    class CallbackHandler(object):
        response = None

        @cherrypy.expose
        def index(self):
            request = cherrypy.serving.request
            self.response = cherrypy.url(qs=request.query_string)
            cherrypy.engine.exit()

    handle = CallbackHandler()
    cherrypy.quickstart(handle, "/callback", config={"/": {"log.screen": False}})
    return handle.response
