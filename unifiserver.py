"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        # self.wfile.write("<html><body><h1>hi!</h1></body></html>")
        self.wfile.write("Hello from the server")

        mypath = self.path
        
        if mypath.count("&") < 1 and mypath.count("?") > 0:
            # print("NONE")
            bt_addr = mypath.split("?")[1]
            print(bt_addr)

            # TODO: lookup in addr in db
            
        elif mypath.count("&") > 0:
            # print("EXISTS!")
            # TODO: lookup in addrs in db
            bt_addr_set = set(mypath.split("?")[1].split("&"))
            print(bt_addr_set)
        
        else:
            pass


    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()