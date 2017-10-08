"""
socket server
A example writed by Python
"""

import socket


def cilent_socket():
    """
    a function imply cilent socket
    """
    sk = socket.socket()
    sk.connect(("127.0.0.1", 9008))
    while True:
        send_data = input("input sending data:")
        sk.sendall(bytes(send_data, encoding="utf8"))
        if send_data == "byebye":
            break
        accept_data = str(sk.recv(1024), encoding="utf8")
        print("".join(["accept data: ", accept_data]))
    sk.close()

if __name__ == "__main__":
    cilent_socket()
