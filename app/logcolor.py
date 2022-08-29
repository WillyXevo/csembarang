import pyfiglet
import os, re
from colorama import Fore, Style, init
from datetime import datetime 
import time


init()

_color = {
    "BLACK":Fore.BLACK,
    "RED":Fore.RED,
    "GREEN":Fore.GREEN,
    "YELLOW":Fore.YELLOW,
    "BLUE":Fore.BLUE,
    "MAGENTA":Fore.MAGENTA,
    "CYAN":Fore.CYAN,
    "WHITE":Fore.WHITE,
    
    "SUCCESS":Fore.GREEN,
    "DANGER":Fore.RED,
    "ERROR":Fore.RED,
    "WARNING":Fore.YELLOW,
    "INFO":Fore.CYAN,
    "PRIMARY":Fore.BLUE,
    }
_style = {
    "NORMAL":Style.NORMAL,
    "DIM":Style.DIM,
    "BRIGHT":Style.BRIGHT,
    "RESET":Style.RESET_ALL
    }
    
def shlog(typ, msg):
    typ = typ.upper()
    warna = _color[typ] if typ in _color else _color["INFO"]
    gaya = Style.BRIGHT
    reset = Style.RESET_ALL
    tim = datetime.now()
    
    
    msg = f"[{tim}]{warna}[{typ}]{reset} {gaya}{msg}"
    if len(msg) > 100:
        msg = msg[0:99]
    
    msg = msg + "".join(" " for n in range(1, 100-len(msg)))
    
    print(f"{gaya}{msg}{reset}", end="\r")
   
def slog(typ, msg, t=0):
    typ = typ.upper()
    warna = _color[typ] if typ in _color else _color["INFO"]
    gaya = Style.BRIGHT
    reset = Style.RESET_ALL
    tim = datetime.now()
    pes = f"{gaya}{warna}[{typ}]{reset} {gaya}{msg}{reset}"
    if t==0:
        print(pes) 
    else:
        return pes
    
def pcolor(m, c="", s=""):    
    c = c.upper()
    s = s.upper()
    warna = _color[c] if c in _color else _color["WHITE"]
    gaya = _style[s] if s in _style else _style["NORMAL"]
    reset = Style.RESET_ALL
    print(f"{gaya}{warna}{m}{reset}")
    
def dline(c, num):
    ret = []
    for a in range(0,num):
        ret.append(c)
    
    return "".join(ret)
    


"""
shlog("success", "ini success")
shlog("error", "ini error")
shlog("warning", "ini warning")
shlog("get", "ini get")
"""