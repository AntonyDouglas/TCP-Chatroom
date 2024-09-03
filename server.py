import threading
import socket

host = '127.0.0.1'
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []
admins = ['admin1', 'admin2'] 

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            
            client.close()
            clients.remove(client)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break

            decoded_message = message.decode('ascii')
            if decoded_message.startswith('/kick'):
                nickname = nicknames[clients.index(client)]
                if nickname in admins:
                    _, target_nickname = decoded_message.split(' ', 1)
                    kick_user(target_nickname)
                else:
                    client.send('You don\'t have permission to use this command.'.encode('ascii'))
            else:
                broadcast(message)
        except (ConnectionResetError, ConnectionAbortedError):
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} left!'.encode('ascii'))
                nicknames.remove(nickname)
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcast(f"{nickname} joined!".encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def kick_user(nickname):
    if nickname in nicknames:
        index = nicknames.index(nickname)
        client_to_kick = clients[index]
        clients.remove(client_to_kick)
        client_to_kick.send('You have been kicked from the server.'.encode('ascii'))
        client_to_kick.close()
        nicknames.remove(nickname)
        broadcast(f'{nickname} was kicked from the server.'.encode('ascii'))

receive()
