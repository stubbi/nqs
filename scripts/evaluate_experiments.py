import subprocess, os, errno
from experiments_settings import experiment_name, randomRestarts, optimizer, number_of_qubits, number_of_cycles, number_of_circuits, number_of_nodes, number_of_tasks_per_node, number_of_omp_threads, number_of_training_samples, number_of_training_iterations, number_of_initial_hidden_units, number_of_sample_steps, number_of_runs, earlyStopping, learnCZ

noctua_user = 'hpc-prf-nqs'
email = 'stubbi@mail.upb.de'
singularity_image_location = "{pc2pfs}/{noctua_user}/nqs.sif".format(
                        noctua_user=noctua_user,
                        pc2pfs=os.environ["PC2PFS"])

epxperiment_folder = "{pc2pfs}/{noctua_user}/{experiment_name}".format(noctua_user=noctua_user,
                                    pc2pfs=os.environ["PC2PFS"],
                                    experiment_name=experiment_name)


batch_script ="""#!/bin/bash
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -J {experiment_name}-evaluation
#SBATCH -A {noctua_user}
#SBATCH -p batch
#SBATCH -t 12:00:00
#SBATCH --mail-type fail
#SBATCH --mail-user {email}
export OMP_NUM_THREADS=1

module reset
module load vis/matplotlib
module load singularity
mpirun --mca mpi_warn_on_fork 0 singularity exec {singularity_image_location} python2.7 $HOME/nqs/scripts/evaluation.py {epxperiment_folder} {number_of_qubits} {number_of_cycles} {number_of_circuits} {listOMPNodes} {listOMPTasks} {listOMPThreads} {listSamples} {listIterations} {listInitialHidden} {listSampleSteps} {numRuns} {randomRestarts} {earlyStopping} {optimizer} {learnCZ}> evaluation_out 2> evaluation_err""".format(
                        epxperiment_folder=epxperiment_folder,
                        experiment_name=experiment_name,
                        noctua_user=noctua_user,
                        email=email,
                        number_of_qubits=','.join(map(str, number_of_qubits)),
                        number_of_cycles=','.join(map(str, number_of_cycles)),
                        number_of_circuits=number_of_circuits,
                        listOMPNodes=','.join(map(str, number_of_nodes)),
                        listOMPTasks=','.join(map(str, number_of_tasks_per_node)),
                        listOMPThreads=','.join(map(str, number_of_omp_threads)),
                        listSamples=','.join(map(str, number_of_training_samples)),
                        listIterations=','.join(map(str, number_of_training_iterations)),
                        listInitialHidden=','.join(map(str, number_of_initial_hidden_units)),
                        listSampleSteps=','.join(map(str, number_of_sample_steps)),
                        numRuns=number_of_runs,
                        singularity_image_location=singularity_image_location,
                        randomRestarts=randomRestarts,
                        earlyStopping=earlyStopping,
                        optimizer=optimizer,
                        learnCZ=learnCZ
                        )

f = open("{epxperiment_folder}/evaluation.slurm".format(epxperiment_folder=epxperiment_folder),'w')
print >>f, batch_script

bashCommand = "sbatch -D {epxperiment_folder} {epxperiment_folder}/evaluation.slurm".format(epxperiment_folder=epxperiment_folder)
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)