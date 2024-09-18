import asyncio

from assistant import Assistant
from pool import AssistantPool

pool = AssistantPool()

assistant1 = None
assistant2 = None

async def return_assistant():
    await asyncio.sleep(3)
    print("Returning assistant")
    pool.return_assistant(assistant1)

async def work():
    global assistant1
    assistant1 = await pool.get_assistant()
    print(f"Got assistant {assistant1.name}")


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    gather = asyncio.gather(
        work(),
        work(),
        return_assistant(),
        work()
    )
    loop.run_until_complete(gather)

    print("finished")

