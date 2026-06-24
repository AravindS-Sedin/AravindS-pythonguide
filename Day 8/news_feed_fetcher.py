# Async News Feed Fetcher
#
# Concepts:
# asyncio, async def, await, asyncio.gather
#
# Real-World App:
# Inshorts / Google News
#
# Problem:
# Fetches news from multiple sources concurrently using asyncio.
# Each source simulates a network request using asyncio.sleep().
# asyncio.gather() runs all fetch operations concurrently in a
# single thread without blocking.
#
# Metrics:
# - Wall Clock Time: Actual async execution time.
# - Sequential Time: Sum of all fetch delays.
#
# Key Learning:
# Async I/O allows thousands of network requests to be handled
# efficiently without creating multiple threads. Total execution
# time is approximately the longest individual request, not the sum.


import asyncio
import time


async def fetch(source: str, delay: float) -> dict:
    
    print(f"[START] Fetching from {source}")

    await asyncio.sleep(delay)

    print(f"[DONE ] {source} fetched in {delay:.1f}s")

    return {
        "source": source,
        "headlines": [
            f"{source} story 1",
            f"{source} story 2"
        ]
    }


async def main():

    sources = [
        ("BBC", 1.5),
        ("Times", 2.0),
        ("Reuters", 1.2)
    ]

    sequential_time = sum(delay for _, delay in sources)

    start = time.perf_counter()

    results = await asyncio.gather(
        fetch("BBC", 1.5),
        fetch("Times", 2.0),
        fetch("Reuters", 1.2)
    )

    end = time.perf_counter()

    print("\nNews Feed")
    print("-" * 40)

    for news in results:
        print(f"\nSource: {news['source']}")
        for headline in news["headlines"]:
            print(f"  • {headline}")

    print("\nPerformance")
    print("-" * 40)
    print(f"Wall Clock Time     : {end - start:.2f}s")
    print(f"Sequential Estimate : {sequential_time:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())