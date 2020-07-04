import discord
from discord.ext import commands
import json
import datetime
import psutil
import os
import platform

import asyncio

bot = commands.Bot(command_prefix = "+")

class Profile(commands.Cog):

  def __init__(self, bot):

    self.bot = bot
    

  @commands.command()
  async def profile(self, ctx, user: discord.Member = None):

    with open("profile.json", "r") as f:

      prof = json.load(f)
    

    if user == None:

      if not str(ctx.author.id) in prof:

        return await ctx.send("You don't have a profile, use `+setprofile` to make one.")

      author_name = prof[str(ctx.author.id)]["character-name"]

      author_age = prof[str(ctx.author.id)]["character-age"]

      author_hobby = prof[str(ctx.author.id)]["character-hobby"]

      author_image = prof[str(ctx.author.id)]["character-image"]

      author_place = prof[str(ctx.author.id)]["character-place"]

      


      embed = discord.Embed()

      embed.color = ctx.author.color

      embed.timestamp = ctx.message.created_at

      embed.set_author(name = "{}'s profile".format(ctx.author.name), icon_url = ctx.author.avatar_url)

      if not author_image.startswith("http"):

        pass

      else:

        embed.set_thumbnail(url = author_image)

      embed.add_field(name = "Name", value = author_name, inline = False)

      embed.add_field(name = "Age", value = author_age, inline = False)

      embed.add_field(name = "Hobby", value = author_hobby, inline = False)

      embed.add_field(name = "Fighting Tool", value = author_place, inline = False)
      

      await ctx.send(embed = embed)

    else:

      if not str(user.id) in prof:

        return await ctx.send(f"{user.mention} doesn't have a character profile.")

      author_name = prof[str(user.id)]["character-name"]

      author_age = prof[str(user.id)]["character-age"]

      author_hobby = prof[str(user.id)]["character-hobby"]

      author_image = prof[str(user.id)]["character-image"]

      author_place = prof[str(user.id)]["character-place"]

      
      embed = discord.Embed()

      embed.color = user.color

      embed.timestamp = ctx.message.created_at

      embed.set_author(name = "{}'s profile".format(user.name), icon_url = user.avatar_url)

      if not author_image.startswith("http"):

        pass

      else:

        embed.set_thumbnail(url = author_image)

      embed.add_field(name = "Name", value = author_name, inline = False)

      embed.add_field(name = "Age", value = author_age, inline = False)

      embed.add_field(name = "Hobby", value = author_hobby, inline = False)

      embed.add_field(name = "Fighting Tool", value = author_place, inline = False)
      

      await ctx.send(embed = embed)

  @commands.command()
  async def setprofile(self, ctx):

    with open("profile.json", "r") as f:

      prof = json.load(f)

    def check(m):

      return m.author == ctx.author and m.channel == ctx.channel

    if not str(ctx.author.id) in prof:

      prof[str(ctx.author.id)] = {}

      await ctx.send(":thinking: It seems that you don't have any character profile yet! Let's get creative!\nEnter a name for your character.\n\nTimeout: 20 seconds.")

      try:

        name = await self.bot.wait_for("message", check = check, timeout = 20)

      except asyncio.TimeoutError:

        await ctx.send("It seems that you haven't entered anything, run the command again to restart.")

        prof.pop(str(ctx.author.id))

      else:

        prof[str(ctx.author.id)]["character-name"] = name.content

        await ctx.send("{} `{}` seems like a good name! Now, enter the age for the character.\n\nTimeout: 20 seconds.".format(ctx.author.mention, name.content))

        try:

          age = await self.bot.wait_for("message", check = check, timeout = 20)

        except asyncio.TimeoutError:

          await ctx.send("It seems that you haven't entered anything, run the command again to restart.")

          prof.pop(str(ctx.author.id))

        else:

          prof[str(ctx.author.id)]["character-age"] = age.content

          await ctx.send(f"{ctx.author.mention} Now, let's pick a hobby for it.\n\nTimeout: 20 seconds.")

          try:

            hobby = await self.bot.wait_for("message", check = check, timeout = 20)

          except asyncio.TimeoutError:

            await ctx.send("It seems that you haven't entered anything, run the command again to restart.")

            prof.pop(str(ctx.author.id))

          else:

            prof[str(ctx.author.id)]["character-hobby"] = hobby.content

            await ctx.send("{} `{}` as a hobby doesn't seem that bad. Now, let's pick an image for it! Enter a URL that starts with either `http://` or `https://`.\n\nTimeout: 40 seconds.".format(ctx.author.mention, hobby.content))
            
            try:

              image = await self.bot.wait_for("message", check = check, timeout = 40)

            except asyncio.TimeoutError:

              await ctx.send("It seems that you haven't entered anything, run the command again to restart.")

              prof.pop(str(ctx.author.id))

            else:

              prof[str(ctx.author.id)]["character-image"] = image.content

              await ctx.send(f"{ctx.author.mention} Finally, enter your characters favourite tool to use in a fight. \n\nTimeout: 20 seconds.")

              try:

                place = await self.bot.wait_for("message", check = check, timeout = 20)

              except asyncio.TimeoutError:

                await ctx.send("It seems that you haven't entered anything, run the command again to restart.")

                prof.pop(str(ctx.author.id))

              else:

                prof[str(ctx.author.id)]["character-place"] = place.content

                await ctx.send("You're done! Use `+profile` to view your profile.")

                with open("profile.json", "w") as f:

                  json.dump(prof, f, indent = 4)

    else:

      await ctx.send("You already have a profile! Use `+profile` to view your profile or type `delete` to delete it.")
      
      try:

        def checks(s):

          return s.author == ctx.author and s.channel == ctx.channel and s.content == "delete"

        await self.bot.wait_for("message", check = checks, timeout = 10)

      except asyncio.TimeoutError:

        await ctx.send("Timed out.")

      else:

        prof.pop(str(ctx.author.id))

        await ctx.send("Your profile has been deleted.")

        with open("profile.json", "w") as f:

          json.dump(prof, f, indent = 4)
          

  bot.launch_time = datetime.datetime.utcnow()
          
  @commands.command()
  @commands.is_owner()
  async def systeminfo(self, ctx):
    delta_uptime = datetime.datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"`{days}d, {hours}h, {minutes}m, {seconds}s`")#
    
  @systeminfo.error
  async def error_handler(self, ctx, error):
    await ctx.send(error)
    
  @commands.command()
  async def stats(self, ctx):
    ping = int(round(self.bot.latency * 1000))
    tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    delta_uptime = datetime.datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Colour.blue())
    embed.add_field(name="System", value=f"**Memory Usage: {used_m}/{tot_m}MB**\n**Python Version: {platform.python_version()}**\n**Discord.py Version: {discord.__version__}**\n**Operating System: {platform.system()}**\n**CPU Usage: {psutil.cpu_percent()}%**\n**CPU Count: {psutil.cpu_count()}**", inline = False)
    embed.add_field(name="Bot", value=f"**Guilds: {len(self.bot.guilds)}**\n**Users: {len(self.bot.users)}**\n\n**Latency: {ping}ms**", inline = False)
    await ctx.send(embed=embed)
    
  @stats.error
  async def error_handler(self, ctx, error):
    await ctx.send(error)
    
def setup(bot):

  bot.add_cog(Profile(bot))