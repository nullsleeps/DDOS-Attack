import threading
import socket
import time


target = '127.0.0.1'  # Local server for testing purposes
port = 8080           # Common port for HTTP servers

# Number of concurrent threads and request frequency (adjustable)
num_threads = 10
request_interval = 0.5  # seconds between requests per thread


request_count = 0
request_limit = 100  # Total requests limit

def simulate_request():
    global request_count
    while request_count < request_limit:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((target, port))
                request = f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n"
                s.send(request.encode('utf-8'))
                
                response = s.recv(1024)
                print(f"Received response: {response.decode('utf-8')}")
                
                request_count += 1
                print(f"Request count: {request_count}")
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(request_interval)

threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=simulate_request)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Test completed.")
