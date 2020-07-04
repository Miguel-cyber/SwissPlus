import discord
from discord.ext import commands

import json

class Snipe(commands.Cog):
  
  def __init__(self, bot):
    
    self.bot = bot
    
  @commands.command()
  @commands.has_permissions(manage_messages = True)
  async def snipe(self, ctx):
    
    file = open("snipe.json", "r")
    
    snipe = json.load(file)
    
    if not str(ctx.guild.id) in snipe:
      
      return await ctx.send("There's nothing to snipe *yet*")
      
    user = snipe[str(ctx.guild.id)]["user-id"]
    
    msg = snipe[str(ctx.guild.id)]["deleted-message"]
    
    fetched_user = await self.bot.fetch_user(int(user))
    
    embed = discord.Embed()
    
    embed.set_author(name = fetched_user, icon_url = fetched_user.avatar_url)
    
    embed.color = discord.Color.blue()
    
    embed.description = msg
    
    embed.timestamp = ctx.message.created_at
    
    await ctx.send(embed = embed)
    
  @commands.Cog.listener()
  async def on_message_delete(self, msg):

    if msg.author.bot:

      return
    
    file = open("snipe.json", "r")
    
    snipe = json.load(file)
    
    if not str(msg.guild.id) in snipe:
      
      snipe[str(msg.guild.id)] = {}
   
    if not "user-id" in snipe[str(msg.guild.id)]:
      
      snipe[str(msg.guild.id)]["user-id"] = {}
      
    if not "deleted-message" in snipe[str(msg.guild.id)]:
      
      snipe[str(msg.guild.id)]["deleted-message"] = {}
      
    snipe[str(msg.guild.id)]["user-id"] = msg.author.id
    
    snipe[str(msg.guild.id)]["deleted-message"] = msg.content
    
    dumps = open("snipe.json", "w")
    
    json.dump(snipe, dumps, indent = 4)
    
def setup(bot):
  
  bot.add_cog(Snipe(bot))