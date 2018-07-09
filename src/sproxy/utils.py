import struct
 
DATA_HEADER_FORMAT = '>ii'
VERSION = 1

def read_request(conn):
    version, length = struct.unpack(DATA_HEADER_FORMAT, conn.recv(8))
    DATA_FORMAT = '>%ss'%(str(length))
    data, = struct.unpack(DATA_FORMAT,conn.recv(length))
    return data.decode()

def write_request(conn, data, encoding='ascii'):
    data = data.encode(encoding)
    length = len(data)
    DATA_FORMAT = DATA_HEADER_FORMAT + '%ss'%(str(length))
    conn.send(struct.pack(DATA_FORMAT, VERSION, length, data))
