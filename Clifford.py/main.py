import discord
from discord.ext import commands
import asyncio
import datetime
import sys
import traceback
import sqlite3

bot = commands.Bot(command_prefix='.', case_insensitive=True)

@bot.event
async def on_ready():
    print('Ich bin Online')
    return await bot.change_presence(activity=discord.Game(type=1, name='Clifford Version 0.2 (WIP)'))

initial_extensions = ['cogs.moderation',
                      'cogs.welcome',
                      'cogs.leveling',
                      'cogs.help']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Fehler beim laden der Erweiterung! {extension}', file=sys.stderr)
            traceback.print_exc()





bot.run("Njk3NTM1MTIyNzE0Mzk0NzI0.Xo8vsA.tR1BTycE8xxmroKw-R_Erq4X864")