import socket

server_ip = "127.0.0.1"
server_port = 5555

try:
    server_config = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_config.bind((server_ip, server_port))
    server_config.listen()
    print(f"Listening on {server_ip}:{server_port}...")

    while True:  # Keep accepting clients
        client_socket, client_address = server_config.accept()
        print(f"Connection from {client_address}")

        code = client_socket.recv(1024).decode("utf-8")
        if code == "RY.:8gf^qtt2f/Y[kd9`s!^Bq](5ng[n1]1LN_IE?J+(+m}AMkkC0":
            response = "git clone https://github.com/tito-byte/Strong_Password_Generator.git \ncd Strong_Password_Generator\n python3 Strong_password_generator.py"
            client_socket.send(response.encode("utf-8"))  # Encode before sending

        client_socket.close()  # Close connection after response

except Exception as e:
    print(f"Error: {e}")

finally:
    server_config.close()  # Close server when done
