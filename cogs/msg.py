import discord
from discord.ext import commands

import json
import heapq

class MessageCounter(commands.Cog):

  def __init__(self, bot):

    self.bot = bot
    
  @commands.command(name = "msg-leaderboard")
  async def msgleaderboard(self, ctx):

    file = open("msg.json", "r")

    msgs = json.load(file)

    if not str(ctx.guild.id) in msgs:

      return await ctx.send("Try sending some messages.")

    guild = msgs[str(ctx.guild.id)]

    top_ten = heapq.nlargest(10, guild)

    highscore = sorted(top_ten, key = lambda x: guild[x].get("message-counter", 0), reverse = True)

    msg = "```"

    msg += "Message Counter Leaderboard\n"

    for number, user in enumerate(highscore):

      member = await self.bot.fetch_user(user)

      messages = "{:,}".format(guild[user].get("message-counter", 0))

      msg += "\n{} - {} sent {} messages.".format(number + 1, member.name, messages)

    msg += "```"

    await ctx.send(msg)

  @commands.Cog.listener()
  async def on_message(self, msg):

    if msg.author.bot:

      return

    file = open("msg.json", "r")

    msgs = json.load(file)

    if not str(msg.guild.id) in msgs:

      msgs[str(msg.guild.id)] = {}

    if not str(msg.author.id) in msgs[str(msg.guild.id)]:

      msgs[str(msg.guild.id)][str(msg.author.id)] = {}

      msgs[str(msg.guild.id)][str(msg.author.id)]["message-counter"] = 0

    msgs[str(msg.guild.id)][str(msg.author.id)]["message-counter"] += 1

    dumps = open("msg.json", "w")

    json.dump(msgs, dumps, indent = 4)

def setup(bot):

  bot.add_cog(MessageCounter(bot))