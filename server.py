import socket
import sys
from assessed1 import send_listing, recv_file, send_file

try:
    # creates a TCP socket on which the server will receive information:
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get the host port
    host_port = sys.argv[1]
    # binds the socket to all available user interfaces
    srv_sock.bind(("0.0.0.0", int(host_port)))
    # get the server's ip address
    host_ip = socket.gethostbyname(socket.gethostname())
    s = ["server up and running", host_ip, host_port]
    print(" ".join(s))
    status = "no operations performed"
    filename = "" # the name of the file on which the request will be performed
    error = ""

    # enables the server to accept connections
    srv_sock.listen(5)
    print("Waiting clients: ")

    while True:
        try:
            cli_sock, cli_addr = srv_sock.accept()
            print("Connected to client: ")
            # receive a request from the client and decode it
            cl_request = cli_sock.recv(1024).decode("utf-8")
            print(f"Client request: {cl_request}", end = "")
            # Process the request
            if (cl_request == "list"):
                send_listing(cli_sock)
            elif (cl_request == "put"):
                filename = cli_sock.recv(1024).decode("utf-8")
                recv_file(cli_sock, filename)
            elif (cl_request == "get"):
                filename = cli_sock.recv(1024).decode("utf-8")
                send_file(cli_sock, filename)
            else:
                print("Invalid request")
                status = "failure"
        except:
            status = "failure"
        finally:
            # server report
            print(f"client: {str(cli_addr)}, request: {cl_request}, status: {status}")
        

            # close the connection
            cli_sock.close()
            print(f"Disconnected from client {cli_addr}")
    
    srv_sock.close()
except:
    # Print the exception message
	print("specify port")