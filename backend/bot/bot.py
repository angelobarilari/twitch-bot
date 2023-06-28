from twitchio.ext.commands import command, Context, Bot
# from .commands.commands import cmd_question, generate_verse
from commands.commands import cmd_question, generate_verse

import asyncpg
import asyncio
import dotenv

dotenv.load_dotenv()


# Database connection
async def db_connection():
    connection = await asyncpg.connect(
        user="postgres",
        password="1234",
        database="twitchbot",
        host="localhost",
        port="5432",
    )

    return connection


class Bot(Bot):
    def __init__(self):
        super().__init__(
            # Put your OAuth Password Token here. You can obtain one in https://twitchapps.com/tmi/
            token="oauth:n8te1ql5ebcq3ai2hok5rivyxoffkz",
            prefix="!"
        )

        self.db_connection = None

    async def event_ready(self):
        # self.db_connection = await db_connection()
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")
        print("bot is running")

        await asyncio.sleep(2)
        await self.join_channels(["reppukk"])
        
    async def event_channel_joined(self, channel):
        print(f"Bot connected in {channel.name}")

    async def event_message(self, message):
        if message.echo:
            return

        await self.handle_commands(message)

    @command(name="pergunta")
    async def cmd_question(self, ctx: Context):
        await cmd_question(ctx)

    @command(name="verso")
    async def generate_verse(self, ctx: Context):
        await generate_verse(ctx)


twitchverse = Bot()
twitchverse.run()
