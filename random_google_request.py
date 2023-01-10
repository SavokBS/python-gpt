import http.server
import random
import socketserver

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))

    def do_GET(self):
        search_terms = ["Python", "programming", "development", "code", "algorithm"]
        search_term = random.choice(search_terms)
        self._send_response("""
            <html>
                <head>
                    <meta http-equiv="refresh" content="0; url='https://www.google.com/search?q={}'" />
                </head>
                <body>
                    <p>Redirecting to a random Google page...</p>
                </body>
            </html>
        """.format(search_term))

with socketserver.TCPServer(("", 6974), RequestHandler) as httpd:
    httpd.serve_forever()
    
    
"""
This code creates a new class called RequestHandler which is a subclass of http.server.BaseHTTPRequestHandler. This class will handle incoming HTTP requests.
Inside the class, do_GET method is overridden. Every time a GET request is made to the server, this method is called and It chooses random search term from the list of search_terms and redirect the user to google with the chosen search term.
In the last part of code, a new instance of the TCPServer class is created and bound to localhost on port 6974, and the RequestHandler class is passed as an argument. This starts the server and will listen for incoming requests on the specified port.
"""
