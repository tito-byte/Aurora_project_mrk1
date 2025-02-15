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

        #   This just connects to the file server (Not the NAS) to pull personal documents or any code that is not released 
        # File Server Input
        if User_input == "1":
            print('Connecting to file server now')
            
            sleep(2)
            continue


        #   Connected to the server uses a simple sql database that uses my github repository to store all the programs/scripts that
        #   are available to download along with a simple input to make the download easy
        # Aurora Server Input
        if User_input == "2":
            print("I need to make the database for this thing and make it always update relative to my github repository")
            
            sleep(2)    
            continue

        # Be able to talk to Sting my personal AI assistant
        # Sting Input
        if User_input == "3":
            print("""Need to find out a away to make sting avalible anywhere I am most likely makeing a 
                program that send specific lines of code for sting for the connection to be made and 
                if the code does not match the connection is terminated""")
            
            sleep(2)
            continue

        #   Settings for the terminal to customize or be able to access the abilty to learn more about the system behind all of it 
        # Settings Input
        if User_input == "4":
            
            subprocess.run([sys.executable, 'Aurora_terminal_settings/settings.py'])
            sys.exit()

            
            sleep(2)
            
        #   This fully exits the systems and deletes itself
        # Exit input            
        if User_input == "5":
            import shutil
                    
            os.system('clear')

            
            # Deletes the folder containing the program form the users computer
            try:
                 script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
                    
                 shutil.rmtree(script_dir)
                    
            except Exception as e:
                    print("Error deleting removing")
            
            
            
            



# Order to start the program in 
def start_order():

    #1
    clear_terminal()

    #2
    main_logo()

    #3
    main_choices()

    #4
    user_choice()

#   Started sepretly beacuse due to the fact that start_order is called to be able to reset the ui it would not make sense to run & 
#   load the config over and over because there is no need
# loads all the configuration for the entire ui using the Aurora_settings.conf file
load_config()


# Starts the entire program off in order to keep everything neat
start_order()
