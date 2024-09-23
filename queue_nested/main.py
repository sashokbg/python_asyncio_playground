import asyncio

from queue_nested.run import Run


async def producer(queue: asyncio.Queue, runs):
    for run in runs:
        print("Putting an item in the queue... ")
        await queue.put(run)
        print(f"done putting {run}")
    await queue.put(None)

async def process_item(run):
    await run.execute()

async def task_pool(queue: asyncio.Queue):
    active_tasks = []
    max_concurrent = 2

    while True:
        while len(active_tasks) < max_concurrent:
            item = await queue.get()

            if item is None:
                break

            task = asyncio.create_task(process_item(item))
            active_tasks.append(task)

        if active_tasks:
            done, pending = await asyncio.wait(active_tasks, return_when=asyncio.FIRST_COMPLETED)

            active_tasks = [task for task in pending]
            queue.task_done()

        if len(active_tasks) == 0 and queue.empty():
            break


async def main():
    queue = asyncio.Queue(maxsize=2)
    runs = [
        Run(f"run-1"),
        Run(f"run-2"),
        Run(f"run-3"),
        Run(f"run-4"),
    ]

    await asyncio.gather(
        producer(queue, runs),
        task_pool(queue),
    )

    print("All done!")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
