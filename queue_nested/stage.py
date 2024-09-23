import asyncio
from random import randrange


class Stage:
    def __init__(self, name):
        self.name = f"stage-{name}"
        self.finished = False

    async def execute(self):
        print(f"\t\tStarting stage {self.name}")
        # duration = randrange(5)
        duration = 2
        await asyncio.sleep(duration)
        print(f"\t\tFinished stage {self.name}")
        self.finished = True
