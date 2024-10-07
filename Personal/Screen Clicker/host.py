import socket
import pickle
import threading
import pyautogui
import pynput.mouse as mouse
import tkinter as tk
from PIL import Image, ImageTk
import io

# Create the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.16.112.44', 5000))  # Bind to your updated IP address
server_socket.listen(1)

print("Waiting for a connection...")
conn, addr = server_socket.accept()
print(f"Connection from: {addr}")

# Function to display the screenshots
def receive_and_display_screenshots():
    root = tk.Tk()
    label = tk.Label(root)
    label.pack()

    while True:
        try:
            # Receive the data from the client
            data = conn.recv(1024 * 64)  # Adjust buffer size for large images
            if not data:
                break
            event_type, img_data = pickle.loads(data)
            if event_type == 'screenshot':
                # Convert the image data back to an image
                img = Image.open(io.BytesIO(img_data))
                img_tk = ImageTk.PhotoImage(img)

                # Update the Tkinter window with the new image
                label.config(image=img_tk)
                label.image = img_tk  # Keep a reference to avoid garbage collection

            root.update_idletasks()
            root.update()
        except Exception as e:
            print(f"Error receiving screenshot: {e}")
            break

# Start the screenshot receiving thread
screenshot_thread = threading.Thread(target=receive_and_display_screenshots)
screenshot_thread.daemon = True
screenshot_thread.start()

# Continue listening for mouse click events like before
def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:  # If left button is pressed
        print(f"Sending coordinates: {(x, y)}")
        data = pickle.dumps((x, y))  # Serialize the data
        conn.send(data)  # Send the coordinates to the client

with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# Close the connection
conn.close()
server_socket.close()
