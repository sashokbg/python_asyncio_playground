from queue_nested.stage import Stage


class Run:
    def __init__(self, name):
        self.name = name
        self.stages = [Stage(name), Stage(name)]
        self.finished = False

    async def execute(self):
        print(f"\texecuting run {self.name}")
        for stage in self.stages:
            await stage.execute()
        print(f"\tFinished run {self.name}")
        self.finished = True

def __str__(self):
    return f"""
{self.name}
"""
