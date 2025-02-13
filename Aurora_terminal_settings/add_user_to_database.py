import socket
import os
import getpass
import bcrypt
from time import sleep
from colorama import Fore, Style, init
import configparser






def creation_status():
        if code != 'V{{$h"ibfv:/!{,=D3{0T=QrIb[nJjAA7':
                    status = "User could not be added to the database, please try again later"
                    #print(status)
                    return status
        
        status = """

 /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$$         /$$$$$$  /$$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
| $$  | $$ /$$__  $$| $$_____/| $$__  $$       /$$__  $$| $$__  $$| $$__  $$| $$_____/| $$__  $$
| $$  | $$| $$  \__/| $$      | $$  \ $$      | $$  \ $$| $$  \ $$| $$  \ $$| $$      | $$  \ $$
| $$  | $$|  $$$$$$ | $$$$$   | $$$$$$$/      | $$$$$$$$| $$  | $$| $$  | $$| $$$$$   | $$  | $$
| $$  | $$ \____  $$| $$__/   | $$__  $$      | $$__  $$| $$  | $$| $$  | $$| $$__/   | $$  | $$
| $$  | $$ /$$  \ $$| $$      | $$  \ $$      | $$  | $$| $$  | $$| $$  | $$| $$      | $$  | $$
|  $$$$$$/|  $$$$$$/| $$$$$$$$| $$  | $$      | $$  | $$| $$$$$$$/| $$$$$$$/| $$$$$$$$| $$$$$$$/
 \______/  \______/ |________/|__/  |__/      |__/  |__/|_______/ |_______/ |________/|_______/ 
                                                                                                
                                                                                            

"""
        #print(status)
        return status


def the_start():        
    
      

    server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"
    server_port = 12345


    server_connection.connect((server_ip, server_port))

    os.system('clear')
    def logo():
        print("""
  /$$$$$$  /$$$$$$$  /$$$$$$$        /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$$ 
 /$$__  $$| $$__  $$| $$__  $$      | $$  | $$ /$$__  $$| $$_____/| $$__  $$
| $$  \ $$| $$  \ $$| $$  \ $$      | $$  | $$| $$  \__/| $$      | $$  \ $$
| $$$$$$$$| $$  | $$| $$  | $$      | $$  | $$|  $$$$$$ | $$$$$   | $$$$$$$/
| $$__  $$| $$  | $$| $$  | $$      | $$  | $$ \____  $$| $$__/   | $$__  $$
| $$  | $$| $$  | $$| $$  | $$      | $$  | $$ /$$  \ $$| $$      | $$  \ $$
| $$  | $$| $$$$$$$/| $$$$$$$/      |  $$$$$$/|  $$$$$$/| $$$$$$$$| $$  | $$
|__/  |__/|_______/ |_______/        \______/  \______/ |________/|__/  |__/
                                                                                    
                                                            

                """)

    logo()

    username_to_add = input('USERNAME > ')

    while True:
        password_to_add = getpass.getpass('PASSWORD > ')

        confirm_password_to_add = getpass.getpass('CONFIRM PASSWORD > ')

        encoded_password = password_to_add.encode()
        
        hashed_password_to_add = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
        
        if confirm_password_to_add != password_to_add:
            os.system('clear')
            logo()
            print('\nPASSWORDS DO NOT MATCH')
            
            
            continue


        else:
            print(password_to_add)
            
            server_connection.send(username_to_add.encode('utf-8'))
            sleep(.2)
            server_connection.send(hashed_password_to_add)

            global code
            code = server_connection.recv(1024).decode('utf-8')
            
            creation_status()
            break
            
        

   



