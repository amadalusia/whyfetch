from whyfetch.data import Data


def separator_from_longest_prop(props: list[str]):
    j: int = 0

    for i in props:
        if len(i) > j:
            j = len(i)
            continue
        else:
            continue

    return "━" * j


class Colours:
    red: str = "\x1b[1;31m"
    blue: str = "\x1b[1;34m"
    white: str = "\x1b[1;39m"
    magenta: str = "\x1b[1;35m"


def __main__():
    d: Data = Data()

    props: list[str] = [
        f"{d.username}@{d.hostname}",
        f"kernel: {d.kernel}",
        f"os:     {d.os}",
        f"shell:  {d.shell}",
        f"ram:    {d.ram}",
        f"up:     {d.uptime}",
        f"locale: {d.locale}",
    ]

    separator: str = separator_from_longest_prop(props)

    print(f"{Colours.white}━━━━━━━━━━━━━━━{separator}")
    print(
        f"   {Colours.red}_.----._{Colours.white}    {Colours.magenta}{d.username}{Colours.white}@{Colours.magenta}{d.hostname}"
    )
    print(
        f" {Colours.red}.'        '.{Colours.white}  {Colours.magenta}kernel:{Colours.white} {d.kernel}"
    )
    print(
        f"{Colours.red}/{Colours.white}._   _.--._ {Colours.red}\\{Colours.white} {Colours.magenta}os:{Colours.white}     {d.os}"
    )
    print(f"|_ '-' _.._ `| {Colours.magenta}shell:{Colours.white}  {d.shell}")
    print(
        f"{Colours.blue}\\{Colours.white} `---'    `-{Colours.blue}/{Colours.white} {Colours.magenta}ram:{Colours.white}    {d.ram}"
    )
    print(
        f" {Colours.blue}'._      _.'{Colours.white}  {Colours.magenta}up:{Colours.white}     {d.uptime}"
    )
    print(
        f"    {Colours.blue}'----'{Colours.white}     {Colours.magenta}locale:{Colours.white} {d.locale}"
    )
    print(f"━━━━━━━━━━━━━━━{separator}")
