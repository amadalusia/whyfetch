import platform
import psutil
import os
from sys import platform as platform2
import csv
import pathlib
import shellingham as shelling
import time
import locale

uname = platform.uname()
svmem = psutil.virtual_memory()
b_to_mb = lambda s : int(s / pow(1024, 2))


class Prop:
    def __init__(self, content) -> None:
        self.content = content
        self.length = len(self.content)
        pass

class Kernel:
    def __init__(self) -> None:
        self.system: str = uname.system
        self.release: str = uname.release
        self.machine: str = uname.machine
        self.node: str = uname.node
        self.prop: Prop = Prop(f"kernel: {self.system} {self.release} {self.machine}")
        pass

class Ram:
    def __init__(self) -> None:
        self.total: int = svmem.total
        self.used: int = svmem.used
        self.available = svmem.available
        self.prop: Prop = Prop(self.format())
        pass
        
    def format(self) -> str:
        total_in_gb: int = b_to_mb(self.total)
        used_in_gb: int = b_to_mb(self.used)
        available_in_gb: int = b_to_mb(self.available)
        
        return f"ram: {used_in_gb}MB/{total_in_gb}MB ({available_in_gb}MB free)"

class Username:
    def __init__(self) -> None:
        content: str = self.get_username()
        self.prop: Prop = Prop(content)
        pass
    
    def get_username(self) -> str:
        username: str = ""
        
        user_home: str = os.path.expanduser('~')
        if platform2 == "win32":
            username = user_home.split("\\")[-1]
        else:
            username = user_home.split("/")[-1]

        return username

class Os:
    def __init__(self) -> None:
        content: str = self.get_os_pretty_name()
        self.prop: Prop = Prop(content)
        pass
    def get_os_pretty_name(self) -> str:
        path = pathlib.Path("/etc/os-release")
        with open(path) as stream:
            reader = csv.reader(stream, delimiter="=")
            os_release = dict(reader)

        return f"os: {os_release['PRETTY_NAME']}"

class Shell:
    def __init__(self) -> None:
        content: str = self.get_shell()
        self.prop: Prop = Prop(content)
        pass
    
    def get_shell(self) -> str:
        try:
            shell = shelling.detect_shell()
        except shelling.shellDetectionFailure:
            shell = self.provide_default()

        return f"shell: {shell[0]}"
    
    def provide_default():
        if os.name == 'posix':
            return os.environ['SHELL']
        elif os.name == 'nt':
            return os.environ['COMSPEC']
        raise NotImplementedError(f'OS {os.name!r} support not available')

class Uptime:
    def __init__(self) -> None:
        content: str = f"up: {self.get_uptime()}"
        self.prop = Prop(content)
        pass
    
    def get_uptime(self) -> str:
        seconds_elapsed = time.time() - psutil.boot_time()
        seconds: int = int(seconds_elapsed % 60)
        minutes: int  = int(seconds_elapsed / 60) % 60
        hours: int = int(seconds_elapsed / pow(60, 2))
        
        return f"{hours} hours, {minutes} minutes and {seconds} seconds"

class Locale:
    def __init__(self) -> None:
        content: str = f"locale: {locale.setlocale(locale.LC_CTYPE)}"
        self.prop: Prop = Prop(content)
        pass

