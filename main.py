import asyncio
import logging
from asyncio import sleep
from sqlalchemy import select
import os
from config import TOKEN
from data import db_session
from data.wards import Wards
from counter_func import get_counterpick_function
from meta_func import get_meta
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

db_session.global_init("db/wards.db")


class DotaInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='counterpick')
    async def get_counterpick(self, ctx, hero_name: str):
        first_line = f'Контрпики для героя {hero_name}: \n'
        counter_list = get_counterpick_function(hero_name)
        result_line = first_line + '\n'.join(counter_list)
        await ctx.send(result_line)

    @commands.command(name='meta')
    async def get_meta(self, ctx, position: str):
        position_list = ['mid', 'hardsup', 'carry', 'fullsup', 'offlane', '1', '2', '3', '4', '5', 'кери', 'керри',
                         'мид', 'мидер', 'оффлейнер', 'тройка', 'пятерка', 'четверка']
        if position.lower() not in position_list:
            error_line = 'Пожалуйста, используйте обозначение позиций предоставленные ниже:'

            await ctx.send(error_line + '\n' + ', '.join(position_list))
        else:
            meta_list = get_meta(position)
            for hero in meta_list:
                hero_name, hero_winrate = hero
                result_line = f'Герой: {hero_name}, винрейт: {hero_winrate}'
                await ctx.send(result_line)

    @commands.command(name='wards')
    async def get_wards_spots(self, ctx, side: str, region: str):
        region_list = ['safe_forest', 'hard_forest']
        if side not in ['dire', 'radiant']:
            await ctx.send('Пожалуйста, при указании стороны используйте dire или radiant')
        elif region not in region_list:
            await ctx.send(f'Пожалуйста, при указании места используйте: {" или ".join(region_list)}')
        else:
            db_sess = db_session.create_session()
            result = db_sess.execute(
                select(Wards.folder_path)
                    .where(Wards.side == side, Wards.name_of_map_piece == region)
            )
            wards_spots = result.one()[0]
            ward_image_names = os.listdir(wards_spots)
            print(ward_image_names)
            for image in ward_image_names:
                picture = discord.File(wards_spots + r'/' + image)
                await ctx.send(file=picture)

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


async def main():
    await bot.add_cog(DotaInfo(bot))
    await bot.start(TOKEN)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
