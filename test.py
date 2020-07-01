import sys
from colorama import init, AnsiToWin32, Back, Fore
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
message = "xin chao cac ban"
print(f"{Fore.RESET}[ {Fore.RED}ERROR{Fore.RESET} ] Exiting the shell. \n\t[\033[033m Err \033[00m: {message} ]")
print(Fore.BLUE + 'blue text on stderr' + Fore.RESET, file=stream)
print('\033[31m' + 'some red text')
