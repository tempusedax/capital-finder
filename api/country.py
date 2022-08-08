from urllib import parse
from http.server import BaseHTTPRequestHandler
import requests
import json


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    country_name = "Chile"
    capital = "Santiago"
    api_url = f"https://restcountries.com/v3.1/name/{country_name}"
    api_capital = f"https://restcountries.com/v2/capital/{capital}"
    response = requests.get(api_url)
    json_data = json.loads(response.text)
    country_capital = json_data[0]['capital']
    message = f" The capital of {country_name} is {country_capital}  "
    self.wfile.write(message.encode())
    return


# url = "https://restcountries.com/v3.1/name/peru"
#
# response = requests.get(url)


