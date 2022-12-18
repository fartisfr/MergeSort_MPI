# How to run
# mpiexec -n 4 python mergesort_mpi.py matrix_size

# Example
# mpiexec -n 4 python mergesort_mpi.py 1000000

from mpi4py import MPI
import numpy as np
import sys

# Get the number of processors and the rank of the current processor
comm = MPI.COMM_WORLD
num_procs = comm.Get_size()
rank = comm.Get_rank()

# Get matrix size from terminal argument
matrix_size = int(sys.argv[1])


# Random an array with seeder
np.random.seed(0)
items = np.random.randint(size=matrix_size, low=0, high=100)


# Calculate time
start = MPI.Wtime()

# Split the list of items into num_procs sublists
sublist_size = len(items) // num_procs
sublist = items[rank*sublist_size:(rank+1)*sublist_size]


# Sort the sublist
sublist.sort()

merged_list = comm.gather(sublist, root=0)

if rank == 0:
    merged_list = [item for sublist in merged_list for item in sublist]
    merged_list.sort()
    # Calculate time
    end = MPI.Wtime()
    print("Time: ", end - start)
