<h1 align="center">⚛️ Custom Quantum Gates Simulation</h1>

<p align="center">
  <b>A Streamlit-powered interactive platform to design, simulate, and visualize custom quantum circuits using Qiskit.</b>
</p>

<hr>

<h2>📌 Overview</h2>
<p>
This repository provides a <b>Quantum Circuit Simulation Tool</b> built with <code>Qiskit</code>, <code>Matplotlib</code>, and <code>Streamlit</code>. 
It allows users to define algorithms in plain text, automatically parse them into quantum circuits, and visualize the simulation results.
</p>

<hr>

<h2>✨ Key Features</h2>
<ul>
  <li>🖥️ <b>Interactive GUI</b> – Built with <code>Streamlit</code> for seamless user experience.</li>
  <li>⚛️ <b>Custom Gate Parsing</b> – Supports Hadamard, Pauli (X, Y, Z), CNOT, and rotation gates (RX, RY, RZ).</li>
  <li>📊 <b>Simulation Engine</b> – Uses Qiskit <code>Sampler</code> to evaluate quantum states and probabilities.</li>
  <li>📈 <b>Visual Output</b> – Generates bar charts and plots of quantum state distributions.</li>
  <li>🔍 <b>Efficiency Metrics</b> – Displays circuit depth as a measure of computational efficiency.</li>
  <li>📷 <b>Image Export</b> – Saves simulation results as JPEG for easy sharing and documentation.</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li><b>Languages:</b> Python</li>
  <li><b>Libraries:</b> Qiskit, Matplotlib, PIL, Regex</li>
  <li><b>Framework:</b> Streamlit (for GUI)</li>
</ul>

<hr>

<h2>⚙️ Usage</h2>

<h3>1️⃣ Run the Streamlit App</h3>
<pre>
streamlit run main.py
</pre>

<h3>2️⃣ Enter Algorithm Instructions</h3>
<p>
Provide quantum gate instructions in text format (semicolon-separated). Examples:
</p>
<pre>
H 0; CX 0 1; RX(1.57) 2; Measure All
</pre>

<h3>3️⃣ Visualize Results</h3>
<p>
The app will:
</p>
<ul>
  <li>Parse instructions into a <code>QuantumCircuit</code></li>
  <li>Simulate using Qiskit <code>Sampler</code></li>
  <li>Display probability distributions and circuit efficiency</li>
  <li>Export results as <code>simulation_result.jpeg</code></li>
</ul>

<hr>

<h2>📂 Repository Structure</h2>
<pre>
├── Quantum.py             # Core simulation and Streamlit GUI
├── simulation_result.jpeg # Example output image
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
</pre>

<hr>

<h2>🔮 Future Scope</h2>
<ul>
  <li>🤖 <b>Advanced Gate Support</b> – Add Toffoli, SWAP, and parameterized custom gates.</li>
  <li>📊 <b>Enhanced Analytics</b> – Provide fidelity, entanglement measures, and performance benchmarks.</li>
  <li>🎨 <b>Interactive Visualizations</b> – Real-time circuit diagrams with drag-and-drop gate placement.</li>
</ul>

<hr>


