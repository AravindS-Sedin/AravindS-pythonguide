# Multiprocessing Image Processor
#
# Concepts:
# multiprocessing, Pool, cpu_count, GIL, CPU-bound processing
#
# Real-World App:
# Adobe Photoshop / Canva / Snapseed
#
# Problem:
# Simulates image processing by performing heavy CPU computations.
# Compares single-process execution with multiprocessing.Pool.
# Pool.map() distributes work across multiple CPU cores to achieve
# parallel execution and reduce total processing time.
#
# Metrics:
# - Single Process Time
# - Multi-Process Time
# - Speedup Ratio
#
# GIL:
# Python's Global Interpreter Lock (GIL) allows only one thread to
# execute Python bytecode at a time. Therefore, threading does not
# improve CPU-bound tasks significantly. Multiprocessing bypasses the
# GIL by creating separate Python processes, each with its own
# interpreter and GIL.


import multiprocessing
import time


def apply_filter(image_name):
    
    result = sum(i ** 2 for i in range(10_000_000))

    process_name = multiprocessing.current_process().name

    return (
        f"Processed: {image_name:<15} "
        f"Checksum: {result % 9999:<5} "
        f"Process: {process_name}"
    )


def single_process(images):

    start = time.perf_counter()

    results = [apply_filter(img) for img in images]

    end = time.perf_counter()

    return results, end - start


def multi_process(images):

    start = time.perf_counter()

    with multiprocessing.Pool(
        processes=multiprocessing.cpu_count()
    ) as pool:

        results = pool.map(apply_filter, images)

    end = time.perf_counter()

    return results, end - start


def main():

    images = [
        f"photo_{i:03d}.jpg"
        for i in range(1, 13)
    ]

    print(f"CPU Cores Available: {multiprocessing.cpu_count()}\n")

    print("Running Single Process Benchmark...")
    single_results, single_time = single_process(images)

    print("\nRunning Multi-Process Benchmark...")
    multi_results, multi_time = multi_process(images)

    speedup = single_time / multi_time

    print("\nSample Results")
    print("-" * 60)

    for result in multi_results[:5]:
        print(result)

    print("\nPerformance Comparison")
    print("-" * 60)

    print(f"Single Process Time : {single_time:.2f}s")
    print(f"Multi Process Time  : {multi_time:.2f}s")
    print(f"Speedup             : {speedup:.2f}x")


if __name__ == "__main__":
    main()