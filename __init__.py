import GoldyBot

class Example(GoldyBot.Extension):
    def __init__(self):
        super().__init__()

    @GoldyBot.command(description = "A command that says hello duhhhh.")
    async def hello(self, platter: GoldyBot.GoldPlatter):
        await platter.send_message("👋 Hello", reply = True)


load = lambda: Example()