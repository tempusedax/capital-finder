# https://restcountries.com/v2/name/{name}
#
# from restcountries import RestCountryApiV2 as rapi
#
# def foo(name):
#     country_list = rapi.get_countries_by_name('France')


# '''
# Basically grab the country data obj
# parse it,
# Put it in a dictionary with key as city, capital as value
# Make string message with either city or cap accessing the dict
#
# '''

from http.server import BaseHTTPRequestHandler
from datetime import datetime


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return