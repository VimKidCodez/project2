import socket
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',5555))


def recive():
    while True :
        try :
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("an error occured")
            client.close()
            break


def write():
    while True:
        message = f'{nickname}:  {input("")}'
        client.send(message.encode('ascii'))


recive_thread = threading.Thread(target=recive)
recive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()