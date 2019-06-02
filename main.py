import tkinter as tk
import discord
import asyncio

# Constants
HEIGHT = 700
WIDTH = 800
bg_color = '#80c1ff'

guild = None
botUser = None
bot = discord.Client()

# GUI init
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bd=5)
canvas.pack()
frame_1 = tk.Frame(root, bg=bg_color, bd=5)
frame_1.place(relx=0.05, rely=0.05, relwidth=.9, relheight=.45)
txt_entry = tk.Entry(frame_1)
txt_entry.place(relwidth=0.80, relheight=0.2)

@bot.event
async def on_ready():
    global guild, botUser
    guild = bot.get_guild(513368774506971150)
    botUser = guild.me

    list_channels = []
    generator_channels = bot.get_all_channels()

    cont = True
    while cont:
        try:
            chan = next(generator_channels)
            if isinstance(chan, discord.TextChannel):
                if botUser in chan.members:
                    list_channels.append(chan)
                    print(chan)
        except StopIteration:
            cont = False


    # Build a list of buttons that are the channels we can talk to
    list_btn_send = []
    scale = 1.0 / len(list_channels)
    for chan in list_channels:
        list_btn_send.append( tk.Button( frame_1, text=chan.name, command=lambda: asyncio.ensure_future(chan.send(txt_entry.get()))))
        list_btn_send[-1].place(relx=0.80, rely=(len(list_btn_send)-1) * scale, relheight=scale, relwidth=0.20)
    root.mainloop()
    print('Logged on as ', botUser, ' to ', len(list_channels), ' channels')


@bot.event
async def on_message(message):
    global guild
    # don't respond to ourselves
    if message.author == bot.user:
        return
    else:
        print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

        if message.content == 'ping':
            await message.channel.send('pong')
        elif "bot.member_count" == message.content.lower():
            await message.channel.send(f'{guild.member_count}')
        elif "bot.logout()" == message.content.lower():
            await bot.close()


async def fn_send(content, chan):
    await chan.send(content)


# Bot init
with open('token.txt') as f:
    Token = f.readline()
bot.run(Token)












































