import socket
import pickle
import pyautogui
import threading
import time
from PIL import ImageGrab  # Used to capture the screen
import io

# Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Try to connect to the server
    print("Attempting to connect to server...")
    client_socket.connect(('172.16.112.44', 5000))  # Connect to your updated IP address
    print("Connected to the server.")
except Exception as e:
    print(f"Error connecting to server: {e}")
    exit()  # Exit if connection fails

pyautogui.FAILSAFE = False

# Function to capture and send the screen to the host
def send_screenshots():
    while True:
        try:
            print("Capturing screenshot...")
            # Capture the screen using ImageGrab
            screenshot = ImageGrab.grab()
            # Convert the screenshot to bytes
            img_bytes = io.BytesIO()
            screenshot.save(img_bytes, format='JPEG')
            img_data = img_bytes.getvalue()

            # Send the image data
            data = pickle.dumps(('screenshot', img_data))
            client_socket.sendall(data)
            
            print("Screenshot sent.")
            time.sleep(0.1)  # Send every 100ms (adjustable based on speed)
        except Exception as e:
            print(f"Error sending screenshot: {e}")
            break

# Start the screenshot sending thread
screenshot_thread = threading.Thread(target=send_screenshots)
screenshot_thread.daemon = True  # Ensure thread closes when main program exits
screenshot_thread.start()

# Continue handling mouse events like before
running = True
while running:
    try:
        # Receive the data (mouse coordinates)
        data = client_socket.recv(1024)
        if not data:
            break
        mouse_pos = pickle.loads(data)  # Deserialize the data
        print(f"Received coordinates: {mouse_pos}")
        # Simulate left-click at the received position on the client
        pyautogui.click(mouse_pos[0], mouse_pos[1])
    except Exception as e:
        print(f"Error: {e}")
        running = False

# Close the connection
client_socket.close()
