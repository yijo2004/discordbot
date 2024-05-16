import discord
from discord.ext import commands
from discord.ui import Button, View
import random
import json

bot = commands.Bot()

@bot.event
async def on_ready():
    print("-----------------------------")
    print("-----------Online------------")
    print("-----------------------------")

# @bot.slash_command(name="hello", description='this says hello', guild_ids=[1233635512007266374])
# async def hello(ctx: discord.Interaction):
#     await ctx.respond(f"Hello {ctx.user.mention}!")

ids = [1233635512007266374, 610247347695255562]

########################## Random Map Command  ###########################
@bot.slash_command(name="random_map", description='This will pick a random Valorant map', guild_ids=ids)
async def random_map(ctx: discord.Interaction):
    num = random.randint(0, 9)
    maps = ["Bind", "Haven", "Split", "Ascent", "Icebox", "Breeze", "Fracture", "Pearl", "Lotus", "Sunset"]
    await ctx.respond(file=discord.File('./maps/'+maps[num]+'.png'))
    await ctx.channel.send("The map chosen is: " + f"***{maps[num]}***")
###########################################################################

########   Variables   ##########
members1 = ""
maybe1 = ""
final = ""
lol = 0
xd = 0
dictionary = {
"Hazal Eyletmez": "<@326465432389287946>",
"Ling Ying Wei": "<@409149245711581204>",
"my doot": "<@224562633825583105>",
"Ryo Kiritani": "<@451932020667318274>",
"sabine": "<@414602150010683403>",
"Shun": "<@619975843065888769>",
"Sunwoo Han": "<@326471666630656002>",
"Tala Nicole Dimaapi Valdez": "<@497858508969082911>",
"TheOriginalJ": "<@522151150594818079>",
"therks": "<@350409255217528844>",
"Varun Batra": "<@321290301169991681>",
"Zyanya Mondragón": "<@266705722408960000>",
"loaf": "<@493757711721168907>",
"Tayane Alves": "<@270638440675147777>",
"Leo": "<@414781206786342912>",
"evie!!": "<@512091726056259584>",
"duncanco": "<@257336528626384897>",
"PsychedelicSuperJesus": "<@558342153001107457>",
"Mr. Woman": "<@424678116514988053>",
"MadaMada": "<@273128060675555329>",
"Amir El Amari": "<@189483157894987776>",
"Social": "<@311305936742645763>"
}
###################################


############################# TENQ  #######################################

class ResetButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.blurple, emoji="❌")
    async def callback(self, interaction):
        global members1
        global maybe1
        members1 = ""
        maybe1 = ""
        await interaction.response.edit_message(content="# THE 10 QUEUE IS DISBANDED", embed = None, view = None)
        #add code here
        if(lol == 10):
            messages = await interaction.channel.history(limit=100).flatten()  # Adjust limit as necessary
            bot_messages = [message for message in messages if message.author == interaction.client.user]
            for message in bot_messages[:3]:  # Get only up to the last 3 messages sent by the bot
                await message.delete()

class BlurpleButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.blurple, emoji="🔄")
    async def callback(self, interaction):
        global final
        usernames1 = final.strip().split('\n')
        #Add code here 
        random.shuffle(usernames1)  # Shuffle the list of usernames randomly
        mid_point = len(usernames1) // 2  # Find the midpoint to split the list into two teams
        team1 = '\n'.join(usernames1[:mid_point])  # First half for team 1
        team2 = '\n'.join(usernames1[mid_point:])  # Second half for team 2

        embed = discord.Embed(title="THE TEAMS", color = discord.Color.blurple())
        embed.add_field(name="Team 1: ", value = team1, inline=False)
        embed.add_field(name="Team 2: ", value = team2, inline=False)
        await interaction.response.edit_message(content = "# LOCKED IN", embed = embed)


class GreenButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.green, emoji="✔")
    async def callback(self, interaction):
        global members1
        global maybe1
        global final
        global lol
        global xd
        if(members1.find(interaction.user.display_name) == -1):
            members1 = members1 + "\n" + interaction.user.display_name
            if (maybe1.find(interaction.user.display_name) != -1):
                maybe1 = maybe1.replace(f'\n{interaction.user.display_name}', '')
        lol = members1.count('\n')
        xd = maybe1.count('\n') + lol
        mem_count = str(lol)
        ###########################         ATTING
        if (mem_count == "10"):
            final = members1
            embed1 = discord.Embed(title=f"Members ({mem_count}/10)", color = discord.Color.blurple())
            embed1.add_field(name="List: ", value = members1, inline=False)
            view = View()
            view.clear_items()
            teammake = BlurpleButton("Create Teams?")
            reset = ResetButton("New Game?")
            view.add_item(teammake)
            view.add_item(reset)
            view.timeout = None
            await interaction.response.edit_message(content = "# LOCKED IN", embed = embed1, view = view)
            usernames = members1.strip().split('\n')
            listofnames = ""
            for username in usernames:
                atting = dictionary[username]
                listofnames = listofnames + atting + " "
            await interaction.channel.send(listofnames)
            ######## Random Map Generator
            num = random.randint(0, 9)
            maps = ["Bind", "Haven", "Split", "Ascent", "Icebox", "Breeze", "Fracture", "Pearl", "Lotus", "Sunset"]
            await interaction.channel.send(file=discord.File('./maps/'+maps[num]+'.png'))
            await interaction.channel.send("The map chosen is: " + f"***{maps[num]}***")
            members1 = ""
            maybe1 = ""
            return
        #############################
        embed = discord.Embed(title=f"Members ({mem_count}/10)", color = discord.Color.blurple())
        embed.add_field(name="✅ Confirmed ✅: ", value = members1, inline=False)
        embed.add_field(name="❓ Maybe ❓: ", value = maybe1, inline=False)
        await interaction.response.edit_message(content = "# Calling all Gamers", embed = embed)

class GrayButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.gray, emoji="❔")
    async def callback(self, interaction):
        global members1
        global maybe1
        global lol
        global xd
        if(maybe1.find(interaction.user.display_name) == -1):
            maybe1 = maybe1 + "\n" + interaction.user.display_name
            if (members1.find(interaction.user.display_name) != -1):
                members1 = members1.replace(f'\n{interaction.user.display_name}', '')
        lol = members1.count('\n')
        xd = maybe1.count('\n')+ lol
        mem_count = str(lol)
        embed = discord.Embed(title=f"Members ({mem_count}/10)", color = discord.Color.blurple())
        embed.add_field(name="✅ Confirmed ✅: ", value = members1, inline=False)
        embed.add_field(name="❓ Maybe ❓: ", value = maybe1, inline=False)
        await interaction.response.edit_message(content = "# Calling all Gamers", embed = embed)

@bot.slash_command(name="tenq", description="Calls the legendary 10q", guild_ids=ids)
async def tenq(ctx: discord.Interaction):
    button = GreenButton("LET ME IN")
    button1 = GrayButton("Maybe...")
    button2 = ResetButton("New Game?")

    view = View()
    view.add_item(button)
    view.add_item(button1)
    view.add_item(button2)
    view.timeout = None

    # @ valorant
    # await ctx.channel.send('<@&1081317738577940551>')

    embed = discord.Embed(title="Members (0/10)", color = discord.Color.blurple())
    embed.add_field(name="✅ Confirmed ✅: ", value = "\n", inline=False)
    embed.add_field(name="❓ Maybe ❓: ", value = "\n", inline=False)
    await ctx.respond("# Calling all Gamers", embed = embed, view = view)

    # await ctx.respond("# Calling all Gamers", view = view)
###########################################################################

@bot.slash_command(name="temp_add_member", description="Temporarly add member to 10q slots (don't use if you don't know what you are doing)", guild_ids=ids)
async def add_member(ctx: discord.Interaction, user: discord.Option(str, description="Username", required=True), at_code: discord.Option(str, description="@ code", required=True)): # type: ignore
    global dictionary
    if user in dictionary:
        await ctx.respond("Already exists!")
    else:
        dictionary[user] = at_code
        await ctx.respond(f"Temporary User: {user} added")

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    token = config.get('DISCORD_BOT_TOKEN')
    if token is None:
        raise ValueError("Token not found in configuration file")
bot.run(token)

# valorant @ <@&1081317738577940551>