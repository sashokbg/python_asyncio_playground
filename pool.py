from asyncio import Event

from assistant import Assistant


class AssistantPool:
    def __init__(self):
        self.assistants = [Assistant("1"), Assistant("2")]
        self.flag = Event()
        self.flag.set()

    def return_assistant(self, assistant):
        self.assistants.append(assistant)
        self.flag.set()

    async def get_assistant(self):
        await self.flag.wait()
        assistant = self.assistants.pop()
        if not self.assistants:
            self.flag.clear()

        return assistant



