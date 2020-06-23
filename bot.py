import discord, io
from discord.ext import commands
from discord.ext.commands import BotMissingPermissions, bot_has_permissions
from discord.ext.commands import clean_content
import time
import time as timeModule
import asyncio
import sys
import ast
import os
import json
import random
import os
import datetime
import praw
import danksearch
from googletrans import Translator
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFile
from PIL import ImageFilter
import pytemperature
import pypokedex
from random import choice, randint
from asyncio import sleep
sys.path.insert(1, '../')



#with open("prefixes.json", "r") as f:
  #load = json.load(f)
  
default_prefix = "+"

#banlist = []

#def get_prefix(bot, message):
  #with open("prefixes.json", "r") as f:
    #prefixes = json.load(f)
    
    #prefix = prefixes[str(message.guild.id)], load.get(message.guild.id, default_prefix)
    #if message.author.id in banlist and message.content.startswith(prefix):
      #return message.channel.send("You have been banned from using `SwissPlus`. Please contact the bot owner for more information.")
    #else:
      #return prefixes[str(message.guild.id)], load.get(message.guild.id, default_prefix)
  
client = discord.Client
client = commands.Bot(command_prefix=default_prefix)


@client.event #on_ready event
async def on_ready():
 await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name="v1.2.0 | swissfun.mysticguard.xyz"))
 channel = client.get_channel(723120227533062205)
 embed = discord.Embed(colour=discord.Colour.green())
 embed.set_image(url="https://cdn.discordapp.com/attachments/716042337330921642/723121061784453130/542171280183656458.png")
 await channel.send(embed=embed)
 print("{} has successfully booted and running!".format(client.user.name))

reddit = praw.Reddit(client_id='GKg9xGGzV4vM9Q', client_secret='FutzuRgQ-0-fFTlOsbbDeJPdcUg', user_agent='Eternal City Bot by u/RedPhantomIRP')
client.remove_command("help")

@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)
      
    prefixes[str(guild.id)] = "+"
    
    with open("prefixes.json", "w") as f:
      json.dump(prefixes, f)




@client.command()
async def help(ctx):
    embed = discord.Embed(title="SwissPlus Help", colour=discord.Colour.blue())
    embed.add_field(name="<a:betterinfo:723691069035905146> Information", value="`botinfo`,`build`,`ping`,`userinfo`", inline=False)
    embed.add_field(name="<a:gears:723662459499708437> Moderation", value="`warn`,`warns`,`clearwarns`,`kick`,`ban`,`purge`,`config`,`recentlog`", inline=False)
    embed.add_field(name="<a:securitybig:723683774776344637> Security", value="`pincode`", inline=False)
    embed.add_field(name="<a:fun:723681896722333726> Fun", value="`fact`,`8ball`,`topic`,`suggest`,`translate`,`slap`,`swiss`,`say`,`age`,`weather`,`hack`,`ship`,`timer`,`youtube`", inline=False)
    embed.add_field(name=":moneybag: Currency", value="`register`,`work`,`balance`", inline=False)
    embed.add_field(name=":page_facing_up: Text", value="`drunkify`,`encrypt`,`decrypt`", inline=False)
    embed.add_field(name="<a:RedditSpin:723666835710541898> Reddit", value="`flightsim`,`fsx`,`meme`,`news`,`swissbot`", inline=False)
    await ctx.send(embed=embed)
    
@client.command(aliases = ["yt"])
async def youtube(ctx, *, search = None):
  
  if search == None:
    
    return
  
  if ctx.channel.is_nsfw() == False:
    
    danksearch.SAFESEARCH = True
  
    video = danksearch.Video(advanced = True)

    bad_word = ["p0rn", "pron", "p0rno", "p0rn0", "4ss", "4ass"]

    if search in bad_word:
  
      await video.search("never gonna give you up")

    else:

      await video.search(search)
  
    embed = discord.Embed(description = "[{}]({})".format(video.title, video.url))
    
    embed.add_field(name = "Views", value = video.views, inline = False)
    
    embed.add_field(name = "Likes", value = video.likes, inline = False)
    
    embed.add_field(name = "Dislikes", value = video.dislikes, inline = False)
    
    embed.add_field(name = "Creator", value = video.creator, inline = False)
    
    embed.add_field(name = "Channel", value = "[Link]({})".format(video.channel))
  
    embed.set_image(url = video.thumbnail)
  
    embed.color = discord.Color.blue()
    
    embed.set_footer(text = "Safesearch: ON | Turn on NSFW to turn off safesearch.")
  
    await ctx.send(embed = embed)
    
  else:
    
    danksearch.SAFESEARCH = False
  
    video = danksearch.Video(advanced = True)
  
    await video.search(search)
  
    embed = discord.Embed(description = "[{}]({})".format(video.title, video.url))
    
    embed.add_field(name = "Views", value = video.views, inline = False)
    
    embed.add_field(name = "Likes", value = video.likes, inline = False)
    
    embed.add_field(name = "Dislikes", value = video.dislikes, inline = False)
    
    embed.add_field(name = "Creator", value = video.creator, inline = False)
    
    embed.add_field(name = "Channel", value = "[Link]({})".format(video.channel))
  
    embed.set_image(url = video.thumbnail)
  
    embed.color = discord.Color.blue()
    
    embed.set_footer(text = "Safesearch: OFF | Turn off NSFW to turn on safesearch.")
  
    await ctx.send(embed = embed)
    

