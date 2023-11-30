from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import random
import time

colorama_init()

print(f"{Fore.GREEN}")

lines = 400      
line = "1 2 3 4 5 6 7 8 9 0 "
index_to_change = 0
new_character = "0"

while(lines > 0):
    lines = lines - 1
    print(line)
    line = line[:index_to_change] + new_character + line[index_to_change + 1:]      

    index_to_change = random.randint(0, 9) * 2
    new_character_int = random.randint(0, 20)
    new_character = chr(new_character_int + 48) #48 = 0x30 
    if(new_character_int > 9):
        new_character = " "
    time.sleep(0.1)      
print(f"{Style.RESET_ALL}")