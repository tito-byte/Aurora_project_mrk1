import os
from time import sleep
from colorama import Fore, Style, init
import configparser
import sys
import subprocess





# Clears the terminal to keep everything clean and neet
def clear_terminal():
    os.system('clear')



# The logo for the terminal when needed just call
def Settings_logo():
    print("""
          
  /$$$$$$              /$$     /$$     /$$                              
 /$$__  $$            | $$    | $$    |__/                              
| $$  \__/  /$$$$$$  /$$$$$$ /$$$$$$   /$$ /$$$$$$$   /$$$$$$   /$$$$$$$
|  $$$$$$  /$$__  $$|_  $$_/|_  $$_/  | $$| $$__  $$ /$$__  $$ /$$_____/
 \____  $$| $$$$$$$$  | $$    | $$    | $$| $$  \ $$| $$  \ $$|  $$$$$$ 
 /$$  \ $$| $$_____/  | $$ /$$| $$ /$$| $$| $$  | $$| $$  | $$ \____  $$
|  $$$$$$/|  $$$$$$$  |  $$$$/|  $$$$/| $$| $$  | $$|  $$$$$$$ /$$$$$$$/
 \______/  \_______/   \___/   \___/  |__/|__/  |__/ \____  $$|_______/ 
                                                     /$$  \ $$          
                                                    |  $$$$$$/          
                                                     \______/           
          
          """)



# All the basic selections 
def setting_choices():
    print("""
    1.List Of Databases

    2.Change Text Color

    3.About Sting

    4.Add User To Aurora Database

    5.Back     
          
          
          """)

