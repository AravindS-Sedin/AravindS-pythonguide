# Multi-Threaded File Downloader
#
# Concepts:
# threading, ThreadPoolExecutor, Lock, concurrent execution
#
# Real-World App:
# IDM / Chrome Downloads
#
# Problem:
# Downloads multiple files concurrently using threads. Each download
# sleeps for a random duration (1–4 seconds) to simulate network latency.
# A Lock protects the shared completed list from race conditions.
# All download tasks are started first and then awaited for completion.
#
# To Display:
# - Completed downloads
# - Wall-clock time (actual concurrent execution time)
# - Sequential estimate (time if downloads ran one after another)


from concurrent.futures import ThreadPoolExecutor
import threading
import random
import time


completed = []
delays = []
lock = threading.Lock()


def download_file(filename, size_mb):

    delay = random.uniform(1, 4)

    with lock:
        delays.append(delay)

    print(
        f"[START] {filename} "
        f"on {threading.current_thread().name}"
    )

    time.sleep(delay)

    with lock:
        completed.append(filename)

    print(f"[DONE ] {filename} in {delay:.2f}s")


def main():

    files = [
        ("report.pdf", 5),
        ("video.mp4", 120),
        ("image.jpg", 2),
        ("data.csv", 15),
    ]

    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=3) as executor:

        futures = []

        for filename, size in files:
            futures.append(
                executor.submit(download_file, filename, size)
            )

        for future in futures:
            future.result()

    end = time.perf_counter()

    wall_clock = end - start
    sequential_estimate = sum(delays)

    print("\nCompleted:", completed)
    print(f"Wall Clock Time     : {wall_clock:.2f}s")
    print(f"Sequential Estimate : {sequential_estimate:.2f}s")


if __name__ == "__main__":
    main()




# import threading
# import time
# import random


# # Shared resources
# completed = []
# lock = threading.Lock()


# def download_file(filename, size_mb):
#     """
#     Simulate downloading a file.
#     """

#     delay = random.uniform(1, 4)

#     print(
#         f"[START] {filename:<12} "
#         f"({size_mb} MB) "
#         f"on {threading.current_thread().name}"
#     )

#     time.sleep(delay)

#     # Critical section
#     with lock:
#         completed.append(filename)

#     print(f"[DONE ] {filename:<12} completed in {delay:.2f}s")


# def sequential_estimate(files):

#     return len(files) * 2.5   # average sleep ≈ 2.5 sec


# def main():

#     files = [
#         ("report.pdf", 5),
#         ("video.mp4", 120),
#         ("image.jpg", 2),
#         ("data.csv", 15),
#     ]

#     threads = []

#     start_time = time.perf_counter()

#     # Create threads
#     for filename, size in files:
#         thread = threading.Thread(
#             target=download_file,
#             args=(filename, size),
#             name=f"Downloader-{filename}"
#         )
#         threads.append(thread)

#     # Start ALL threads first
#     for thread in threads:
#         thread.start()

#     # Then join ALL threads
#     for thread in threads:
#         thread.join()

#     end_time = time.perf_counter()

#     print("\nCompleted Files:")
#     print(completed)

#     wall_clock_time = end_time - start_time

#     print(f"\nWall Clock Time : {wall_clock_time:.2f} sec")
#     print(
#         f"Sequential Estimate : "
#         f"{sequential_estimate(files):.2f} sec"
#     )


# if __name__ == "__main__":
#     main()