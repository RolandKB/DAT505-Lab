from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = f"""
        <html>
        <head><title>Hacked!</title></head>
        <body>
            <h2>You have been hacked!</h2>
        </body>
        </html>
        """
        self.wfile.write(html.encode())


server = HTTPServer(('0.0.0.0', 80), Handler)
print("server running on port 80")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\n[!] Stopping server")