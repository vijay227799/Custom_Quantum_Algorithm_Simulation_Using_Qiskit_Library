import socket

# Server configuration
HOST = 'localhost'
PORT = 12345

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Send the quantum algorithm to the server

#algorithm_text =input("Enter the algorithm you want to simulate")
algorithm_text=input("Enter the basic Algorithm that you want to simulate")
#print(f"Sending algorithm: {algorithm_text}")
client_socket.sendall(algorithm_text.encode())#Security is ensured

# Receive the simulated image from the server
with open('received_simulation.png', 'wb') as image_file:
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        image_file.write(data)

print("Simulation image received and saved as 'received_simulation.png'.")

# Close the connection
client_socket.close()
