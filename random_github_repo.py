import http.server
import random
import socketserver
import json
import requests

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))

    def do_GET(self):
        resp = requests.get("https://api.github.com/orgs/github/repos")
        repos = json.loads(resp.text)
        repo = random.choice(repos)
        repo_url = repo['html_url']
        self._send_response("""
            <html>
                <head>
                    <meta http-equiv="refresh" content="0; url='{}'" />
                </head>
                <body>
                    <p>Redirecting to a random Github official repository...</p>
                </body>
            </html>
        """.format(repo_url))

with socketserver.TCPServer(("", 6974), RequestHandler) as httpd:
    httpd.serve_forever()

"""
This code creates a new class called RequestHandler which is a subclass of http.server.BaseHTTPRequestHandler. This class will handle incoming HTTP requests.
The first thing the do_GET method does is it makes a GET request to the Github's API to get the list of Github official repositories by calling requests.get("https://api.github.com/orgs/github/repos"). The API returns the repositories in the json format, which is then parsed into a python list by json.loads(resp.text).
Then, using the random.choice() function, it randomly chooses one repository from the list of repositories. It then gets the html_url of the chosen repository and saves it in the variable repo_url
Finally, it sends an HTML response back to the client with a meta refresh tag, which automatically redirects the client's browser to the repository URL.

And in the last part of code, a new instance of the TCPServer class is created and bound to localhost on port 6974, and the RequestHandler class is passed as an argument. This starts the server and will listen for incoming requests on the specified port.
You can access the webpage by visiting 'http://localhost:6974' in your web browser. It will redirect you to a random Github's official repository.
"""
