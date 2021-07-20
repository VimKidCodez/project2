import threading
import socket


host ='192.168.1.8'
port =  9090
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind( (host , port ))
server.listen()


clients = []
nickname = []


def sending_messages(message):
    for client in clients:
        client.send(message)


def handle (clint):
    while True:
        try:
            message = client.recv(1024)
            sending_messages(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            sending_messages(f"{nickname}left the chat ".encode('ascii'))
            nicknames.remove(nickname)
            break


def recive():
    while True:
        client , address = server.accept()
        print (f"connected with {str(address)}")

        client.send('NICK'.encode('asci'))
        nickname =  clients.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print (f"nickname os client is {nickname}!")
        sending_messages(f"{nickname}joined the chat !".encode('ascii'))
        client.send(' connected to the server ! '.encode('ascii'))


        thread = threading.Thread(target=handle,args=(client))
        thread.start()


print('server is listening')
recive()