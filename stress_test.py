import websocket
import concurrent.futures
import time


class WebSocketStressTest:
    def __init__(self, url, num_connections):
        self.url = url
        self.num_connections = num_connections
        self.connection_times = []

    def establish_connection(self, _):
        start_time = time.time()
        ws = websocket.WebSocketApp(
            self.url,
            on_open=lambda ws: self.on_open(ws, start_time),
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            # header={'Authorization': 'Token '}
        )
        ws.run_forever(sslopt={"do_handshake_on_connect": False})
        
    def on_open(self, ws, start_time):
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.connection_times.append(elapsed_time)
        print(f"WebSocket connection established. Elapsed Time: {elapsed_time:.4f} seconds")

        # Perform any necessary actions or send messages on the WebSocket connection here
        ws.close()

    def on_message(self, ws, message):
        # Handle received messages if needed
        pass

    def on_error(self, ws, error):
        print(f"WebSocket connection error: {error}")
        ws.close()

    def on_close(self, ws, status_code, _):
        print("WebSocket connection closed")
        ws.close()


    def perform_stress_test(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.establish_connection, range(self.num_connections))
        
        # self.on_close()
        if len(self.connection_times) > 0:
            avg_time = sum(self.connection_times) / len(self.connection_times)
            print(f"Average time per WebSocket connection: {avg_time:.4f} seconds")


def main():
    url = "ws://127.0.0.1:8000/ws/chatroom/1/"
    num_connections = 20000

    stress_test = WebSocketStressTest(url, num_connections)
    print("Start the stress test")
    stress_test.perform_stress_test()


if __name__ == '__main__':
    main()
