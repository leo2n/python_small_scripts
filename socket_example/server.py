"""
socket server
A example writed by Python
"""

import socket

def server_socket():
    """
    a function imply server socket
    """
    sk = socket.socket()
    sk.bind(("127.0.0.1", 9008))
    sk.listen(5) # ???
    while True:
        conn, addr = sk.accept()
        while True:
            accept_date = str(conn.recv(1024), encoding="utf8")
            print("".join(["receive data: ", accept_date, "  cilent ip:  ", str(addr[0]) ,"  cilent port:  ", str(addr[1])]))
            if accept_date == "byebye":
                break
            send_data = input("input send data: ")

            conn.sendall(bytes(send_data, encoding="utf8"))
        conn.close()

if __name__ == "__main__":
    server_socket()
