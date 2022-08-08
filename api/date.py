from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    message = f"The Capital of "
    self.wfile.write(message.encode())
    return