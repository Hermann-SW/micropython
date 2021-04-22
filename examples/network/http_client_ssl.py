try:
    import usocket as _socket
except:
    import _socket
try:
    import ussl as ssl
except:
    import ssl


def main(use_stream=True):
    s = _socket.socket()

    host = "stamm-wilbrandt.de"
    hpath = "cgi-bin/sol.English.pl?60000"
    req = "GET /" + hpath + " HTTP/1.0\r\nHost: " + host + "\r\n\r\n"

    ai = _socket.getaddrinfo(host, 443)
    print("Address infos:", ai)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)

    s = ssl.wrap_socket(s)
    print(s)

    if use_stream:
        # Both CPython and MicroPython SSLSocket objects support read() and
        # write() methods.
        s.write(bytes(req, 'utf-8'))
        print(s.read(4096))
    else:
        # MicroPython SSLSocket objects implement only stream interface, not
        # socket interface
        s.send(bytes(req, 'utf-8'))
        print(s.recv(4096))

    s.close()


main()
