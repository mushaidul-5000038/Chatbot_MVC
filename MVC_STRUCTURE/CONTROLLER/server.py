
import http.server
import socketserver
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(
    os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(
    'D:\My_chatbot_mvc_repos\Chatbot_MVC\MVC_STRUCTURE\MODEL\chat_processor.py', 'D:\My_chatbot_mvc_repos\Chatbot_MVC\MVC_STRUCTURE')))
# first parameter goes for the Script Directory path
# second parameter goes for the parent directory path
from MODEL.chat_processor import chatbot_query

PORT = 8083
DIRECTORY = 'VIEW'


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        self.send_response(200)
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length)
        self.end_headers()
        print('user query', post_body)
        print(type(post_body))
        chat_processor_chatbot_reply = chatbot_query(post_body)
        self.wfile.write(str.encode(chat_processor_chatbot_reply))


with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('serving at port', PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
