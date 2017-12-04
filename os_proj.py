import BaseHTTPServer
import os
import cgi

def move_car(direction):
    print 'moving %s' % direction
    # TODO: implement car motion

class ReqHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    webpage_text = 'hello world'

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(webpage_text)

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type']
                     })

        self._set_headers()

        direction = form['direction'].value
        move_car(direction)

# run script

print 'Loading html...'
try:
    webpage = open('site.html', 'r')
    webpage_text = webpage.read()
    webpage.close()
except IOError:
    print 'Unable to load site.html'

server_class = BaseHTTPServer.HTTPServer
handler_class = ReqHandler
# port = int(os.environ.get('PORT', 5000))
port = 4545

server_address = ('0.0.0.0', port)
httpd = server_class(server_address, handler_class)
print 'Starting httpd...'
httpd.serve_forever()
