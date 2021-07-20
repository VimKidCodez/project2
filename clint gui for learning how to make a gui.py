import socket
import threading
from  tkinter import  *

# GUI

root = Tk()
root.title('simple gu ni tested chat ')

f_button = Button(root, text= "start chat ", bg = 'green' )
f_button.grid(row=0,column =0)

e_box = Listbox(root,height=20,width=43)
e_box.grid(row=1,column=0)

en_box = Entry(root)
ba =  en_box.get()
en_box.grid(row= 2,column= 0)

s_button = Button(root, text = 'send')
s_button.grid(row=3,column=0)

root.mainloop()



# All networking and sockting
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


def show():
    while True:
        message = f'{nickname}:  {input("")}'
        client.send(message.encode('ascii'))

def start_chat():
    recive_thread = threading.Thread(target=recive)
    recive_thread.start()

    write_thread = threading.Thread(target=show)
    write_thread.start()


