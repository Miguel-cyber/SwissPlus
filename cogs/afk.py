import discord
from discord.ext import commands
from discord.ext.commands import BotMissingPermissions, bot_has_permissions

import json

class AFK(commands.Cog):

  def __init__(self, bot):

    self.bot = bot



  @commands.Cog.listener()
  async def on_message(self, msg):

    if msg.author.bot:

      return

    file = open("afk.json", "r")

    afk = json.load(file)

    if not str(msg.guild.id) in afk:

      return

    if len(msg.mentions) > 0:

      user = msg.mentions[0]

      if user.id in afk[str(msg.guild.id)]["to-mention-ids"]:

        msgs = f"{user} is currently AFK: `{afk[str(msg.guild.id)][str(user.id)]}`"

        await msg.channel.send(msgs, delete_after=5)

    if msg.author.id in afk[str(msg.guild.id)]["to-mention-ids"]:

      index = afk[str(msg.guild.id)]["to-mention-ids"].index(msg.author.id)

      del afk[str(msg.guild.id)]["to-mention-ids"][index]

      afk[str(msg.guild.id)].pop(str(msg.author.id))

      dumps = open("afk.json", "w")

      json.dump(afk, dumps, indent = 4)

      await msg.channel.send("{}, Welcome back to the server. I have removed your AFK status.".format(msg.author.mention), delete_after=5)

  @commands.command()
  @commands.bot_has_permissions(manage_nicknames = True)
  async def afk(self, ctx, *, message = "None"):

    file = open("afk.json", "r")

    afk = json.load(file)

    if not str(ctx.guild.id) in afk:

      afk[str(ctx.guild.id)] = {}

    if not str(ctx.author.id) in afk[str(ctx.guild.id)]:

      afk[str(ctx.guild.id)][str(ctx.author.id)] = {}

    if not "to-mention-ids" in afk[str(ctx.guild.id)]:

      afk[str(ctx.guild.id)]["to-mention-ids"] = []

    if not ctx.author.id in afk[str(ctx.guild.id)]["to-mention-ids"]:

      afk[str(ctx.guild.id)][str(ctx.author.id)] = message

      afk[str(ctx.guild.id)]["to-mention-ids"].append(ctx.author.id)

      dumps = open("afk.json", "w")

      json.dump(afk, dumps, indent = 4)

      await ctx.send(":white_check_mark: {} I have set your AFK to the reason of: `{}`".format(ctx.author.mention, message))
      
    
    else:

      return
  
  
  @commands.command()
  async def haash(self, ctx):
    await ctx.send("bangladesh high commission boi")
      
def setup(bot):

  bot.add_cog(AFK(bot))