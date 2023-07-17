# WebSocket Stress Test

This project implements a WebSocket stress test script using Python's websocket library. It allows you to establish multiple WebSocket connections to a specified URL and measure the connection time for each connection. This can be useful for testing the performance and scalability of WebSocket servers.
Requirements

To run this script, you need to have the following installed:

    Python 3.x
    websocket library (pip install websocket)

Usage

    Clone the repository or download the source code.

    Install the required dependencies by running the following command:

pip install websocket

Open the stress_test.py file and modify the url and num_connections variables in the main function to match your WebSocket server URL and the number of connections you want to establish.

Run the script by executing the following command:

python stress_test.py

The script will initiate multiple WebSocket connections to the specified URL and measure the connection time for each connection. Once all connections have been established and closed, the average connection time will be displayed.

Customize the on_open, on_message, on_error, and on_close methods in the WebSocketStressTest class according to your requirements. These methods provide hooks for handling various events during the WebSocket connections.