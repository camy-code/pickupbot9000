# for this code we use a pickup line API
# https://getpickuplines.herokuapp.com
import requests
import os
from keep_alive import keep_alive

my_secret = os.environ['TOKEN'] #this is my secret tokenn

import discord

client = discord.Client()

@client.event
async def on_ready(): #we need this for it 
  print("Hello we are ready to go!")
  print(client.user)
  pass

@client.event
async def on_message(message): #we need this for it 
  if message.author == client.user:
    return 

  if message.content.startswith('!id:'):
    num = message.content.split(':')[1].strip()
    if num.isdigit():
      if 0<= int(num) <= 94:
        r = requests.get(f'http://getpickuplines.herokuapp.com/lines/' + num)
        await message.channel.send(r.json()['line'])
      else:
        await message.channel.send("Enter a valid number")
    else:
        await message.channel.send("Enter a Digit or valid number")
    
  
  if message.content.startswith('!pickup'):
    response = requests.get("http://getpickuplines.herokuapp.com/lines/random")
    await message.channel.send(response.json()['line'])

  if message.content.startswith('!help'):
    a = """This is a pickup line bot with two commands
    1. !pickup - gives a random pickup line
    2. !id:0 - gives the first pickpup line in the API. There is 94 in total!"""
    await message.channel.send(a)


keep_alive()
client.run(my_secret) #this is where we put the token gotta be 
#we are at 16:29 in the video
