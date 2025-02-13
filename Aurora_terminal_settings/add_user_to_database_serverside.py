import socket
import sqlite3

server_ip = "127.0.0.1"
server_port = 12345

def register_user(username, password):
                
                #   Change the file path for the databases

                conn = sqlite3.connect(r'/home/titobyte/Desktop/Databases/aurora_databases/aurora_userbase.sqlite')
                cursor = conn.cursor()

                try:
                    cursor.execute("INSERT INTO '4uR0R4' (username, 'pass id') VALUES (?, ?)", (username, password))
                    conn.commit()
                    print("User registered successfully!")
                except sqlite3.IntegrityError:
                    print("Username already exists!")
                
                conn.close()

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen()
    print(f"Server is now listening for connections on {server_ip} : {server_port}")

    while True:
            
            
            
            client_connection, addr = server.accept()

            username = client_connection.recv(1024).decode('utf-8')

            hashed_password = client_connection.recv(1024)

            client_connection.send('V{{$h"ibfv:/!{,=D3{0T=QrIb[nJjAA7'.encode('utf-8'))

            print(f"{username} : {hashed_password}")

            break
except:
    print("connection with client could not be astablished")

finally:
    server.close()

try:
    register_user(username, hashed_password)

except:
      print("was not able to write to database")