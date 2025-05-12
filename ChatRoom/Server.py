import socket
import threading
import random
import datetime

#Panda facts and emojis
PANDA_EMOJIS = ["🐼", "🎋", "🌿", "🍃", "🐾"]
PANDA_FACTS = [
    "Pandas spend around 14 hours a day eating bamboo! 🎋",
    "Baby pandas are born pink and weigh only about 100 grams! 🐼",
    "A group of pandas is called an embarrassment! 😆",
    "Pandas can swim and are excellent tree climbers! 🌲",
    "There are only about 1,800 giant pandas left in the wild. 🏞️"
]

#List of connected names
clients = {}
lock = threading.Lock()

#Logs messages here
def log_message(message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_entry = f"{timestamp} {message}\n"
    print(log_entry.strip())  #prints log on screen
    with open("server_log.txt", "a") as log_file:  #adds to log file
        log_file.write(log_entry)

#Controls the communication with one client
def handle_client(client_socket):
    try:
        #Ask client to pick a name
        client_socket.sendall("🐼 Choose your panda name:".encode())

        #Receives the panda name and stores it
        panda_name = client_socket.recv(1024).decode().strip()

        #If its empty
        if not panda_name:
            client_socket.sendall("Invalid name. Restart and enter a valid name.".encode())
            client_socket.close()
            return
        with lock:
            clients[client_socket] = panda_name

        log_message(f"{panda_name} joined the chat.")  

        #Welcome message
        client_socket.sendall(f"🐼 Welcome {panda_name}! You can now chat. Type messages or use @bamboo, @grove, @leaves.".encode())

        while True:
            #wait for message from client
            message = client_socket.recv(1024).decode().strip()
            if not message:
                break 

            #Handle special commands
            if message == "@bamboo":
                #Gives a random panda fact
                response = random.choice(PANDA_FACTS)
                client_socket.sendall(response.encode())
                log_message(f"{panda_name} requested @bamboo. Sent fact: {response}")
            elif message == "@grove":
                #Gives  a list of connected panda names
                with lock:
                    users = ", ".join(clients.values())
                client_socket.sendall(f"Connected pandas: {users}".encode())
                log_message(f"{panda_name} requested @grove. Sent list: {users}")
            elif message == "@leaves":
                #Allows the client to leave the chat
                client_socket.sendall("You have left the chat. Goodbye! 🐾".encode())
                log_message(f"{panda_name} left the chat.")
                break
            else:
                #Show message to clients
                broadcast(f"{panda_name}: {message} {random.choice(PANDA_EMOJIS)}", client_socket)
                log_message(f"{panda_name} sent message: {message}")

    #Handles disconnection
    except (ConnectionResetError, BrokenPipeError):
        log_message(f"{clients.get(client_socket, 'Unknown Panda')} disconnected unexpectedly.")
    finally:
        with lock:
            if client_socket in clients:
                del clients[client_socket]
        client_socket.close()

#gives message to all connected clients
def broadcast(message, sender_socket=None):
    with lock:
        for client in list(clients.keys()):
            try:
                client.sendall(message.encode())
            except:
                #If sending fails, remove that client
                client.close()
                del clients[client]
        log_message(f"Broadcasted message: {message}")

#Start the server and looks for connections
def main():
    host = "127.0.0.1"  #Localhost
    port = 12345        #Port number

    #Server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  #Has 5 waiting connections
    log_message("🐼 Panda Chat Server started")

    while True:
        try:
            #Accept a new client connection
            client_socket, _ = server_socket.accept()
            log_message("New panda joined the chat!")

            #Handle client in a new thread
            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()
        except KeyboardInterrupt:
            log_message("🐼 Server shutting down")
            break

    server_socket.close()

#Start the server
if __name__ == "__main__":
    main()
