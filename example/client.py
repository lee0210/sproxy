from sproxy.utils import write_request, read_request

import socket

PORT = 20000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1',PORT))
    write_request(s, 'HB')
    data = read_request(s)
    print(data)