@client.command(aliases=["w"])
async def weather(ctx, *, varos):
    if not ctx.message.author.bot:
        try:
            api_key = "7a94d7ac1501b84ccd5796dc95c3974d"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = varos
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            async with aiohttp.ClientSession() as session:
                async with session.get(complete_url) as r:
                    response = await r.json()
            x = response
            if x["cod"] != "404":
                import pytemperature
                y = x["main"]
                z = x["weather"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                weather_description = z[0]["description"]
                celsius = pytemperature.k2c(current_temperature)
                embed = discord.Embed(title="Weather informations", color=0x00ff00, timestamp=datetime.datetime.utcnow())
                embed.add_field(name="**Temperature**", value=f"{int(celsius)}°C")
                embed.add_field(name="**Pressure**", value=f"{current_pressure}hPa")
                embed.add_field(name="**Humidity**", value=f"{current_humidity}%")
                embed.set_author(name="SwissPlus", icon_url=ctx.message.author.avatar_url)
                await ctx.send(embed=embed)
            else:
                await ctx.send(":x: Cannot find this city!")
        except Exception as e:
            await ctx.send(":x: Couldn't retrieve data!")
            
@client.event
async def on_member_join(member):
    file = open("system.json", "r")
    load = json.load(file)

    if "welcomer" in load:

        return
    channel = client.get_channel(723540800171933717)
    embed = discord.Embed(title="***Welcome to {ctx.guild.name}***", description="Welcome {} to {}! you are the {} member!  Please read The <#593154693459476480>. Enjoy your stay!".format(member.mention, ctx.guild.name, str(member.guild.member_count)), colour=discord.Colour.green())
    embed.set_footer(text=member.name, icon_url=member.avatar_url)
    await channel.send(embed=embed)

'''
@client.command()
async def locate(ctx, *, place = None):

if place == None:

  embed = discord.Embed()

  embed.title = ":x: Invalid argument"

  embed.description = "**+locate <place>**"

  embed.color = discord.Color.red()

  return await ctx.send(embed = embed)

async with aiohttp.ClientSession() as session:

  async with session.get("https://api.ksoft.si/kumo/gis", params = {"q": place, "include_map": "true"}, headers = {"Authorization": f"Bearer {ksoft_token}"}) as resp:

    data = await resp.json()

embed = discord.Embed()

embed.title = data["data"]["address"]

embed.url = data["data"]["map"]

embed.set_image(url = data["data"]["map"])

embed.add_field(name = "Latitude", value = data["data"]["lat"])

embed.add_field(name = "Longitude", value = data["data"]["lon"])

await ctx.send(embed = embed)
'''
            
@client.command()
async def butter(ctx):
    await ctx.send("you think this is a command? maybe later :)")
    
@client.command()
async def emoji(ctx, emoji: str):
    emoji=discord.utils.get(ctx.guild.emojis, name=emoji)
    await ctx.send(F"\{emoji}")
    


@client.command()
async def about (ctx,user: discord.Member):
    img = Image.open("infoimgimg.png") #Replace infoimgimg.png with your background image.
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Modern_Sans_Light.otf", 100) #Make sure you insert a valid font from your folder.
    fontbig = ImageFont.truetype("Fitamint Script.ttf", 400) #Make sure you insert a valid font from your folder.
    #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
    draw.text((200, 0), "Information:", (255, 255, 255), font=fontbig)
    draw.text((50, 500), "Name:\n{}".format(user), (255, 255, 255), font=font)
    draw.text((50, 700), "ID:\n{}".format(user.id), (255, 255, 255), font=font)
    draw.text((50, 900), "User Status:\n{}".format(user.status), (255, 255, 255), font=font)
    draw.text((50, 1100), "Account created:\n{}".format(user.created_at), (255, 255, 255), font=font)
    draw.text((50, 1300), "Nickname:\n{}".format(user.display_name), (255, 255, 255), font=font)
    draw.text((50, 1500), "Users' Top Role:\n{}".format(user.top_role), (255, 255, 255), font=font)
    draw.text((50, 1700), "User Joined:\n{}".format(user.joined_at), (255, 255, 255), font=font)
    img.save('about.png') #Change infoimg2.png if needed.
    await ctx.send(file=discord.File("about.png"))
    
@client.command()
async def getsomehelp (ctx,user: discord.Member):
    if user is None:
        await ctx.send("Mention someone smh")
    else:
        img = Image.open("getsomehelp.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Modern_Sans_Light.otf", 30)
        fontbig = ImageFont.truetype("Fitamint Script.ttf", 400)
        
        draw.text((50, 1), "  {} wanted {} to get help".format(ctx.author.name, user.name), (255, 255, 255), font=font)
        img.save('getsomehelp1.png')
        await ctx.send(file=discord.File("getsomehelp1.png"))
        
@client.command()
async def hack(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send("Mention a user to hack!")
    else:
        m1=await ctx.send(f"Hacking **{user}**.")
        await asyncio.sleep(2)
        await m1.edit(content=f'Hacking **{user}**..')
        await asyncio.sleep(2)
        await m1.edit(content=f'Hacking **{user}**...')
        await asyncio.sleep(1)
        await m1.edit(content='S')
        await asyncio.sleep(0.3)
        await m1.edit(content='St')
        await asyncio.sleep(0.3)
        await m1.edit(content='Ste')
        await asyncio.sleep(0.3)
        await m1.edit(content='Stea')
        await asyncio.sleep(0.3)
        await m1.edit(content='Steal')
        await asyncio.sleep(0.3)
        await m1.edit(content='Steali')
        await asyncio.sleep(0.3)
        await m1.edit(content='Stealin')
        await asyncio.sleep(0.3)
        await m1.edit(content='Stealing ')
        await asyncio.sleep(0.3)
        await m1.edit(content='Stealing i')
        await asyncio.sleep(0.3)
        await m1.edit(content='Stealing in')
        await asyncio.sleep(0.3)
        await m1.edit(content='Stealing inf')
        await asyncio.sleep(0.5)
        await m1.edit(content='Stealing info')
        await asyncio.sleep(0.3)
        await m1.edit(content='Stealing info.')
        await asyncio.sleep(1)
        await m1.edit(content='Stealing info..')
        await asyncio.sleep(1)
        await m1.edit(content='Stealing info...')
        await asyncio.sleep(1)
        await m1.edit(content='Stealing password.')
        await asyncio.sleep(1)
        await m1.edit(content='Stealing password..')
        await asyncio.sleep(1)
        await m1.edit(content='Stealing password...')
        await asyncio.sleep(1)
        await m1.edit(content='Stealing more shit...')
        await asyncio.sleep(2)
        await m1.edit(content='Grabbing ip... *(jk im not)*')
        await asyncio.sleep(1)
        await m1.edit(content='Loading hacking tool')
        await asyncio.sleep(1)
        await m1.edit(content='Loading hacking tool.')
        await asyncio.sleep(1)
        await m1.edit(content='Loading hacking tool..')
        await asyncio.sleep(1)
        await m1.edit(content='Loading hacking tool...')
        await asyncio.sleep(1)
        await m1.edit(content='Done.')
        await asyncio.sleep(1)
        await m1.edit(content='Hacking system.')
        await asyncio.sleep(1)
        await m1.edit(content='Hacking system..')
        await asyncio.sleep(1)
        await m1.edit(content='Hacking system...')
        await asyncio.sleep(1)
        await m1.edit(content=f'Successfully hacked {user.mention}.')

@client.command()
async def ship(ctx, name1 : clean_content, name2 : clean_content):
    shipnumber = random.randint(0,100)
    if 0 <= shipnumber <= 10:
        status = "Really low! {}".format(random.choice(["Friendzone ;(", 
                                                        'Just "friends"', 
                                                        '"Friends"', 
                                                        "Little to no love ;(", 
                                                        "There's barely any love ;("]))
    elif 10 < shipnumber <= 20:
        status = "Low! {}".format(random.choice(["Still in the friendzone", 
                                                 "Still in that friendzone ;(", 
                                                 "There's not a lot of love there... ;("]))
    elif 20 < shipnumber <= 30:
        status = "Poor! {}".format(random.choice(["But there's a small sense of romance from one person!", 
                                                 "But there's a small bit of love somewhere", 
                                                 "I sense a small bit of love!", 
                                                 "But someone has a bit of love for someone..."]))
    elif 30 < shipnumber <= 40:
        status = "Fair! {}".format(random.choice(["There's a bit of love there!", 
                                                  "There is a bit of love there...", 
                                                  "A small bit of love is in the air..."]))
    elif 40 < shipnumber <= 60:
        status = "Moderate! {}".format(random.choice(["But it's very one-sided OwO", 
                                                      "It appears one sided!", 
                                                      "There's some potential!", 
                                                      "I sense a bit of potential!", 
                                                      "There's a bit of romance going on here!", 
                                                      "I feel like there's some romance progressing!", 
                                                      "The love is getting there..."]))
    elif 60 < shipnumber <= 70:
        status = "Good! {}".format(random.choice(["I feel the romance progressing!", 
                                                  "There's some love in the air!", 
                                                  "I'm starting to feel some love!"]))
    elif 70 < shipnumber <= 80:
        status = "Great! {}".format(random.choice(["There is definitely love somewhere!", 
                                                   "I can see the love is there! Somewhere...", 
                                                   "I definitely can see that love is in the air"]))
    elif 80 < shipnumber <= 90:
        status = "Over average! {}".format(random.choice(["Love is in the air!", 
                                                          "I can definitely feel the love", 
                                                          "I feel the love! There's a sign of a match!", 
                                                          "There's a sign of a match!", 
                                                          "I sense a match!", 
                                                          "A few things can be imporved to make this a match made in heaven!"]))
    elif 90 < shipnumber <= 100:
        status = "True love! {}".format(random.choice(["It's a match!", 
                                                       "There's a match made in heaven!", 
                                                       "It's definitely a match!", 
                                                       "Love is truely in the air!", 
                                                       "Love is most definitely in the air!"]))

    if shipnumber <= 33:
        shipColor = 0xE80303
    elif 33 < shipnumber < 66:
        shipColor = 0xff6600
    else:
        shipColor = 0x3be801

    emb = (discord.Embed(color=shipColor, \
                         title="Love test for:", \
                         description="**{0}** and **{1}** {2}".format(name1, name2, random.choice([
                                                                                                    ":sparkling_heart:", 
                                                                                                    ":heart_decoration:", 
                                                                                                    ":heart_exclamation:", 
                                                                                                    ":heartbeat:", 
                                                                                                    ":heartpulse:", 
                                                                                                    ":hearts:", 
                                                                                                    ":blue_heart:", 
                                                                                                    ":green_heart:", 
                                                                                                    ":purple_heart:", 
                                                                                                    ":revolving_hearts:", 
                                                                                                    ":yellow_heart:", 
                                                                                                    ":two_hearts:"]))))
    emb.add_field(name="Results:", value=f"{shipnumber}%", inline=True)
    emb.add_field(name="Status:", value=(status), inline=False)
    emb.set_author(name="Shipping", icon_url="http://moziru.com/images/kopel-clipart-heart-6.png")
    await ctx.send(embed=emb)
    
@client.command()
async def drunkify(ctx, *, s):
    lst = [str.upper, str.lower]
    newText = await commands.clean_content().convert(ctx, ''.join(random.choice(lst)(c) for c in s))
    if len(newText) <= 380:
        await ctx.send(newText)
    else:
        try:
            await ctx.author.send(newText)
            await ctx.send(f"**{ctx.author.mention} The output too was too large, so I sent it to your DMs! :mailbox_with_mail:**")
        except Exception:
            await ctx.send(f"**{ctx.author.mention} There was a problem, and I could not send the output. It may be too large or malformed**")
    
@client.command()
async def encrypt(ctx, *, s):
    a = ''
    try:
        for letter in s:
            a+=chr(ord(letter)+len(s))
        cleanS = await commands.clean_content().convert(ctx, a)
    except Exception as e:
        await ctx.send(f"**Error: `{e}`. This probably means the input is malformed. Sorry, I'm not perfect and my bot developer is dumb**")
    if len(cleanS) <= 479:
        await ctx.send(f"```{cleanS}```")
    else:
        try:
            await ctx.author.send(f"```{cleanS}```")
            await ctx.send(f"**{ctx.author.mention} The output too was too large, so I sent it to your DMs! :mailbox_with_mail:**")
        except Exception:
            await ctx.send(f"**{ctx.author.mention} There was a problem, and I could not send the output. It may be too large or malformed**")

@client.command()
async def decrypt(ctx, *, s):
    a = ''
    try:
        for letter in s:
            a+=chr(ord(letter)-len(s))
        cleanS = await commands.clean_content().convert(ctx, a)
    except Exception as e:
        await ctx.send(f"**Error: `{e}`. This probably means the input is malformed. Sorry, I'm not perfect and my bot developer is dumb**")
    if len(cleanS) <= 479:
        await ctx.send(f"```{cleanS}```")
    else:
        try:
            await ctx.author.send(f"```{cleanS}```")
            await ctx.send(f"**{ctx.author.mention} The output too was too large, so I sent it to your DMs! :mailbox_with_mail:**")
        except Exception:
            await ctx.send(f"**{ctx.author.mention} There was a problem, and I could not send the output. It may be too large or malformed**")

@client.command()
async def timer(ctx, timer):
    """Counts down till it's over! Usage: *timer [time in secs]"""
    try:
        float(timer)
    except ValueError:
        await ctx.send("Silly billy... Usage: +timer [time in secs]. Make sure the time is a **whole number**.")
    else:
        await ctx.send(f"{ctx.author.mention} Your timer has started for {timer}s.")
        await asyncio.sleep(float(timer))
        await ctx.send(f"{ctx.author.mention} Your timer has finished. The timer was set for `{timer}`s.")
        await author.send(f"Your timer of `{timer}`s has finished.")
        
@commands.cooldown(1, 10, commands.cooldowns.BucketType.guild)
@commands.max_concurrency(1, per=commands.cooldowns.BucketType.guild)
@client.command(name='user_graph', aliases=['ug'])
async def user_graph(ctx, history: int = 24):
    """
    Display the bots user count over the past 24 hours.
    `history`: The amount of hours to display in the graph.
    """

    if history <= 0:
        raise exceptions.ArgumentError('History must be more than `0`.')

    async with ctx.channel.typing():

        query = 'WITH t AS (SELECT * from client_growth ORDER BY date DESC LIMIT $1) SELECT * FROM t ORDER BY date'
        user_growth = await client.db.fetch(query, history)

        if not user_growth:
            return await ctx.send('No user growth data.')

        title = f'User growth over the last {len(user_growth)} hour(s)'
        y_axis = [record['member_count'] for record in user_growth]
        x_axis = [record['date'] for record in user_growth]

        plot = await client.loop.run_in_executor(None, functools.partial(client.imaging.do_growth_plot, title,
                                                                           'Datetime (YYYY-MM-DD: HH:MM)', 'Users',
                                                                           y_axis, x_axis))
        return await ctx.send(file=discord.File(fp=plot, filename='UserGraph.png'))

    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        img = Image.open("error1.png") #Replace infoimgimg.png with your background image.
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Modern_Sans_Light.otf", 100) #Make sure you insert a valid font from your folder.
        fontbig = ImageFont.truetype("Fitamint Script.ttf", 400) #Make sure you insert a valid font from your folder.
        #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
        draw.text((50, 0), "         That is not a command.",(255, 255, 255), font=font)
        draw.text((40, 900), "Use +help to get the list of commands", (255, 255, 255), font=font)
        img.save('error.png') #Change infoimg2.png if needed.
        await ctx.send(file=discord.File("error.png"))
        logs = client.get_channel(716042337330921642)
        embed = discord.Embed(title="Command Not Found", description=f"{ctx.author} sent a command which could not be found.\n**Command**: `{message}",colour=discord.Colour.blue())
        await logs.send(embed=embed)
        

@client.command()
async def GuildCount(ctx):
  servers = list(client.guilds)
  await ctx.send("**SwissFun** is connected on " + str(len(client.guilds)) + " server(s):")
  await ctx.send('\n'.join(server.name for server in servers))

@client.command()
@commands.has_permissions(administrator=True)
async def say(ctx, channel : discord.TextChannel, *, arg = None):
  
  if arg == None:
    
    return await ctx.send("Say something to say 😑\nUsage: **`+say #channel <message>`**")
  await ctx.message.delete()
  
  await channel.send(arg)
  logs = client.get_channel(716042337330921642)
  embed = discord.Embed(title="Say Command Used", description=f"Message: `{arg}`\nSent in: <#{channel.id}>\nSent by: {ctx.author}",colour=discord.Colour.blue())
  await logs.send(embed=embed)
  await ctx.send(f"{ctx.author.mention}, Message sent to <#{channel.id}> with the message: `{arg}`.")
 
@client.command()
@commands.has_permissions(manage_messages=True)
@commands.bot_has_permissions(manage_messages = True)
async def purge(ctx,amount:int=None):
    if ctx.author.guild_permissions.manage_messages:
        if amount == None:
            embed = discord.Embed(title=":x: Invalid argument", description="+purge <amount>", color = discord.Colour.red())
            await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit = amount + 1)
            embed = discord.Embed(color=discord.Colour.green(), description=f":white_check_mark: Purged {amount} message(s).")
            await ctx.send(embed=embed, delete_after=3)
            
@purge.error
async def error_handler(ctx, error):
    if isinstance(error, BotMissingPermissions):
        embed=discord.Embed(description=f":x: I need the permission `{' '.join(error.missing_perms)}` to do that!", color = 0xff0000)
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description = ":x: You need the `Manage Messages` permission to do that.", color = 0xff0000)
        await ctx.send(embed=embed)
        raise CustomException() from error
    else:
        raise error
  



