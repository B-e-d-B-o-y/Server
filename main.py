import os
import socket
import tkinter as tk
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 2908))

server.listen()

def windowregistr():
    window = tk.Tk()
    window.title("IP адрес")

    ip_label = tk.Label(window, text="IP адрес:")
    ip_label.pack()

    ip_text = tk.Label(window, text=socket.gethostbyname_ex(socket.gethostname())[-1][-1])
    ip_text.pack()

    window.mainloop()

def windowbutton():
    while True:

        user, adres = server.accept()

        while True:
            data = user.recv(1024).decode("utf-8").lower()
            print(data)

            if data == "telegram":
                os.startfile("D:\Telegram Desktop\Telegram.exe")

Thread(target=windowregistr).start()
Thread(target=windowbutton).start()