def user_choice():
    while True:
        user_input = input("> ")

        # List of programs
        if user_input == "1":
            clear_terminal()
            print("""\
            
 /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$  /$$$$$$ 
| $$__  $$ /$$__  $$|__  $$__//$$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$_____/ /$$__  $$
| $$  \ $$| $$  \ $$   | $$  | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/| $$      | $$  \__/
| $$  | $$| $$$$$$$$   | $$  | $$$$$$$$| $$$$$$$ | $$$$$$$$|  $$$$$$ | $$$$$   |  $$$$$$ 
| $$  | $$| $$__  $$   | $$  | $$__  $$| $$__  $$| $$__  $$ \____  $$| $$__/    \____  $$
| $$  | $$| $$  | $$   | $$  | $$  | $$| $$  \ $$| $$  | $$ /$$  \ $$| $$       /$$  \ $$
| $$$$$$$/| $$  | $$   | $$  | $$  | $$| $$$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$$|  $$$$$$/
|_______/ |__/  |__/   |__/  |__/  |__/|_______/ |__/  |__/ \______/ |________/ \______/ 




""")
            
            database_path = '/home/titobyte/Desktop/Databases/aurora_databases'
            databases = os.listdir(database_path)
            for database in databases:
                count = 0
                print(f"{count + 1} : {database}")
            


            sleep(2)
            print()
            print()
            print()
            
            input("Press [Enter] to continue...")
            start()
        
        
        # Change the color of the text
        if user_input == "2":
                clear_terminal()
                print("""
  /$$$$$$   /$$$$$$  /$$        /$$$$$$  /$$$$$$$         /$$$$$$  /$$   /$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$$ 
 /$$__  $$ /$$__  $$| $$       /$$__  $$| $$__  $$       /$$__  $$| $$  | $$ /$$__  $$| $$$ | $$ /$$__  $$| $$_____/| $$__  $$
| $$  \__/| $$  \ $$| $$      | $$  \ $$| $$  \ $$      | $$  \__/| $$  | $$| $$  \ $$| $$$$| $$| $$  \__/| $$      | $$  \ $$
| $$      | $$  | $$| $$      | $$  | $$| $$$$$$$/      | $$      | $$$$$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$| $$$$$   | $$$$$$$/
| $$      | $$  | $$| $$      | $$  | $$| $$__  $$      | $$      | $$__  $$| $$__  $$| $$  $$$$| $$|_  $$| $$__/   | $$__  $$
| $$    $$| $$  | $$| $$      | $$  | $$| $$  \ $$      | $$    $$| $$  | $$| $$  | $$| $$\  $$$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$/|  $$$$$$/| $$$$$$$$|  $$$$$$/| $$  | $$      |  $$$$$$/| $$  | $$| $$  | $$| $$ \  $$|  $$$$$$/| $$$$$$$$| $$  | $$
 \______/  \______/ |________/ \______/ |__/  |__/       \______/ |__/  |__/|__/  |__/|__/  \__/ \______/ |________/|__/  |__/
                                                                                                                            
                                                                                                    
                            """)

                valid_colors = {
                        "red","blue","black","green","yellow","white","cyan","magenta",
                        "1","2","3","4","5","6","7","8",
                }

                print("""
                Choose a Color
                ##############          
    1.Red
    
    2.White / default
    
    3.Blue
    
    4.Yellow            
    
    5.Black
    
    6.Green
    
    7.Cyan
    
    8.Magenta
                                """)

                while True:
                    color_choice = input("> ")

                    if color_choice.lower() not in valid_colors:
                        print("That's not a valid choice")
                        continue
                    else:
                        if color_choice == "1":
                            color_choice = "red"
                        elif color_choice == "2":
                            color_choice = "white"
                        elif color_choice == "3":
                            color_choice = "blue"
                        elif color_choice == "4":
                            color_choice = "yellow"
                        elif color_choice == "5":
                            color_choice = "black"
                        elif color_choice == "6":
                            color_choice = "green"
                        elif color_choice == "7":
                            color_choice = "cyan"
                        elif color_choice == "8":
                            color_choice = "magenta"
                        
                        # Read all lines first
                        with open("Aurora_terminal_settings/config/Aurora_settings.conf", "r") as conf_file:
                            lines = conf_file.readlines()

                        # Modify the line containing "text_color"
                        with open("Aurora_terminal_settings/config/Aurora_settings.conf", "w") as conf_file:
                            for line in lines:
                                if line.startswith("text_color"):
                                    conf_file.write(f"text_color = {color_choice}\n")  # Write the new line
                                    print("\nColor Theme has been changed")
                                    
                                    sleep(1)
                                    print("\nRestarting for changes to take effect")
                                    
                                    sleep(2)
                                    break  # Exit the loop and finish writing to the file
                                else:
                                    conf_file.write(line)  # Write the unchanged lines

                        # Apply the color change to the terminal
                        if color_choice == "red":
                            print(Fore.RED + "This is red text!")
                        elif color_choice == "blue":
                            print(Fore.BLUE + "This is blue text!")
                        elif color_choice == "black":
                            print(Fore.BLACK + "This is black text!")
                        elif color_choice == "green":
                            print(Fore.GREEN + "This is green text!")
                        elif color_choice == "yellow":
                            print(Fore.YELLOW + "This is yellow text!")
                        elif color_choice == "white":
                            print(Fore.WHITE + "This is white text!")
                        elif color_choice == "cyan":
                            print(Fore.CYAN + "This is cyan text!")
                        elif color_choice == "magenta":
                            print(Fore.MAGENTA + "This is magenta text!")

                        sleep(1)
                        print("\nRestarting for changes to take effect")
                        sleep(2)
                          # Exit the loop and finish the color change
                        
                        subprocess.run([sys.executable, 'Aurora_terminal_settings/settings.py'])
                        sys.exit()

                        #subprocess.run([sys.executable, 'Aurora_terminal_based_ui.py'])
                        #sys.exit()



        # About Sting AI
        if user_input == "3":
            
            
            os.system('clear')
            
            print("""
                  
  /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$$        /$$$$$$  /$$$$$$$$  /$$$$$$     /$$   /$$      /$$$$$$ 
 /$$__  $$| $$__  $$ /$$__  $$| $$  | $$|__  $$__/       /$$__  $$|__  $$__/ |_  $$_/    | $$$ | $$     /$$__  $$
| $$  \ $$| $$  \ $$| $$  \ $$| $$  | $$   | $$         | $$  \__/   | $$      | $$      | $$$$| $$    | $$  \__/
| $$$$$$$$| $$$$$$$ | $$  | $$| $$  | $$   | $$         |  $$$$$$    | $$      | $$      | $$ $$ $$    | $$ /$$$$
| $$__  $$| $$__  $$| $$  | $$| $$  | $$   | $$          \____  $$   | $$      | $$      | $$  $$$$    | $$|_  $$
| $$  | $$| $$  \ $$| $$  | $$| $$  | $$   | $$          /$$  \ $$   | $$      | $$      | $$\  $$$    | $$  \ $$
| $$  | $$| $$$$$$$/|  $$$$$$/|  $$$$$$/   | $$         |  $$$$$$//$$| $$ /$$ /$$$$$$ /$$| $$ \  $$ /$$|  $$$$$$/
|__/  |__/|_______/  \______/  \______/    |__/          \______/|__/|__/|__/|______/|__/|__/  \__/|__/ \______/ 
                                                                                                                 
                                                                                                                 
                                                                                                     

                  """)
            story = """

The Story of Sting: My Personal AI Assistant

Sting is my custom-built AI assistant, designed to enhance my digital workflow and automate daily tasks. 
It started as a simple Python project inspired by my interest in AI and automation,
evolving into a sophisticated system capable of speech recognition, smart home integration, and file management.

Built using Python, Ollama AI, Coqui TTS, and Home Assistant, Sting runs on my Ubuntu Linux-powered server, ensuring efficiency and control.
As I expand my knowledge in C++ and JavaScript, I continue refining Sting’s capabilities, aiming for a seamless, J.A.R.V.I.S-like experience.

This project represents my passion for AI, programming, and system optimization, constantly growing alongside my skills and innovations."""
            
            # Gives the typing effect as the text gets printed out
            def typing_effect(text, speed=0.05):
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    sleep(speed)
                print()

            typing_effect(story, 0.05)
            print()
            input("Press [Enter] to continue...")
            start()
           

        
        # Add username and password
        if user_input == "4":
            
            #print("need to add something to connect to the database where the database is stored")

            import add_user_to_database
            
            add_user_to_database.the_start()
            user_adding_status = add_user_to_database.creation_status()
            
            os.system('clear')
            print(user_adding_status)
            
            sleep(5)

            start()
        
        # Go back 
        if user_input == "5":
            subprocess.run([sys.executable, 'Aurora_terminal_based_ui.py'])
            sys.exit()
            

            


# Order to start the program in 
def start():
    #1
    

    #2
    clear_terminal()

    #3
    Settings_logo()

    #4
    setting_choices()

    #5
    user_choice()

start()