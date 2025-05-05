import socket
import pickle
import pynput.mouse as mouse

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.16.117.100', 5000))  # Bind to your updated IP address
server_socket.listen(1)

print("Waiting for a connection...")
conn, addr = server_socket.accept()
print(f"Connection from: {addr}")

# Function to handle mouse click events
def on_click(x, y, button, pressed):
    if pressed:  # Send data only when a button is pressed
        print(f"Sending coordinates: {(x, y)}")
        data = pickle.dumps((x, y))  # Serialize the data
        conn.send(data)  # Send the coordinates to the client


# Start listening for mouse events
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# Close the connection
conn.close()
server_socket.close()
