#DeprecationWarning: The class qiskit.primitives.sampler.Sampler is deprecated as of qiskit 1.2. 
# It will be removed no earlier than 3 months after the release date. 
# All implementations of the BaseSamplerV1 interface have been deprecated in favor of their V2 counterparts.
#  The V2 alternative for the Sampler class is StatevectorSampler. sampler = Sampler()
#Develop a GuI - it will be helpful
import socket
from qiskit import QuantumCircuit
from qiskit.primitives import Sampler
import matplotlib.pyplot as plt
import re

# Server configuration
HOST = 'localhost'
PORT = 12345

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

#print(f"Server listening on {HOST}:{PORT}")

def parse_algorithm_text(algorithm_text):
    
    
    
    # Split the instructions by ';'
    instructions = algorithm_text.split(';')
    n=len(instructions)
    qc = QuantumCircuit(n)# Initialize a QuantumCircuit with 3 qubits (can adjust if needed)
    for instruction in instructions:
        instruction = instruction.strip()  # Remove leading/trailing spaces
        if not instruction:  # Skip empty instructions
            continue
        if '(' in instruction:
        # Check for gates with angles using regex
            match = re.match(r"([A-Z]+)\(([^)]+)\)\s+(\d+)", instruction)
        
            if match:  # Rotation gate detected
                gate = match.group(1)  # Extract gate (e.g., RX, RY, RZ)
                angle = float(match.group(2))  # Extract angle
                target_qubit = int(match.group(3))  # Extract target qubit
            
            # Apply the appropriate gate
                if gate == 'RX':
                    qc.rx(angle, target_qubit)
                elif gate == 'RY':
                    qc.ry(angle, target_qubit)
                elif gate == 'RZ':
                    qc.rz(angle, target_qubit)
            else:
                raise ValueError(f"Unsupported rotation gate: {gate}")
        else:  # Non-rotation gates
            parts = instruction.split()
            gate = parts[0]  # Gate name
            
            if gate == 'H':  # Hadamard gate
                qc.h(int(parts[1]))
            elif gate == 'X':  # Pauli-X gate
                qc.x(int(parts[1]))
            elif gate == 'Y':  # Pauli-Y gate
                qc.y(int(parts[1]))
            elif gate == 'Z':  # Pauli-Z gate
                qc.z(int(parts[1]))
            elif gate == 'CX':  # Controlled-X (CNOT) gate
                qc.cx(int(parts[1]), int(parts[2]))
            elif gate.lower() == 'measure' and parts[1].lower() == 'all':  # Measure all qubits
                qc.measure_all()
            else:
                raise ValueError(f"Unsupported gate or invalid format: {instruction}")
    
    return qc

 
    

def simulate_and_generate_image(circuit):
    sampler = Sampler()
    job = sampler.run([circuit])
    result = job.result()
    circuit_depth = circuit.depth()
# Extract the statevector and calculate probabilities
    counts = result.quasi_dists[0]

# Generate binary keys (state labels)
    

    print(counts)

    fig,ax = plt.subplots()
    plt.plot(counts.keys(),counts.values())
    plt.xlabel('States')
    plt.ylabel('Counts')
    ax.text(0.5, 0.95, f'Circuit Depth(Efficiency): {circuit_depth}', transform=ax.transAxes, fontsize=12, verticalalignment='top', horizontalalignment='center')
    plt.title('Quantum Simulation Results')
    plt.show()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(counts.keys(), counts.values(), color='skyblue', width=0.6)
    ax.set_xlabel('Quantum States', fontsize=14)
    ax.set_ylabel('Probability', fontsize=14)
    ax.set_title('Quantum Circuit Simulation Results', fontsize=16)
    ax.text(0.5, 0.95, f'Circuit Depth(Efficiency): {circuit_depth}', transform=ax.transAxes, fontsize=12, verticalalignment='top', horizontalalignment='center')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    image_path = 'simulation_result.jpeg'
    plt.savefig(image_path)
    plt.close()

    return image_path

while True:
    client_conn, client_addr = server_socket.accept()
    #print(f"Connection from {client_addr}")

    # Receive algorithm text from the client
    algorithm_text = client_conn.recv(1024).decode()
    
    print(f"Received algorithm: {algorithm_text}")

    try:
        # Parse and simulate the quantum circuit
        circuit = parse_algorithm_text(algorithm_text)
        image_path = simulate_and_generate_image(circuit)

        # Send the image to the client
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        #client_conn.sendall(image_data)
        #print("Image sent to the client successfully.")
    except Exception as e:
        print(f"Error: {e}")
        #client_conn.sendall(b"Error processing request.")

    client_conn.close()