@client.command()
@commands.has_permissions(administrator=True)
async def config(ctx, pin = None, type = None):
    file = open("system.json", "r")
    load = json.load(file)
        
            
    if type is None:
        embed = discord.Embed()
        embed.set_footer(text = "You can enable/disable commands by using +config enable/disable category-name")
        
        if not "fun" in load:
            embed.add_field(name="Fun", value="Current: **Enabled**", inline=False)
        elif "fun" in load:
            embed.add_field(name="Fun", value="Current: **Disabled**", inline=False)
        if not "moderation" in load:
            embed.add_field(name="Moderation", value="Current: **Enabled**", inline=False)
        elif "moderation" in load:
            embed.add_field(name="Moderation", value="Current: **Disabled**", inline=False)
        if not "reddit" in load:
            embed.add_field(name="Reddit", value="Current: **Enabled**", inline=False)
        elif "reddit" in load:
            embed.add_field(name="Reddit", value="Current: **Disabled**", inline=False)
        if not "welcomer" in load:
            embed.add_field(name="Welcomer", value="Current: **Enabled**", inline=False)
        elif "welcomer" in load:
            embed.add_field(name="Welcomer", value="Current: **Disabled**", inline=False)
        return await ctx.send(embed=embed)
         #except: pass
                    
        
    if type == "enable-mod":
    
      if not "moderation" in load:
    
        return await ctx.send("The `Moderation` commands wasn't disabled. The commands are currently active.")
    
      load.pop("moderation")
    
      dumps = open("system.json", "w")
      json.dump(load, dumps, indent = 4)
    
      await ctx.send(f"<a:success:719504281044123680> Enabled `moderation` commands.")
          
    elif type == "disable-mod":
    
      if not "moderation" in load:
    
        load["moderation"] = {}
    
      dumps = open("system.json", "w")
    
      json.dump(load, dumps, indent = 4)
    
      await ctx.send(f"<a:success:719504281044123680> Disabled `moderation` commands.")
    
    elif type == "enable-fun":
    
      if not "fun" in load:
    
        return await ctx.send("The `fun` commands wasn't disabled. The commands are currently active.")
    
      load.pop("fun")
    
      dumps = open("system.json", "w")
      json.dump(load, dumps, indent = 4)
    
      await ctx.send(f"<a:success:719504281044123680> Enabled `fun` commands.")
          
    elif type == "enable-reddit":
    
      if not "reddit" in load:
    
        return await ctx.send("The `reddit` commands wasn't disabled. The commands are currently active.")
    
      load.pop("reddit")
    
      dumps = open("system.json", "w")
      json.dump(load, dumps, indent = 4)
    
      await ctx.send(f"<a:success:719504281044123680> Enabled `reddit` commands.")
    
    elif type == "disable-fun":
    
      if not "fun" in load:
    
        load["fun"] = {}
    
      dumps = open("system.json", "w")
    
      json.dump(load, dumps, indent = 4)
    
      await ctx.send(f"<a:success:719504281044123680> Disabled `fun` commands.")
          
    
    elif type == "disable-reddit":
    
      if not "reddit" in load:
    
        load["reddit"] = {}
    
      dumps = open("system.json", "w")
    
      json.dump(load, dumps, indent = 4)
    
      await ctx.send(f"<a:success:719504281044123680> Disabled `reddit` commands.")
      
    elif type == "enable-welcomer":
    
      if not "welcomer" in load:
    
        return await ctx.send("The `Welcomer` system isn't disabled. The system are currently active.")
    
      load.pop("welcomer")
    
      dumps = open("system.json", "w")
      json.dump(load, dumps, indent = 4)
    
      await ctx.send(f"<a:success:719504281044123680> Enabled `welcomer` system.")
          
    elif type == "disable-welcomer":
    
      if not "welcomer" in load:
    
        load["welcomer"] = {}
    
      dumps = open("system.json", "w")
    
      json.dump(load, dumps, indent = 4)
    
      await ctx.send(f"<a:success:719504281044123680> Disabled `welcomer` system.")
      
    
    
