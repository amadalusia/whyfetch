from typing import Callable, NamedTuple
import getpass as gp
import socket as sk
import platform as pl
import psutil as ps
import shellingham as sh
import locale as lc
import datetime as dt
import time as tm
import os

ures: pl.uname_result = pl.uname()
sys: str = pl.system()

class Data:
    def __init__(self) -> None:
        self.username: str = gp.getuser()
        self.hostname: str = sk.gethostname()
        self.kernel: str = f"{ures.system} {ures.release} {ures.machine}"
        self.os: str = self.get_os()
        self.shell: str = self.get_shell()
        self.ram: str = self.get_ram()
        self.uptime: str = self.get_uptime()
        self.locale: str = lc.setlocale(lc.LC_CTYPE)
        pass
    
    def get_os(self) -> str:
        if "Linux" == ures.system:
            linux_res: dict[str, str] = pl.freedesktop_os_release()
            return linux_res['PRETTY_NAME']

        if [ "FreeBSD", "OpenBSD", "NetBSD" ] not in [ ures.system ]:
            return ures.system

        if sys == "Darwin":
            mac_res: tuple[str, tuple[str, str, str], str] = pl.mac_ver()
            mac_release: str = mac_res[0]
            mac_version: str = mac_res[1][0]
            return f"{mac_release} {mac_version}"

        if sys == "Windows":
            win_res: tuple[str, str, str, str] = pl.win32_ver()
            win_edition: str = pl.win32_edition()
            win_release: str = win_res[0]
            win_ver: str = win_res[1]
            return f"{win_release} {win_edition} {win_ver}"
        
        raise ValueError("Unknown operating system. %r" % sys)

    def get_shell(self) -> str:
        try:
            shell_info = sh.detect_shell()
            shell: str = shell_info[0]
        except sh.ShellDetectionFailure:
            shell: str = provide_default_shell()
    
        return shell

    def get_ram(self) -> str:
        to_gb: Callable[[int], float] = lambda s: s / (1024 ** 3)
        vm: NamedTuple = ps.virtual_memory()
        total: float = to_gb(vm.total)
        used: float = to_gb(vm.used)
        percent: int = int(vm.percent)
        return f"{used:.1f}GB / {total:.1f}GB ({percent}%)"

    def get_uptime(self) -> str:
        current_uptime: tm.struct_time = tm.gmtime(tm.time() - ps.boot_time())
        return tm.strftime("%H hours, %M minutes, %S seconds", current_uptime)

def provide_default_shell() -> str:
    if os.name == 'nt':
        return os.environ['COMSPEC']
    elif os.name == 'posix':
        return os.environ['SHELL']
    raise NotImplementedError(f'OS {os.name!r} support not available')
