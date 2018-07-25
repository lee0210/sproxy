from sproxy.utils import read_request, write_request
class fake_socket:
    def recv(self, n):
        self.c = self.c + n
        return self.data[self.c-n:self.c]
    def send(self, data):
        self.data = data
        self.c = 0 

conn = fake_socket()

def test_read_write_request():
    input_data = 'hello world'
    write_request(conn, input_data)
    output_data = read_request(conn)
    assert(output_data == input_data)
   
def test_testTravisCI():
    assert(False)       
