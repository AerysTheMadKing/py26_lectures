import socket

HOST = '127.0.0.1'  # the local host
PORT = 8080  # arbitrary non-privileged port

def handle_request(request):
    """Returns a response for the given HTTP request."""
    headers, body = request.split(b'\r\n\r\n')
    method, path, version = headers.split(b'\r\n')[0].split()
    
    if path == b'/':
        response = b'HTTP/1.1 200 OK\nContent-Type: text/html\n\n<html><body><h1>Welcome to the home page!</h1></body></html>\n'
    elif path == b'/about':
        response = b'HTTP/1.1 200 OK\nContent-Type: text/html\n\n<html><body><h1>About us</h1><p>We are a small web development company.</p></body></html>\n'
    else:
        response = b'HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\n404 Not Found\n'

    return response

def run_server():
    """Starts the server and listens for incoming connections."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind to local host and port
        server_socket.bind((HOST, PORT))
        # Listen for incoming connections
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}...")

        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            print(f"Client connected: {client_address}")

            # Receive request
            request = client_socket.recv(1024)
            print(f"Received request:\n{request.decode()}")

            # Handle request and send response
            response = handle_request(request)
            client_socket.sendall(response)
            print("Response sent.")

            # Close connection
            client_socket.close()
            print(f"Client disconnected: {client_address}\n")

if __name__ == '__main__':
    run_server()