from colorama import just_fix_windows_console, Fore

def help(command_name:str) -> None:
	if command_name == "all":
		minus:str = f"{Fore.LIGHTYELLOW_EX}-{Fore.RESET}"
		def comment(content:str) -> str:
			return f"{Fore.LIGHTBLACK_EX}// {content}{Fore.RESET}"
		print()
		print(f"Spicer commands list")
		print()
		print(f"{minus} spicer help <command name> {comment('Provides information on a command')}")
		print()
		return
	return

def run(argc:int,argv:list[str]) -> None:
	just_fix_windows_console()
	if argc < 2:
		print()
		print("Welcome to the Spicer command-line utility!")
		print("If you need more information on a command or on")
		print(f"the tool itself, run {Fore.LIGHTYELLOW_EX}spicer help <command name>{Fore.RESET}.")
		print()
		print(f"If you want a list of commands, try {Fore.LIGHTYELLOW_EX}spicer help all{Fore.RESET}!")
		print()
		return
	if argv[1] == "help":
		if argc < 3:
			print()
			print(f"Nuh uh. You {Fore.LIGHTRED_EX}MUST{Fore.RESET} a {Fore.LIGHTYELLOW_EX}command name{Fore.RESET}!")
			print()
			return
		help(argv[2])
		return
	return None