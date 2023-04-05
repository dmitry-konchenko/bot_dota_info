import asyncio
import logging
from asyncio import sleep

from counter_func import get_counterpick_function
import discord
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']


class DotaInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='get_counterpick')
    async def get_counterpick(self, ctx, hero_name: str):
        first_line = f'Контрпики для героя {hero_name}: \n'
        counter_list = get_counterpick_function(hero_name)
        result_line = first_line + '\n'.join(counter_list)
        await ctx.send(result_line)

    @commands.command(name='roshan')
    async def wait_roshan_time(self, ctx):
        await ctx.send('Таймер респавна Рошана запущен')
        min_line = 'Прошло минимальное время респавна рошана'
        max_line = 'Рошан точно заспавнился'
        await sleep(480)
        await ctx.send(min_line)
        await sleep(240)
        await ctx.send(max_line)


bot = commands.Bot(command_prefix='/', intents=intents)

TOKEN = "MTA5MTY4MTY4OTQ2NzYyOTY1OA.Gsoynj.Ni0Lk0l3yjd7IhPD7PvSyypyXxU7hr-FyDb0ug"


async def main():
    await bot.add_cog(DotaInfo(bot))
    await bot.start(TOKEN)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