@config.error
async def config_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description = ":no_entry_sign: You need the `Administrator` permission to preform this command.", color = 0xff0000)
        await ctx.send(embed=embed)
        

    
@client.command()
@commands.dm_only()
async def pincode(ctx, pin: int = None):

  if pin == None:
    return await ctx.send(f"Return the command: `+pincode` and enter your authorisation code between `4` and `6` characters long.\nAfter that i will make an Authorisation Token with your id (`{ctx.author.id}`) to access certain commands.")

  file = json.load(open("two-factor-auth.json", "r"))

  author = ctx.author
  

  if not str(author.id) in file:
    file[str(author.id)] = pin

  json.dump(file, open("two-factor-auth.json", "w"), indent = 4)

  
  if str(author.id) in file:
    file[str(author.id)] = pin
    
  json.dump(file, open("two-factor-auth.json", "w"), indent = 4)
      
  return await author.send(f"**You have made changes to your Security**!\nSuccessfully changed your pincode to: `{pin}`\nPlease save this code as you may need it whilst running a command to protect you and the server.")
  
  
@pincode.error
async def pincode_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title="Slow it down!",description=f"C'mon, {error}", color = 0xff0000)
        await ctx.send(ctx.author.mention, embed=embed, delete_after=5)
        #await msg.edit(embed=embed)
    else:
        embed=discord.Embed(title="Error!",description=f"{error}", color = 0xff0000)
        return await ctx.send(embed=embed)
    
@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
        roles= [role for role in member.roles]
        embed = discord.Embed(colour=discord.Colour.blue(), timestamp=ctx.message.created_at)
        embed.set_author(name = member, icon_url = member.avatar_url)
        embed.set_footer(text = "ID: {}".format(member.id))
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Nickname", value=member.nick, inline=False)
        embed.add_field(name="Status", value=member.status, inline=False)
        embed.add_field(name="Registered", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"), inline=False)
        embed.add_field(name="Joined", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"), inline=False)
        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="Bot?", value=member.bot)
        await ctx.send(embed=embed)

    else:
        roles= [role for role in member.roles]
        embed = discord.Embed(colour=discord.Colour.blue(), timestamp=ctx.message.created_at)
        embed.set_author(name = member, icon_url = member.avatar_url)
        embed.set_footer(text = "ID: {}".format(member.id))
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Nickname", value=member.nick, inline=False)
        embed.add_field(name="Status", value=member.status, inline=False)
        embed.add_field(name="Registered", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"), inline=False)
        embed.add_field(name="Joined", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %P UTC"), inline=False)
        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="Bot?", value=member.bot)
        #embed.add_field(name="Status", value=member.Status)
        await ctx.send(embed=embed)

@client.command()
async def suggest(ctx, *, reportmsg):
    channel = client.get_channel(724426437557223425)
    embed = discord.Embed(title=f"{ctx.author}", description=f"{reportmsg}", color=0xFFFF)
    request=await channel.send(embed=embed)
    await request.add_reaction("✅"); await request.add_reaction("❌")
    embed = discord.Embed(title=f"{ctx.author} Your suggestion has been submitted.", color=0xFFFF)
    await ctx.message.delete()
    await ctx.send(embed=embed)

@client.command()
async def build(ctx):
    embed = discord.Embed(Title="SwissPlus Build", colour=discord.Colour.blue())
    embed.add_field(name="Build Version:", value="v1.2.0", inline=False)
    embed.add_field(name="Released:", value="17th June 2020", inline=False)
    embed.add_field(name="Github:", value="[Click Me](http://swissplus.mysticguard.xyz)", inline=False)
    embed.add_field(name="Known Issues", value="Issues with loading some images via Reddit\n\nIssues __should__ be fixed, please dm a SwissPlus developer if errors occure.", inline=False)
    embed.add_field(name="Upcoming Commands", value="`+meter`", inline=False)
    await ctx.send(embed=embed)
    

@client.command()
async def news(ctx):
    file = open("system.json", "r")
    load = json.load(file)

    if "reddit" in load:

        return await ctx.send(":no_entry_sign: The `reddit` commands are currently **disabled**.")
    await ctx.trigger_typing()
    memes_submissions = reddit.subreddit('AviationNews').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
	    submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title=f'{submission.title}', color=discord.Colour.blue(), url=submission.url)
    embed.set_image(url="https://cdn.discordapp.com/attachments/719472911223619735/722839498777559060/Aviation_News_Today.jpg")
    embed.add_field(name="Reddit r/AviationNews", value=f"By u/{str(submission.author)}")
    all_comments = submission.comments
    embed.set_footer(text=f"{submission.ups} | {len(all_comments)}")
    await ctx.send(embed=embed)
    
@news.error
async def news_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title="Slow it down!",description=f"C'mon, {error}", color = 0xff0000)
        await ctx.send(ctx.author.mention, embed=embed, delete_after=5)
        #await msg.edit(embed=embed)
    else:
        embed=discord.Embed(title="Error!",description=f"{error}", color = 0xff0000)
        await ctx.send("An error has occured, please rerun the command", embed=embed)
    
@client.command()
async def swissbot(ctx):
    file = open("system.json", "r")
    load = json.load(file)

    if "reddit" in load:

        return await ctx.send(":no_entry_sign: The `reddit` commands are currently **disabled**.")
    await ctx.trigger_typing()
    memes_submissions = reddit.subreddit('swissbot').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
	    submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title=f'{submission.title}', color=discord.Colour.blue(), url=submission.url)
    embed.set_image(url=submission.url)
    embed.add_field(name="Reddit r/swissbot", value=f"By u/{str(submission.author)}")
    all_comments = submission.comments
    embed.set_footer(text=f"{submission.ups} | {len(all_comments)}")
    await ctx.send(embed=embed)
    
@swissbot.error
async def swissbot_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title="Slow it down!",description=f"C'mon, {error}", color = 0xff0000)
        await ctx.send(ctx.author.mention, embed=embed, delete_after=5)
        #await msg.edit(embed=embed)
    else:
        embed=discord.Embed(title="Error!",description=f"{error}", color = 0xff0000)
        await ctx.send("An error has occured, please rerun the command", embed=embed)



