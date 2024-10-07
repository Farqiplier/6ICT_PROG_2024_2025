import socket
import pickle
import threading
import pyautogui
import pynput.mouse as mouse
import time

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.16.112.44', 5000))  # Bind to your updated IP address
server_socket.listen(1)

print("Waiting for a connection...")
conn, addr = server_socket.accept()
print(f"Connection from: {addr}")

# Function to send the mouse position every 1ms
def send_mouse_position():
    while True:
        try:
            x, y = pyautogui.position()  # Get current mouse position
            data = pickle.dumps(('move', (x, y)))  # Serialize the movement data
            # Prefix each message with a fixed-length header indicating the size of the message
            message = bytes(f"{len(data):<10}", 'utf-8') + data
            conn.sendall(message)  # Send the mouse position to the client
            time.sleep(0.001)  # Wait for 1ms
        except Exception as e:
            print(f"Error sending mouse position: {e}")
            break

# Function to handle left-click events
def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:  # If left button is pressed
        print(f"Sending left-click coordinates: {(x, y)}")
        data = pickle.dumps(('click', (x, y)))  # Serialize the click event
        # Prefix each message with a fixed-length header indicating the size of the message
        message = bytes(f"{len(data):<10}", 'utf-8') + data
        conn.sendall(message)  # Send the left-click coordinates to the client

# Start the mouse position thread
position_thread = threading.Thread(target=send_mouse_position)
position_thread.daemon = True  # Ensure thread closes when main program exits
position_thread.start()

# Start listening for mouse click events
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# Close the connection
conn.close()
server_socket.close()
