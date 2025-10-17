from multiprocessing import Pool
import heapq

def _sort_chunk(chunk):
    return sorted(chunk)

def parallel_sort(data, nproc=2):
    if not data:
        return []

    size = len(data) // nproc
    chunks = [data[i:i+size] for i in range(0, len(data), size)]

    with Pool(processes=nproc) as pool:
        sorted_chunks = pool.map(_sort_chunk, chunks)

    return list(heapq.merge(*sorted_chunks))
