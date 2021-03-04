import os
import socket

def send_file(socket, filename):
    with open(filename, "rb") as f:
        socket.sendall(filename)
    return
    
def recv_file(socket, filename):
    with open(filename, "wb") as f:
        while True:
            print("Receiving file: ")
            if (data.decode("utf-8") == ""):
                print("Reached end of file.", end = "")
                break
            data = socket.recv(1024)
            f.write(data.decode("utf-8"))
    return   

def send_listing(socket):
    path = os.getcwd()
    directories = os.listdir(path)
    
    for filename in directories:
        socket.send(filename.encode("utf-8"))
    return
      
def recv_listing(socket):
    listing = socket.recv(1024).decode("utf-8")
    print(listing)
    return
    