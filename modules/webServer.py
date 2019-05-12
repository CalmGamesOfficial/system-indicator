import os
import webbrowser
import socketserver as server
from http.server import BaseHTTPRequestHandler, HTTPServer

def create():
    port = 8000

    httpd = HTTPServer(("localhost", port), myServer)
    webbrowser.open_new("http://localhost:8000")
    print("Configuration window is openned in " + "http://localhost:" + str(port))
    print("Press Ctrl + C to stop")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

class myServer(BaseHTTPRequestHandler):
    def do_GET(self):
        root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'modules/www')
        if self.path == '/':
            filename = root + '/index.html'
        else:
            filename = root + self.path

        self.send_response(200)
        if filename[-4:] == '.css':
            self.send_header('Content-type', 'text/css')
        elif filename[-5:] == '.json':
            self.send_header('Content-type', 'application/javascript')
        elif filename[-3:] == '.js':
            self.send_header('Content-type', 'application/javascript')
        elif filename[-4:] == '.ico':
            self.send_header('Content-type', 'image/x-icon')
        else:
            self.send_header('Content-type', 'text/html')
        self.end_headers()

        with open(filename, 'rb') as file:
            html = file.read()
            self.wfile.write(html)
