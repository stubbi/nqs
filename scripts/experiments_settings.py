experiment_name = 'sr-2'
circuit_generator_script = 'random_circuit.py'
# parameters to be tested
number_of_qubits = [4,5,6]
number_of_cycles = [5,10,15]
number_of_circuits = 3 #number of random circuits with same number of qubits and cycles

number_of_nodes = [1]
number_of_tasks_per_node = [1]
number_of_omp_threads = [1]

number_of_training_samples = [10 + i * 20 for i in range(5)] 
number_of_training_iterations = [1000 + i * 2000 for i in range(5)]

number_of_initial_hidden_units = [q*(q-1)/2.0 for q in number_of_qubits]
number_of_sample_steps = [q if q%2 != 0 else q+1 for q in number_of_qubits]
number_of_runs = 3 #number of runs for a specific circuit

randomRestarts = 10
earlyStopping = True
optimizer = 'AdaMax'
