import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='j!', intents=intents) # в '' вставляете свой префикс

@bot.event
async def on_ready():
	print('YT - JomixCode') # print это то что будет выводится в консоль
	print('Бот Активный')

@bot.command()
async def hello(ctx):
	member = ctx.author # создали переменую что member это ctx.author
	await ctx.reply(f'Привет {member.mention}!')

bot.run('you-token')
