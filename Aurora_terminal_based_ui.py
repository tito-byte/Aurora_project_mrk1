import os 
from time import sleep
from colorama import Fore, Style, init
import configparser
import sys
import subprocess
            
def load_config():
    # Open the config file
    parser = configparser.ConfigParser()
    parser.read("Aurora_terminal_settings/config/Aurora_settings.conf")

    # Extract text color
    tx_color = parser["text-colors"]["text_color"]

    # Define color mapping
    color_map = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
        'black': Fore.BLACK
    }

    # Set text color globally
    global text_color
    text_color = color_map.get(tx_color.lower(), Fore.WHITE)

    # Explicitly delete parser to free memory (not necessary but good practice)
    del parser

def clear_terminal():
    os.system('clear')

def main_logo():
    print(f"{text_color}{Style.BRIGHT}""""


  /$$$$$$                                                                   
 /$$__  $$                                                                  
| $$  \ $$ /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$       
| $$$$$$$$| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ |____  $$      
| $$__  $$| $$  | $$| $$  \__/| $$  \ $$| $$  \__/| $$  \ $$  /$$$$$$$      
| $$  | $$| $$  | $$| $$      | $$  | $$| $$      | $$  | $$ /$$__  $$      
| $$  | $$|  $$$$$$/| $$      |  $$$$$$/| $$      |  $$$$$$/|  $$$$$$$      
|__/  |__/ \______/ |__/       \______/ |__/       \______/  \_______/      
                                                                            

    """)

def main_choices():
    print("""
    1.File Server / Sting

    2.Auroa Server Programs

    3.Sting Ai
        
    4.Settings
        
    5.Exit
        

    """)

def user_choice():
    while True:
        User_input = input("> ")

        if User_input == "1":
            print('Connecting to file server now')
            
            sleep(2)
            continue
        if User_input == "2":
            print("I need to make the database for this thing and make it always update relative to my github repository")
            
            sleep(2)    
            continue
        if User_input == "3":
            print("""Need to find out a away to make sting avalible anywhere I am most likely makeing a 
                program that send specific lines of code for sting for the connection to be made and 
                if the code does not match the connection is terminated""")
            
            sleep(2)
            continue
        if User_input == "4":
            
            subprocess.run([sys.executable, 'Aurora_terminal_settings/settings.py'])
            sys.exit()

            
            sleep(2)
            
            
        if User_input == "5":
            print("exiting now")
            
            sleep(1)
            os.system('clear')
            exit()

# Order to start the program in 
def start_order():
    #1
    #config()

    #2
    clear_terminal()

    #3
    main_logo()

    #4
    main_choices()

    #5
    user_choice()

load_config()
start_order()