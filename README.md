THIS IS FOR EDUCATIONAL PERPOSES ONLY, IF YOU INDEND ON USING THIS FOR THE WRONG PURPOSE I WILL NOT BE RESPONSIBlE FOR YOUR ACTIONS, YOU WILL BE DOING SO AT YOUR OWN RISK.

How To Run:
`Run a local HTTP server`: Use Python’s built-in HTTP server for a quick setup:
```bash
python -m http.server 8080
```
Monitor the Server: Check server logs or responses to observe the effects of the requests.
You can also add more logic to your server to simulate rate-limiting or throttling.

Explanations:
1. `Local Server`: This code targets a server on `127.0.0.1`, which is your local machine.
Run a local server on this IP to observe the effects without impacting any external networks.

2. `Thread and Request Limitations`: By limiting the number of threads and requests, you prevent overloading your system or the server.
The `request_limit` variable caps the total requests to avoid runaway conditions.

3. `Interval Between Requests`: `request_interval` controls the frequency of requests per thread, giving the server a chance to respond and letting you observe how it handles multiple simultaneous connections.

4. `Thread Management`: The code spawns a fixed number of threads, each making requests at intervals.
This simulates load but doesn’t flood the server.

5. `Error Handling`: Including basic error handling provides feedback if the server becomes unresponsive or rejects connections.

Enjoy :)
