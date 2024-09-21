import asyncio
from asyncio import ensure_future

counter = 0

async def consumer(queue: asyncio.Queue):
    print("Consuming an item from the queue..")
    await asyncio.sleep(4)
    item = await queue.get()
    print(f"done consuming {item}")

async def producer(queue: asyncio.Queue):
    print("Putting an item in the queue... ")

    global counter
    item = f"ITEM-{counter}"
    await queue.put(item)
    print(f"done putting {item}")

    counter += 1

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    queue = asyncio.Queue(maxsize=2)

    all_tasks = asyncio.gather(
        ensure_future(producer(queue)),
        ensure_future(producer(queue)),
        ensure_future(producer(queue)),
        ensure_future(consumer(queue))
    )

    loop.run_until_complete(all_tasks)

