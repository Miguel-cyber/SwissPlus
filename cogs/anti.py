import discord
from discord.ext import commands
import os
import praw
import json
import psutil
import time
import random
import asyncio
import requests
from googletrans import Translator
import datetime

bot = commands.Bot(command_prefix="+")

class AntiSwear(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot


  @commands.command(name="anti-word")
  @commands.has_permissions(manage_messages=True)
  @commands.bot_has_permissions(manage_messages = True)
  async def antiword(self, ctx, type = None, *, arg = None):
      
      if type == "enable":
        
        with open("antiswear.json", "r") as f:
          
          antiswear = json.load(f)
        
        if not str(ctx.guild.id) in antiswear:
          
          antiswear[str(ctx.guild.id)] = {}
          
          antiswear[str(ctx.guild.id)]["antiswear"] = []
          
          with open("antiswear.json", "w") as f:
            
            json.dump(antiswear, f, indent=4)
            
          await ctx.send("Anti-word is now enabled.")
          
        else:
          
          return await ctx.send("Anti-word is already enabled.")
          
      elif type == "add":
        
        with open("antiswear.json", "r") as f:
          
          antiswear = json.load(f)
        
        if not str(ctx.guild.id) in antiswear:
          
          return await ctx.send("Anti-word wasn't enabled.")
        
        if not "antiswear" in antiswear[str(ctx.guild.id)]:
          
          antiswear[str(ctx.guild.id)]["antiswear"] = []
        
        if arg in antiswear[str(ctx.guild.id)]["antiswear"]:
          
          return await ctx.send(f"**{arg}** is already listed in anti-word words.")
        
        antiswear[str(ctx.guild.id)]["antiswear"].append(arg)
        
        with open("antiswear.json", "w") as f:
          
          json.dump(antiswear, f, indent=4)
          
        await ctx.send(f"**{arg}** has been added as anti-word word.")
        
      elif type == "disable":
        
        with open("antiswear.json", "r") as f:
          
          antiswear = json.load(f)
          
        if not str(ctx.guild.id) in antiswear:
          
          return await ctx.send("Anti-word wasn't enabled.")
          
        antiswear.pop(str(ctx.guild.id))
        
        with open("antiswear.json", "w") as f:
          
          json.dump(antiswear, f, indent=4)
          
        await ctx.send("Anti-word has been disabled.")
      
      elif type == "remove":
        
        with open("antiswear.json", "r") as f:
          
          antiswear = json.load(f)
          
        if not str(ctx.guild.id) in antiswear:
          
          return await ctx.send("Anti-word wasn't enabled.")
          
        antiswear_word = antiswear[str(ctx.guild.id)]["antiswear"]
        
        if arg in antiswear_word:
          
          index = antiswear_word.index(arg)
          
          del antiswear_word[index]
          
          antiswear[str(ctx.guild.id)]["antiswear"] = antiswear_word
          
          with open("antiswear.json", "w") as f:
          
            json.dump(antiswear, f, indent=4)
            
          await ctx.send(f"Removed **{arg}** from anti-word words.")
          
        else:
          
          await ctx.send(f"**{arg}** wasn't listed in anti-word words.")
      
      elif type == "words":
        
        with open("antiswear.json", "r") as f:
          
          antiswear = json.load(f)
        
        if not str(ctx.guild.id) in antiswear:
          
          return await ctx.send("Anti-word wasn't enabled.")
        
        """
        msg = f"```Anti-swear words:\n"
          
        words = f"\n".join(antiswear[str(ctx.guild.id)]["antiswear"])
        
        msg += f"{words}"
        
        msg += "```"
          
        await ctx.send(msg)
        """
        
        embed = discord.Embed()
        
        embed.color = discord.Color.blue()
        
        embed.title = "Anti-Swear Words"
        
        embed.timestamp = ctx.message.created_at
        
        embed.description = "\n".join(antiswear[str(ctx.guild.id)]["antiswear"])
        
        await ctx.send(embed=embed)
        
      else:
        
        embed = discord.Embed(description="`+anti-word enable/disable`\n`+anti-word add/remove <word>`\n`+anti-word words`", color = discord.Color.blue())
        
        embed.set_author(name="Command: +anti-word")
        
        await ctx.send(embed=embed)
          
def setup(bot):
  
  bot.add_cog(AntiSwear(bot))