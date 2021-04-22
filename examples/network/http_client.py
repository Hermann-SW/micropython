try:
    import usocket as socket
except:
    import socket


def main(use_stream=False):
    s = socket.socket()

    host = "neverssl.com"
    hpath = ""
    req = "GET /" + hpath + " HTTP/1.0\r\nHost: " + host + "\r\n\r\n"

    ai = socket.getaddrinfo(host, 80)
    print("Address infos:", ai)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)

    if use_stream:
        # MicroPython socket objects support stream (aka file) interface
        # directly, but the line below is needed for CPython.
        s = s.makefile("rwb", 0)
        s.write(bytes(req, 'utf-8'))
        print(s.read())
    else:
        s.send(bytes(req, 'utf-8'))
        print(s.recv(4096))

    s.close()


main()