@client.command()
async def flightsim(ctx):
    file = open("system.json", "r")
    load = json.load(file)

    if "reddit" in load:

        return await ctx.send(":no_entry_sign: The `reddit` commands are currently **disabled**.")
    await ctx.trigger_typing()
    memes_submissions = reddit.subreddit('flightsim').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
	    submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title=f'{submission.title}', color=discord.Colour.blue(), url=submission.url)
    embed.set_image(url=submission.url)
    embed.add_field(name="Reddit r/flightsim", value=f"By u/{str(submission.author)}")
    all_comments = submission.comments
    embed.set_footer(text=f"{submission.ups} | {len(all_comments)}")
    await ctx.send(embed=embed)
    
@flightsim.error
async def flightsim_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title="Slow it down!",description=f"C'mon, {error}", color = 0xff0000)
        await ctx.send(ctx.author.mention, embed=embed, delete_after=5)
        #await msg.edit(embed=embed)
    else:
        embed=discord.Embed(title="Error!",description=f"{error}", color = 0xff0000)
        await ctx.send("An error has occured, please rerun the command", embed=embed)



@client.command()
async def fsx(ctx):
    file = open("system.json", "r")
    load = json.load(file)

    if "reddit" in load:

        return await ctx.send(":no_entry_sign: The `reddit` commands are currently **disabled**.")
    await ctx.trigger_typing()
    memes_submissions = reddit.subreddit('fsx').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
	    submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title=f'{submission.title}', color=discord.Colour.blue(), url=submission.url)
    embed.set_image(url=submission.url)
    embed.add_field(name="Reddit r/fsx", value=f"By u/{str(submission.author)}")
    all_comments = submission.comments
    embed.set_footer(text=f"{submission.ups} | {len(all_comments)}")
    await ctx.send(embed=embed)
    
@fsx.error
async def fsx_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title="Slow it down!",description=f"C'mon, {error}", color = 0xff0000)
        await ctx.send(ctx.author.mention, embed=embed, delete_after=5)
        #await msg.edit(embed=embed)
    else:
        embed=discord.Embed(title="Error!",description=f"{error}", color = 0xff0000)
        await ctx.send("An error has occured, please rerun the command", embed=embed)


@client.command()
async def meme(ctx):
    file = open("system.json", "r")
    load = json.load(file)

    if "reddit" in load:

        return await ctx.send(":no_entry_sign: The `reddit` commands are currently **disabled**.")
    await ctx.trigger_typing()
    memes_submissions = reddit.subreddit('dankmemes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
	    submission = next(x for x in memes_submissions if not x.stickied)
    embed = discord.Embed(title=f'{submission.title}', color=discord.Colour.blue(), url=submission.url)
    embed.set_image(url=submission.url)
    embed.add_field(name="Reddit r/dankememes", value=f"By u/{str(submission.author)}")
    all_comments = submission.comments
    embed.set_footer(text=f"{submission.ups} | {len(all_comments)}")
    await ctx.send(embed=embed)
    



@client.command()
async def topic(ctx):
    file = open("system.json", "r")
    load = json.load(file)

    if "fun" in load:

        return await ctx.send(":no_entry_sign: The `fun` commands are currently **disabled**.")
    facts=["If you found $100 on the ground, what would you do with it?", "What would you do if you couldn't use the internet or watch TV for a month?", "Have you been active recently?", "If you made a airline, what would it be called?", "What is your favorite airplane?", "Are you a risk taker? What is the biggest risk that you've taken?", "Do you watch __*all*__ of Swiss001's Videos?", "How often do you use your phone?", "What is something that makes you smile?", "Describe your favorite type of pizza?", "As a child, what was your dream to become?", "As a child, what did you want to be when you grow up?", "Whos your faviourite actor?", "What are you doing at the weekend?", "How are you coping with Covid-19?"]
    embed=discord.Embed(color=0xFF9393, title="Topic", description=random.choice(facts))
    await ctx.send(embed=embed)

@client.command()
async def botinfo(ctx, member: discord.Member = None):
    embed = discord.Embed(colour=0xe74c3c)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/613436874261921912/648283763016597515/PicsArt_11-23-03.21.35.png')
    embed.add_field(name="User name:", value="SwissPlus", inline=False)
    embed.add_field(name="ID:", value="722770938609008672", inline=False)
    embed.add_field(name="Developers", value="<@596751548877373440> and <@414391316059783172>", inline=False)
    embed.add_field(name="Libary:", value="Discord.py", inline=False)
    embed.add_field(name="Status:", value="online", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await ctx.trigger_typing()
    t2 = time.perf_counter()
    embed = discord.Embed(title=None, description=':ping_pong: ping pong: {}ms'.format(
        round((t2-t1)*1000)), color=0x2874A6)
    await ctx.send(embed=embed)

@client.command()
async def fact(ctx):
    file = open("system.json", "r")
    load = json.load(file)

    if "fun" in load:

        return await ctx.send(":no_entry_sign: The `fun` commands are currently **disabled**.")
    facts=["Pilots eat a different meal. There are various rules which are imposed by different airlines. However, there is one rule which is common to the vast majority of them. It is the rule that pilots must be fed the same multi-course meal given to those in the first and business class whilst the co-pilots are encouraged to eat different entrees to guard against cases of food poisoning.", "More than 80% of the population is afraid of flying! Acrophobia is defined as a fear of heights. Unlike a specific phobia like aerophobia – fear of flying -and other specific phobias, acrophobia can cause a person to fear a variety of things related to being far from the ground. Depending on the severity of the phobia, an acrophobic person may equally fear being on a high floor of a building or simply climbing a ladder.", "A Boeing 747 is made up of six million parts! Boeing 747 is the most well known  wide-body commercial airliner and cargo transportation aircraft frequently referred to as the Queen of the Skies or the Jumbo Jet. This airplane is famed because it was the first huge body aircraft ever produced. A Boeing 747 is made up of six million parts which are made to be all controlled by a few pilots sitting up front with switches and buttons under their fingertips.", "Only 5% of the world’s population have ever been on an airplane. Though the aviation sector is growing rapidly, according to the statistics only 5% of the world’s population has ever flown on an airplane. Many people, especially from the underdeveloped regions, have never ever been in an aircraft and it is not likely that they will have an opportunity to fly in all of their lives. However, at the same time a small minority of the world’s population fly very regularly.", "In fact, according to a report from the Air Accident Investigation & Aviation Safety Board, those masks only provide 12 minutes of continuous airflow on a 737. Luckily, that's typically just the amount of time needed for your flight to find a safe landing spot.", "So, who's flying your plane, exactly? Maybe no one—at least for portions of the flight. According to a 2017 report by the British Airline Pilots Association (BALPA), among a group of 500 pilots polled, 43 percent admitted to accidentally falling asleep while manning the plane, while 31 percent admitted to waking up from a nap to find their co-pilot sleeping, as well.", "The black box, also known as the Flight Data Recorder, is actually painted bright orange. The heat-resistant paint used to coat the boxes' exteriors comes in a highlighter-orange hue, which also happens to make them easier to find in case of an accident.", "The Boeing 747 burns about 1 gallon of fuel every second, or 5 gallons per mile. Reversing this gives us the figure of 0.2 miles per gallon of fuel. This is much lower than the average car's fuel efficiency at about 25 miles per gallon. But, considering the number of passengers the 747 carries, it is far more efficient. This breakdown explains that, because the plane can carry about 500 people, it's actually getting 100 miles per gallon per person.", "In 1985, an ex-con who hijacked a Norwegian Boeing 737 armed with a pistol decided to abandon his plan so long as the police were willing to give him one thing: beer. In the end, the plane landed safely at Fornebu Airport in Oslo, none of the 115 passengers on board were harmed, and the hijacker was arrested.", "As it so happens, the filthiest place on a plane is that tray table you're eating your meal off of. According to a study conducted by TravelMath, tray tables hosted 2,155 colony-forming bacterial units (CFU) per square inch. In comparison, the button to flush the toilet had just 265 CFU in the same amount of space.", "The Antonov An-225 has an impressive maximum takeoff weight of 591.7 tons. In comparison, the Boeing 747-8F's maximum takeoff weight is 489,218 pounds less, at 347.091 tons.", "You are about 7 percent of the distance to space during flights.\nSometimes, it can feel like you are astronomically high in the air when you're on a plane. However, you might be surprised to discover that you're actually only 7 percent of the distance it would take for you to get into space. Planes can fly much higher than their average altitude of 30,000, but they don't because doing so would present health risks to those inside.", "Airplanes can trigger lightning.\nWhen a plane passes through clouds, the static created can actually spur the development of lightning. Fortunately, even if your plane is struck, you're likely pretty safe. There hasn't been a lightning-related plane crash in the United States since 1967, and increasing safety measures have made lightning strikes less dangerous to passengers than ever before. When lightning strikes a plane, the electrical current is evenly distributed throughout the aircraft's conductive aluminum interior, while grounding the plane's interior electrical systems prevents surges that could interfere with its functionality.", "Airplane bathrooms can be opened from the outside.\nWhile flipping that latch inside the bathroom that turns the door sign to occupied may give you some semblance of privacy, there's an easy way for flight personnel to get in if they need to. Underneath that lavatory sign, there's a switch that allows flight crew to open the door if they're concerned about your safety or the safety of other passengers.", "One airline has had no fatal accidents.\nDespite being in business for nearly a century, Australian airline Qantas has never had a fatal accident involving one of its commercial aircrafts."]
    embed=discord.Embed(color=0xFF9393, title="Fact", description=random.choice(facts))
    await ctx.send(embed=embed)

@client.command(name='8ball', description="Answers a yes/no question.", brief="Answers from the beyond.", aliases=['eight_ball', 'eightball', '8-ball'])
async def eightball(ctx):
    file = open("system.json", "r")
    load = json.load(file)

    if "fun" in load:

        return await ctx.send(":no_entry_sign: The `fun` commands are currently **disabled**.")
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        'Execute bean.exe',
        'ok nerd',
        'You must be borking mad!'
    ]
    await ctx.send(random.choice(possible_responses) + ", " + ctx.message.author.mention)




@client.command()
@commands.is_owner()
async def restart(ctx):
    await ctx.send("i hate when u restart me it hurts smh ok bye")
    await sys.exit()
    
@client.command()
async def terminate(ctx):
    print('hi')


#kick
@client.command()
@bot_has_permissions(kick_members=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None, *, reason=None):
    file = open("system.json", "r")
    load = json.load(file)

    if "moderation" in load:

        return await ctx.send(":no_entry_sign: The `moderation` commands are currently **disabled**.")
    if member is (ctx.author):
        return await ctx.send('You cannot kick yourself!')
    if not member:
        embed = discord.Embed(description = ":question: Mention someone to kick or mention their User ID.", color = 0xff0000)
        return await ctx.send(embed = embed)
    await member.kick(reason=reason)
    embed = discord.Embed(description = f"<a:success:719504281044123680> `{member}` has been kicked.", color = 0x00ff00)
    return await ctx.send(embed = embed)
	

@kick.error
async def error_handler(ctx, error):
    if isinstance(error, BotMissingPermissions):
        embed=discord.Embed(description=f":x: I need the permission `{' '.join(error.missing_perms)}` to do that!", color = 0xff0000)
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description = ":x: You need the `Kick Members` permission to do that.", color = 0xff0000)
        await ctx.send(embed=embed)
    if isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(description = f":x: That user is a mod/admin. I cannot do that.", color = 0xff0000)
        await ctx.send(embed=embed)
        raise CustomException() from error
    else:
        raise error
  
