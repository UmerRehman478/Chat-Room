import socket
import threading

#recives message from server
def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
    except:
        print("🐼 Disconnected from server.")
    finally:
        client_socket.close()

def main():
    host = "127.0.0.1"
    port = 12345

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        #Receive and print the name it gets from the server
        name_prompt = client_socket.recv(1024).decode()  #Asks for "Choose your panda name:"
        print(name_prompt, end=" ")  

        #Put panda name and send it to the server
        panda_name = input()  
        client_socket.sendall(panda_name.encode())

        #Gets welcome message from the server
        print(client_socket.recv(1024).decode())

        #receives messages in a separate thread
        thread = threading.Thread(target=receive_messages, args=(client_socket,))
        thread.daemon = True
        thread.start()

        #Send the messages
        while True:
            message = input()
            if message.lower() == "@leaves":
                client_socket.sendall(message.encode())
                break
            client_socket.sendall(message.encode())

    except ConnectionRefusedError:
        print("🐼 Server is not running. Please try again later.")
    except KeyboardInterrupt:
        print("\n🐼 Exiting chat...")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
