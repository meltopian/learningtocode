import socket, threading, time
try:
    import tkinter
    import tkinter.scrolledtext
except ImportError:
    import Tkinter as tkinter
    import ScrolledText as scrolledtext
    tkinter.scrolledtext = scrolledtext
def connection(sock):
    while True:
        data_recv = sock.recv(4098)
        if not data_recv:
            break
#        print(data_recv)
        output_box.insert(tkinter.END, data_recv)
        output_box.yview(tkinter.END)
    sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("45.152.210.255", 9872))
# connection(sock)

thread = threading.Thread(target=connection, args=(sock,))
thread.daemon=True
thread.start()

# sock.sendall(bytes('Hello I am Bob' + "\n", 'utf-8'))
# while True:
#     sock.sendall(bytes(input()+"\n", 'utf-8'))

root = tkinter.Tk()
root.title("Chat Client")
output_box = tkinter.scrolledtext.ScrolledText(root, width=40, height=15)
output_box.pack(fill=tkinter.BOTH, expand=1)
input_box = tkinter.Entry(root)
input_box.pack(fill=tkinter.BOTH)
def handle_user_input(e):
#    sock.sendall((input_box.get()+'\n').encode('utf-8'))
    sock.sendall(('Mel: '+input_box.get()+'\n').encode('utf-8'))
    input_box.delete(0, tkinter.END)
input_box.bind("<KeyRelease-Return>", handle_user_input)
input_box.focus_set()

root.mainloop()