#ban
@client.command()
@bot_has_permissions(ban_members=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None, *, reason=None):
    file = open("system.json", "r")
    load = json.load(file)

    if "moderation" in load:

        return await ctx.send(":no_entry_sign: The `moderation` commands are currently **disabled**.")
    if member is (ctx.author):
        return await ctx.send('You cannot ban yourself!')
    if not member:
        embed = discord.Embed(description = ":question: Mention someone to ban or mention their User ID.", color = 0xff0000)
        return await ctx.send(embed = embed)
    await member.ban(reason=reason)
    embed = discord.Embed(description = f"{member} has been banned.", color = 0x00ff00)
    return await ctx.send(embed = embed)
	

@ban.error
async def error_handler(ctx, error):
    if isinstance(error, BotMissingPermissions):
        embed=discord.Embed(description=f":x: I need the permission `{' '.join(error.missing_perms)}` to do that!", color = 0xff0000)
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description = ":x: You need the `Ban Members` permission perform that command.", color = 0xff0000)
        await ctx.send(embed=embed)
    if isinstance(error, discord.Forbidden):
        embed = discord.Embed(description = ":x: That user is a mod/admin, I can't do that.", color = 0xff0000)
        await ctx.send(embed=embed)
        raise CustomException() from error
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description = ":x: I don't know who to ban!\nMention a member to ban them.", color = 0xff0000)
        await ctx.send(embed=embed)
        raise CustomException() from error
    else:
        raise error

@client.command()
async def gayrate(ctx, member: discord.Member = None):
    file = open("system.json", "r")
    load = json.load(file)

    if "fun" in load:

        return await ctx.send(":no_entry_sign: The `fun` commands are currently **disabled**.")
    if member is None:
        Percent = str(random.randint(0,100))
        await ctx.send(f"You are {Percent}% gay!")
    else:
        Percent = str(random.randint(0,100))
        await ctx.send(f"{member.mention} is {Percent}% gay!")

@client.command()
async def simprate(ctx, member: discord.Member = None):
    file = open("system.json", "r")
    load = json.load(file)

    if "fun" in load:

        return await ctx.send(":no_entry_sign: The `fun` commands are currently **disabled**.")
    if member is None:
        Percent = str(random.randint(0,100))
        await ctx.send(f"You are {Percent}% simp!")
    else:
        Percent = str(random.randint(0,100))
        await ctx.send(f"{member.mention} is {Percent}% simp!")
        
@client.command()
async def age(ctx, member: discord.Member = None):
    file = open("system.json", "r")
    load = json.load(file)

    if "fun" in load:

        return await ctx.send(":no_entry_sign: The `fun` commands are currently **disabled**.")
    if member is None:
        Percent = str(random.randint(13,100))
        await ctx.send(f"You are {Percent} years old!")
    else:
        Percent = str(random.randint(13,100))
        await ctx.send(f"{member.mention} is {Percent} years old!")
        
@client.command()
@commands.has_permissions(manage_messages = True)
async def clearwarns(ctx, user: discord.Member = None):
    file = open("system.json", "r")
    load = json.load(file)

    if "moderation" in load:

      return await ctx.send(f":no_entry_sign: The `moderation` commands is currently **disabled** by a LockBot Staff Member.")

    x = ":x:"

    if user == None:

      embed = discord.Embed()

      embed.description = "**+clearwarn <@user>**"

      embed.title = "{} Invalid argument".format(x)

      embed.color = discord.Color.red()

      return await ctx.send(embed = embed)

    file = open("warns.json", "r")

    warn = json.load(file)

    if not str(ctx.guild.id) in warn:

      return await ctx.send("There are no warnings in this guild.")

    if not str(user.id) in warn[str(ctx.guild.id)]:

      return await ctx.send(":x: This user doesn't have any warnings.")

    warnings = warn[str(ctx.guild.id)][str(user.id)]["warns"]

    warn[str(ctx.guild.id)].pop(str(user.id))

    dumps = open("warns.json", "w")

    json.dump(warn, dumps, indent = 4)

    embed = discord.Embed()

    embed.description = ":white_check_mark: Cleared {} warning(s) for {}.".format(len(warnings), user.mention)

    embed.color = discord.Color.green()

    await ctx.send(embed = embed)
    
@clearwarns.error
async def clearwarns_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description = ":no_entry_sign: You need the `Manage Messages` permission to preform this command.", color = 0xff0000)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description = ":warning: Error", color = discord.Colour.red())
        embed.add_field(name="An error has occured!", value=f"{error}")
        await ctx.send(embed=embed)

@client.command(aliases = ["warnings"])
@commands.has_permissions(manage_messages = True)
async def warns(ctx, user: discord.Member = None):
    file = open("system.json", "r")
    load = json.load(file)

    if "moderation" in load:

      return await ctx.send(f":no_entry_sign: The `moderation` commands is currently **disabled** by a LockBot Staff Member.")

    file = open("warns.json", "r")

    warn = json.load(file)

    if not str(ctx.guild.id) in warn:

      return await ctx.send("There are no warnings in this server.")

    if user == None:

        await ctx.send("> :question: Mention a member to view warnings for.")

    else:

      fetched_user = await client.fetch_user(user.id)

      if not str(fetched_user.id) in warn[str(ctx.guild.id)]:

        return await ctx.send("User doesn't have any warnings.")

      msg = "```"

      msg += "Warning(s) for: {}\n\n- ".format(fetched_user)

      msg += "\n- ".join([warns for warns in warn[str(ctx.guild.id)][str(fetched_user.id)]["warns"]])

      msg += "```"
      
      embed = discord.Embed(description = f"Warnings for {fetched_user}", color = 0x00ff00)
      embed.add_field(name=f"Warnings:", value=f"\n\n".join([warns for warns in warn[str(ctx.guild.id)][str(fetched_user.id)]["warns"]]))

      await ctx.send(embed=embed)

      #await ctx.send(msg)
      
