import socket
import sys
from assessed1 import recv_listing, send_file, recv_file

try:
    # create a TCP socket
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get the server's address by getting (IP address, Port number)
    srv_addr = (sys.argv[1], int(sys.argv[2]))

    # Convert to string, to be used shortly
    str_srv_addr = str(srv_addr)

    # get the requested command:
    cl_request = sys.argv[3]
    if cl_request == "put" or cl_request == "get":
        filename = sys.argv[4]
        
    # connect socket to server
    cli_sock.connect(srv_addr)
    print(f"Connecting to server: {str_srv_addr}")

    try:
        cli_sock.send(cl_request.encode("utf-8"))
        if (cl_request == "list"):
            recv_listing(cli_sock)
        elif (cl_request == "put"):
            send_file(cli_sock, filename)
        elif (cl_request == "get"):
            recv_file = (cli_sock, filename)       
    except:
        print("Request was not sent or processed correctly")
    finally:
        cli_sock.close()
except:
    print("client requires (localhost, port, request, (file if request is get or put))")
