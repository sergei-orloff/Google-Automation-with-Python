#!/usr/bin/env python3


import subprocess

src = "/data/prod/"   # It is the source directory
dest = "/data/prod_backup/"  # It is the destination directory

subprocess.call(["rsync", "-arq", src, dest])

# ===========================================

#!/usr/bin/env python3


from multiprocessing import Pool

def run(task):
  # Do something with task here
  print("Handling {}".format(task))

if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)
