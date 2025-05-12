import http.server
import socketserver
import requests
import json
from datetime import datetime
from http import HTTPStatus

class Handler(http.server.SimpleHTTPRequestHandler):
    i = 0
    def do_GET(self):
        Handler.i += 1
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(bytes('Hello world!\n', 'utf-8'))
        self.wfile.write(bytes('Current date and time: ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n', 'utf-8'))
        self.wfile.write(bytes('This is request #' + str(Handler.i) + "\n", 'utf-8'))
        if (Handler.i % 10 == 0):
            self.wfile.write(bytes('Your request # is divisible by 10! Woohoo!\n', 'utf-8'))
        funfactjson = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random', headers={"Accept":"application/json"})
        self.wfile.write(bytes('Fun fact:' + funfactjson.json()['text'], 'utf-8'))


httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()
