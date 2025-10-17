from zad02 import parallel_sort
import time
import random
import matplotlib.pyplot as plt

def benchmark():
    sizes = [1_000, 2_000, 4_000, 8_000, 10_000, 20_000]
    processes = [1, 2, 4, 8, 16, 32]
    results = {}

    for x in sizes:
        data = [random.randint(0, 10**6) for _ in range(x)]
        results[x] = {}
        for p in processes:
            start = time.time()
            parallel_sort(data, nproc=p)
            elapsed_time = time.time() - start
            results[x][p] = elapsed_time
            print(f"size={x}, procs={p}, time={elapsed_time:.3f}s")

    for x in sizes:
        plt.plot(processes, [results[x][p] for p in processes], marker="o", label=f"n={x}")
    plt.xlabel("Number of processes")
    plt.ylabel("Time [s]")
    plt.title("Parallel sort benchmark")
    plt.legend()
    plt.show()

# demo
if __name__ == "__main__":
    benchmark()