@warns.error
async def warns_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description = ":no_entry_sign: You need the `Manage Messages` permission to preform this command.", color = 0xff0000)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description = ":warning: Error", color = discord.Colour.red())
        embed.add_field(name="An error has occured!", value=f"{error}")
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages = True)
async def warn(ctx, user: discord.Member = None, *, reason = None):
    file = open("system.json", "r")
    load = json.load(file)

    if "moderation" in load:

      return await ctx.send(f":no_entry_sign: The `moderation` commands is currently **disabled** by a LockBot Staff Member.")

    x = ":x:"

    embed = discord.Embed()

    embed.title = "{} Invalid argument".format(x)

    embed.description = "**+warn <@user> <reason>**"

    embed.color = discord.Color.red()

    if user == None:

      return await ctx.send(embed = embed)

    if reason == None:

      return await ctx.send(embed = embed)

    file = open("warns.json", "r")

    warn = json.load(file)

    if not str(ctx.guild.id) in warn:

      warn[str(ctx.guild.id)] = {}

    if not str(user.id) in warn[str(ctx.guild.id)]:

      warn[str(ctx.guild.id)][str(user.id)] = {}

      warn[str(ctx.guild.id)][str(user.id)]["warns"] = []

    warn[str(ctx.guild.id)][str(user.id)]["warns"].append(reason)

    dumps = open("warns.json", "w")

    json.dump(warn, dumps, indent = 4)

    done = discord.Embed()

    done.description = f":white_check_mark: Warned {user.mention} ({user.id})\n**Moderator**: {ctx.author.mention}\n**Reason**: {reason}"

    done.color = discord.Color.green()

    log = discord.Embed()

    log.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

    log.description = "Command `warn` in {}\nd-warn {} {}".format(ctx.channel.mention, user.mention, reason)

    log.color = discord.Color.blue()

    log.timestamp = ctx.message.created_at

    await ctx.send(embed = done)


    await ctx.message.delete()
    
@warn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description = ":no_entry_sign: You need the `Manage Messages` permission to preform this command.", color = 0xff0000)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description = ":warning: Error", color = discord.Colour.red())
        embed.add_field(name="An error has occured!", value=f"{error}")
        await ctx.send(embed=embed)
        
@commands.cooldown(1, 5, commands.BucketType.user)
@client.command()
async def translate(ctx, type = None, *, arg = None):
      if type == None:
        error = discord.Embed(title=":x: Invalid argument", description="**+translate <language> <sentence>**", color = discord.Colour.red())
        await ctx.send(embed=error)
        embed = discord.Embed(title="10 Most Spoken Languages", description="English | en\nHindi | en\nSpanish | es\nFrench | fr\n Arabic | ar\nBengali | bn\n Russian | ru\n Portuguese | pt\n Indonesian | id", color = discord.Colour.red())
        await ctx.send(embed=embed)
      elif arg == None:
         error = discord.Embed(title=":x: Invalid argument", description="**+translate <language> <sentence>**", color = discord.Colour.red())
         await ctx.send(error)
      else:
        embeds = discord.Embed(description="Translating...", color = discord.Colour.red())
        msg = await ctx.send(embed=embeds)
        translator = Translator()
        translation = translator.translate(arg, dest=type)
        embed = discord.Embed(color = discord.Colour.green())
        embed.add_field(name=f"From {translation.src}:", value=f"{arg}", inline=False)
        embed.add_field(name=f"To {translation.dest}:", value=f"{translation.text}", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url="https://images-ext-2.discordapp.net/external/8LyhaOIVKavl5gXj51X0GaMKL-S4O6ZwWVoaQQbI0Aw/https/i.imgur.com/wmpg9F5.png")
        await msg.edit(embed=embed)

   
@translate.error
async def translate_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title="Slow it down!",description=f"C'mon, {error}", color = 0xff0000)
        await ctx.send(ctx.author.mention, embed=embed, delete_after=5)
        await msg.edit(embed=embed)
    else:
        embed=discord.Embed(title="Error!",description=f"{error}", color = 0xff0000)
        await ctx.send(ctx.author.mention, embed=embed)
        await msg.edit(embed=embed)
        
@client.command()
async def slap(ctx, member: discord.Member = None):
    file = open("system.json", "r")
    load = json.load(file)

    if "fun" in load:

        return await ctx.send(":no_entry_sign: The `fun` commands are currently **disabled**.")
    if member is None:
        await ctx.send("Mention somebody to slap.")
    else:
        
        possible_responses = [
            'https://media1.tenor.com/images/6a288821409733bb848f14b9443f8b73/tenor.gif?itemid=4079563',
            'https://media1.tenor.com/images/d2257d7a3803a4aabcdddf3878149d01/tenor.gif?itemid=14279719',
            'https://media1.tenor.com/images/3c161bd7d6c6fba17bb3e5c5ecc8493e/tenor.gif?itemid=5196956'
        ]
        embed = discord.Embed(title=f"{ctx.author} slapped {member.name}!")
        embed.set_image(url=random.choice(possible_responses))
        await ctx.send(embed=embed)
        
@commands.cooldown(1, 5, commands.BucketType.user)
@client.command()
async def swiss(ctx):
    file = open("system.json", "r")
    load = json.load(file)

    if "fun" in load:

        return await ctx.send(":no_entry_sign: The `fun` commands are currently **disabled**.")
    possible_responses = [
        'https://www.youtube.com/watch?v=WHY8VMBs0s4',
        'https://www.youtube.com/watch?v=SvyI-VnTTmg',
        'https://www.youtube.com/watch?v=V9XycELn_3I&list=PLYMreygRONRBbtzuEYLe9DLsMLqLMOGQ6&index=164',
        'https://www.youtube.com/watch?v=we3NGmTTGss&index=194&list=PLYMreygRONRBbtzuEYLe9DLsMLqLMOGQ6',
        'https://www.youtube.com/watch?v=3ppge2TwQlw',
        'https://www.youtube.com/watch?v=I4UX5w4nqz0',
        'https://www.youtube.com/watch?v=7fVp1PRUteQ',
        'https://www.youtube.com/watch?v=1NaKul-O3hE',
        'https://www.youtube.com/watch?v=M6qet67TqMY',
        'https://www.youtube.com/watch?v=6GApOqt2YHI',
        'https://www.youtube.com/watch?v=AOx4Ql8gCBE',
        'https://www.youtube.com/watch?v=WSWkZq6w7-Y',
        'https://www.youtube.com/watch?v=4WgFfR3GHVY',
        'https://www.youtube.com/watch?v=c1HpAGX59Bg',
        'https://www.youtube.com/watch?v=9w4tytaqH84',
        'https://www.youtube.com/watch?v=UVpsxPJjAPg',
        'https://www.youtube.com/watch?v=1KUzLpcVK2Q',
        'https://www.youtube.com/watch?v=Mksekezsz-4',
        'https://www.youtube.com/watch?v=e_jAqmVF0cs',
        'https://www.youtube.com/watch?v=f-T0sMEUu-A',
        'https://www.youtube.com/watch?v=jWXgS6PkPXw',
        'https://www.youtube.com/watch?v=COWBX-Mg-WA',
        'https://www.youtube.com/watch?v=t8bP3sq9br4',
        'https://www.youtube.com/watch?v=G3AQChqL8WE',
        'https://www.youtube.com/watch?v=g7EcA1uQbo8',
        'https://www.youtube.com/watch?v=VQopCkBJPOo'
    ]
    await ctx.send("Here's a random video {}".format(random.choice(possible_responses)))
        
@swiss.error
async def swiss_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title="Slow it down cowboy!",description=f"C'mon, {error}", color = 0xff0000)
        await ctx.send(embed=embed)
        
