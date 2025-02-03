import socket
import pickle
import threading
import pynput.mouse as mouse
from PIL import Image, ImageTk
import io
import tkinter as tk

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print("Binding the server to IP and port...")
    server_socket.bind(('172.16.112.44', 5000))  # Bind to your updated IP address
    print("Server bound to IP and port.")
    server_socket.listen(1)
    print("Waiting for a connection...")
    conn, addr = server_socket.accept()
    print(f"Connection from: {addr}")
except Exception as e:
    print(f"Error setting up server: {e}")
    server_socket.close()
    exit()

# Function to handle mouse click events
def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:  # If left button is pressed
        print(f"Sending coordinates: {(x, y)}")
        try:
            data = pickle.dumps((x, y))  # Serialize the data
            conn.send(data)  # Send the coordinates to the client
        except Exception as e:
            print(f"Error sending coordinates: {e}")
            return False  # Stop the listener on error

# Function to receive data from the client
def receive_screenshots():
    buffer = b''  # Buffer to hold incoming screenshot data
    while True:
        try:
            print("Waiting to receive screenshots...")
            # Receive data from the client
            chunk = conn.recv(4096)
            if not chunk:
                print("No more data from the client, closing connection.")
                break
            buffer += chunk

            # Check if we have a complete pickle object
            try:
                event_type, img_data = pickle.loads(buffer)
                if event_type == 'screenshot':
                    print("Received screenshot data.")
                    buffer = b''  # Clear buffer for next image
                    
                    # Load the image from the byte data and display it
                    img = Image.open(io.BytesIO(img_data))
                    update_screen(img)  # Update the displayed image
            except pickle.UnpicklingError:
                # Incomplete pickle data, continue to gather more
                pass

        except Exception as e:
            print(f"Error receiving screenshot: {e}")
            break

# Function to update the screen with the received image
def update_screen(img):
    global label, root
    img_tk = ImageTk.PhotoImage(img)
    label.config(image=img_tk)
    label.image = img_tk  # Keep a reference to avoid garbage collection

# Start receiving screenshots in a separate thread
try:
    screenshot_thread = threading.Thread(target=receive_screenshots)
    screenshot_thread.daemon = True
    screenshot_thread.start()
    print("Started screenshot receiving thread.")
except Exception as e:
    print(f"Error starting screenshot thread: {e}")

# Start the mouse listener for clicks
try:
    print("Starting mouse listener...")
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    print("Mouse listener started.")
except Exception as e:
    print(f"Error with mouse listener: {e}")

# Close the connection when done
def close_connection():
    print("Closing connection...")
    conn.close()
    server_socket.close()
    print("Connection closed.")

# Tkinter window to display the client's screen
root = tk.Tk()
root.title("Client's Screen")
label = tk.Label(root)
label.pack()

# Bind the window close event to close the socket
root.protocol("WM_DELETE_WINDOW", close_connection)

# Start the Tkinter mainloop (for displaying the screen)
root.mainloop()
