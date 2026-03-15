from http.server import HTTPServer, BaseHTTPRequestHandler
import json


# Handles all incoming POST requests and always returns a success response
class MockHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Figure out how many bytes to read from the request body
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        # Just log what came in so we can see it in the terminal
        print(f"POST {self.path}")
        print(f"Body: {body.decode()}")

        # Always respond with success regardless of what was sent
        response = {
            'success': True,
            'message': 'Key confirmed.',
            'remaining_time': '9999 days'
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    # Suppress the default request logging that HTTPServer prints to stdout
    def log_message(self, format, *args):
        pass


if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 80), MockHandler)
    print("Mock server running on port 80...")
    server.serve_forever()
