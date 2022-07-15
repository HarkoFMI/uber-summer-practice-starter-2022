import os
from flask import Flask, request

server = Flask(__name__)

@server.route("/")
def hello():
  return "Hello World alabala!"

@server.route("/hello")
def personalised_hello():
  username = request.args.get('user')
  return f'Hello {username}!'

if __name__ == "__main__":
   server_port = os.environ['FLASK_PORT']
   server.run(host='0.0.0.0', port=server_port, debug=True)
