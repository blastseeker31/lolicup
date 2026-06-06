"""Serve LoliCup static site — Tailscale IP only, no HTTPS."""
import http.server
import os
import socketserver

PORT = 8085
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def log_message(self, fmt, *args):
        pass

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(('0.0.0.0', PORT), Handler) as httpd:
        print(f'LoliCup → http://0.0.0.0:{PORT}')
        httpd.serve_forever()
