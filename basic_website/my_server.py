import BaseHTTPServer # uses the BaseHTTPServer module

HOST_NAME = '146.231.123.9'
PORT_NUMBER = 8080
indexFile = ''

# the BaseHTTPRequestHandler is used to handle the incomgin requests
class requestHandler(BaseHTTPServer.BaseHTTPRequestHandler): # creates a new class and inherites from BassHTTPServer
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html; charset=utf-8")
        s.end_headers()
        s.wfile.write(indexFile)
    def log_message(self, format, *args):
        with open('logs/requests', 'a') as l:
            l.write("%s|%s|%s\n" % (self.address_string(), self.log_date_time_string(), format%args))
def readFileToString(filename):
    with open(filename, 'r') as f:
        return f.read()

if __name__ == "__main__":
    indexFile = readFileToString('index.html')
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), requestHandler)
    print "server listening on %s:%s" % (HOST_NAME, PORT_NUMBER)
    try :
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.socket.close()
