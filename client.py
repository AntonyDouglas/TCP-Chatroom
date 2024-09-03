import socket
import threading

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            elif message == 'You have been kicked from the server.':
                print(message)
                client.close()
                break
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = input('')
        if message.startswith('/kick'):
            client.send(message.encode('ascii'))
        elif message.startswith('/'):
            client.send(f"Unknown command: {message}".encode('ascii'))
        else:
            formatted_message = '{}: {}'.format(nickname, message)
            client.send(formatted_message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
