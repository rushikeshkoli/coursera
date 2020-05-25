import filecmp
import os

f1 = os.getcwd() + "/week2_priority_queues_and_disjoint_sets/2_job_queue/tests/02.a"
f2 = os.getcwd() + "/week2_priority_queues_and_disjoint_sets/2_job_queue/tests/temp.a"

print(filecmp.cmp(f1, f2, shallow=False))