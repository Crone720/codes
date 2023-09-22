import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='j!', intents=intents)

@bot.event
async def on_ready():
	print('YT - JomixCode')
	print('Бот Активный')

@bot.command()
async def hello(ctx):
	member = ctx.author
	await ctx.reply(f'Привет {member.mention}!')

bot.run('you-token')