import whyfetch.system_properties as w

colours = {
    "red": "\x1b[1;31m",
    "blue": "\x1b[1;34m",
    "white": "\x1b[1;39m",
}

def separator_from_longest_prop(properties: list[w.Prop]):
    j: int = 0
    
    for i in properties:
        if i.length > j:
            j = i.length
            continue
        else:
            continue

    return "━"*j

def __main__():
    kernel: w.Kernel = w.Kernel()
    ram: w.Ram = w.Ram()
    username: w.Username = w.Username()
    os: w.Os = w.Os()
    shell: w.Shell = w.Shell()
    uptime: w.Uptime = w.Uptime()
    locale: w.Locale = w.Locale()

    properties: list[w.Prop] = [ kernel.prop, ram.prop, username.prop, os.prop, uptime.prop, locale.prop ]

    print(f'{colours["white"]}━━━━━━━━━━━━━━━{separator_from_longest_prop(properties)}')
    print(f'   {colours["red"]}_.----._{colours["white"]}    {username.prop.content}@{kernel.node}')
    print(f' {colours["red"]}.\'        \'.{colours["white"]} {kernel.prop.content}')
    print(f'{colours["red"]}/{colours["white"]}._   _.--._ {colours["red"]}}\\ {os.prop.content}')
    print(f'|_ \'-\' _.._ `| {shell.prop.content}')
    print(f'\\ `---\'    `-/ {ram.prop.content}')
    print(f' \'._      _.\'  {uptime.prop.content}')
    print(f'    \'----\'     {locale.prop.content}')
    print(f'━━━━━━━━━━━━━━━{separator_from_longest_prop(properties)}')




