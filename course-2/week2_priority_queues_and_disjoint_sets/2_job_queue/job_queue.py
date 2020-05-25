# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def SiftDown(i, H):
    maxIndex = i
    l = 2 * i + 1
    if l < len(H) and H[l].started_at < H[maxIndex].started_at:
        maxIndex = l
    r = 2 * i + 2
    if r < len(H) and H[r].started_at < H[maxIndex].started_at:
        maxIndex = r

    if l < len(H) and H[l].started_at == H[maxIndex].started_at and H[l].worker < H[maxIndex].worker:
        maxIndex = l
    if r < len(H) and H[r].started_at == H[maxIndex].started_at and H[r].worker < H[maxIndex].worker:
        maxIndex = r

    if i != maxIndex:
        H[i], H[maxIndex] = H[maxIndex], H[i]
        SiftDown(maxIndex, H)


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    H = []
    for i in range(n_workers):
        H.append(AssignedJob(i, 0))
    # print(H[0].started_at)
    for job in jobs:
        result.append(H[0])
        H[0] = (AssignedJob(H[0].worker, H[0].started_at + job))
        SiftDown(0, H)
    return result

    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
