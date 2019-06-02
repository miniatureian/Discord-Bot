import discord
import tkinter
import asyncio
bot = discord.Client()
root = tkinter.Tk()

# Methods without arguments to be called from buttons
def start():
    with open('token.txt') as f:
        TOKEN = f.readline()
    bot.run(TOKEN)
def stop():
    bot.close()

# This is how discord.py uses messages
@bot.event
async def on_message(message):
    if message.content == 'ping':
        await message.channel.send('pong')

if __name__ == '__main__':
    # Building a GUI
    canvas = tkinter.Canvas(root, height=300, width=400, bd=5)
    canvas.pack()
    frame = tkinter.Frame(root, bd=5)
    frame.place(relx=0.05, rely=0.05, relwidth=.9, relheight=.9)

    btn_start = tkinter.Button(frame, text="Start", command=start)
    btn_start.place(relx=0.25, rely=.4, relheight=.2, relwidth=0.25)
    btn_stop = tkinter.Button(frame, text="Stop", command=stop)
    btn_stop.place(relx=0.5, rely=.4, relheight=.2, relwidth=0.25)

    # Here's the juicy code bits that we've come for:
    root.mainloop()