@client.command()
@commands.has_permissions(view_audit_log=True)
@commands.bot_has_permissions(view_audit_log = True)
async def recentlog(ctx):
  async for entry in ctx.guild.audit_logs(limit=1):
    
    """
    msg = f"{entry.user} did {entry.action} to {entry.target}"
    
    embed = discord.Embed(color = discord.Colour.red(), description=msg)
  
    await ctx.send(embed=embed)
    """
    
    embed = discord.Embed()
    
    embed.color = discord.Color.red()
    
    embed.timestamp = entry.created_at
    
    embed.set_footer(text = f"ID: {entry.id} | Timestamp")
    
    embed.set_thumbnail(url = entry.user.avatar_url)
    
    embed.set_author(name = "Audit Log", icon_url = ctx.guild.icon_url)
    
    embed.add_field(name="User", value = entry.user, inline = False)
    
    embed.add_field(name = "Target", value = entry.target, inline = False)
    
    embed.add_field(name = "Action", value = entry.action, inline = False)
    
    embed.add_field(name = "Reason", value = entry.reason, inline = False)
    
    embed.add_field(name = "Extra Information", value = entry.extra, inline = False)
    
    embed.add_field(name = "Before", value = entry.before, inline = False)
    
    embed.add_field(name = "After", value = entry.after, inline = False)
    
    await ctx.send(embed=embed)
    
@recentlog.error
async def recentlog_handler(ctx, error):
    if isinstance(error, BotMissingPermissions):
        embed=discord.Embed(description=f":x: I need the permission `{' '.join(error.missing_perms)}` to do that!", color = 0xff0000)
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description = ":x: You need the `View Audit Log` permission to do that.", color = 0xff0000)
        await ctx.send(embed=embed)
        raise CustomException() from error
    else:
        raise error
        
# Money System

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def gamble(ctx, amount: int = None):

    x = ":x:"

    if amount == None:

      embed = discord.Embed()
    
      embed.title = "{} Invalid argument".format(x)
    
      embed.description = "**+gamble <amount>**"
    
      embed.color = discord.Color.red()
    
      return await ctx.send(embed = embed)
    
      file = open("currency.json", "r")
    
      cur = json.load(file)
    
      if not str(ctx.guild.id) in cur:
    
        cur[str(ctx.guild.id)] = {}
    
      if not str(ctx.author.id) in cur[str(ctx.guild.id)]:
    
        return await ctx.send("You're not registered. Type `+register` to register.")
    
      ranNUM_1 = random.randint(0, 10)
    
      ranNUM_2 = random.randint(0, 10)
    
      xyz = 1 * amount / 4
    
      no_float_amount = "{:.0f}".format(xyz)
    
      divided_amount = 4 * amount / 5
    
      no_float = '{:.0f}'.format(divided_amount)
    
      coins = cur[str(ctx.guild.id)][str(ctx.author.id)]["coins"]
    
      embed = discord.Embed()
    
      if amount < 0:
    
        return await ctx.send("You can't gamble with negative numbers.")
    
      elif amount > coins:
    
        return await ctx.send("You only have {} coins.".format(coins))
    
      elif ranNUM_1 > ranNUM_2:
    
        cur[str(ctx.guild.id)][str(ctx.author.id)]["coins"] += int(no_float)
    
      dumps = open("currency.json", "w")
    
      json.dump(cur, dumps, indent = 4)
    
      embed.set_author(name = "{}'s gambling game".format(ctx.author.name), icon_url = ctx.author.avatar_url)
    
      embed.description = "You **won** {} coins!\nYou now have {} coins.".format(no_float, coins + int(no_float))
    
      embed.add_field(name = "{}".format(ctx.author.name), value = "Rolled a `{}`".format(ranNUM_1))
    
      embed.add_field(name = "SwissPlus", value = "Rolled a `{}`".format(ranNUM_2))
    
      embed.timestamp = ctx.message.created_at
    
      await ctx.send(embed = embed)
    
    else:
    
      cur[str(ctx.guild.id)][str(ctx.author.id)]["coins"] -= int(no_float_amount)
    
      dumps = open("currency.json", "w")
    
      json.dump(cur, dumps, indent = 4)
    
      embed.set_author(name = "{}'s gambling game".format(ctx.author.name), icon_url = ctx.author.avatar_url)
    
      embed.description = "You **lost** {} coins.\nYou now have {} coins.".format(no_float_amount, coins - int(no_float_amount))
    
      embed.add_field(name = "{}".format(ctx.author.name), value = "Rolled a `{}`".format(ranNUM_1))
    
      embed.add_field(name = "SwissPlus", value = "Rolled a `{}`".format(ranNUM_2))
    
      embed.timestamp = ctx.message.created_at
    
      await ctx.send(embed = embed)
      


@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def work(ctx):

  randomNum = random.randint(0, 100)

  currency_file = open("currency.json", "r")

  cur = json.load(currency_file)

  if not str(ctx.guild.id) in cur:

    cur[str(ctx.guild.id)] = {}

  if not str(ctx.author.id) in cur[str(ctx.guild.id)]:

    return await ctx.send("You're not registered. Type `+register` to register.")

  await ctx.send("You have worked your socks off and you earned yourself {} coins!".format(randomNum))

  cur[str(ctx.guild.id)][str(ctx.author.id)]["coins"] += randomNum

  dumps = open("currency.json", "w")

  json.dump(cur, dumps, indent = 4)
  
@work.error
async def work_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title="Slow it down cowboy!",description=f"C'mon, {error}", color = 0xff0000)
        await ctx.send(embed=embed)

@client.command()
async def register(ctx):

    with open("currency.json", "r") as f:
    
        cur = json.load(f)
    
    if not str(ctx.guild.id) in cur:
    
      cur[str(ctx.guild.id)] = {}
    
      cur[str(ctx.guild.id)][str(ctx.author.id)] = {}
    
      cur[str(ctx.guild.id)][str(ctx.author.id)]["coins"] = 0
    
      cur[str(ctx.guild.id)][str(ctx.author.id)]["bank"] = 0
    
      with open("currency.json", "w") as f:
    
        json.dump(cur, f, indent = 4)
    
      return await ctx.send("Registered.")
    
    else:
    
        if not str(ctx.author.id) in cur[str(ctx.guild.id)]:
    
          cur[str(ctx.guild.id)][str(ctx.author.id)] = {}
    
          cur[str(ctx.guild.id)][str(ctx.author.id)]["coins"] = 0
    
          cur[str(ctx.guild.id)][str(ctx.author.id)]["bank"] = 0
    
          with open("currency.json", "w") as f:
    
            json.dump(cur, f, indent = 4)
    
          return await ctx.send("Registered.")
    
        else:
    
            await ctx.send("You're already registered.")


@client.command(aliases = ["bal"])
async def balance(ctx, user: discord.Member = None):

  file = open("currency.json", "r")

  cur = json.load(file)

  if not str(ctx.guild.id) in cur:

    cur[str(ctx.guild.id)] = {}

  if user == None:

    if not str(ctx.author.id) in cur[str(ctx.guild.id)]:

      return await ctx.send("You're not registered. Type `+register` to register.")

    coins = cur[str(ctx.guild.id)][str(ctx.author.id)]["coins"]

    bank = cur[str(ctx.guild.id)][str(ctx.author.id)]["bank"]

    msg = "```"

    msg += "Your balance\n\nCoins: {}\nBank: {}".format(coins, bank)

    msg += "```"

    #await ctx.send(msg)
    
    embed = discord.Embed(description="Your Balance", colour=discord.Colour.blue())
    embed.add_field(name="Coins:", value=f"{coins}", inline=False)
    embed.add_field(name="Bank:", value=f"{bank}", inline=False)
    await ctx.send(embed=embed)

  else:

    if not str(user.id) in cur[str(ctx.guild.id)]:

      return await ctx.send("{} wasn't registered.".format(user.mention))

    coins = cur[str(ctx.guild.id)][str(user.id)]["coins"]

    bank = cur[str(ctx.guild.id)][str(user.id)]["bank"]

    msg = "```"

    msg += "{}'s balance\n\nCoins: {}\nBank: {}".format(user.name, coins, bank)

    msg += "```"

    #await ctx.send(msg)
    
    embed = discord.Embed(description=f"{user.name}'s Balance", colour=discord.Colour.blue())
    embed.add_field(name="Coins:", value=f"{coins}", inline=False)
    embed.add_field(name="Bank:", value=f"{bank}", inline=False)
    await ctx.send(embed=embed)
    
@gamble.error
async def gamble_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed(title="Slow it down cowboy!",description=f"C'mon, {error}", color = 0xff0000)
        await ctx.send(embed=embed)

client.run(os.environ['BOT_TOKEN'])
