try:
  from os import system, name
except:
  print("Error: Please install the required libaries")
  exit()
try:
  import json
  import discord
  from colorama import Fore
  import requests
  import asyncio
except:
  system("pip install discord discord.py-self requests colorama asyncio")

with open("config.json", "r") as f:
  config = json.load(f)

class MyClient(discord.Client):
  async def on_voice_state_update(self, member, before, after):
    if before.channel != after.channel:
      if not before.channel and after.channel and config["JoinChannel"]:
        if member.id in config['StalkID(s)']:
          webhook = {
            "embeds": [
              {
                "title": f"{member} joined `{after.channel}`",
                "color": 65280
              }
            ],
            "attachments": []
          }
          requests.post(config['Webhook'], json = webhook)
      elif before.channel and after.channel and config["SwitchChannel"]:
        if member.id in config['StalkID(s)']:
          webhook = {
            "embeds": [
              {
                "title": f"{member} switched channels from `{before.channel}` to `{after.channel}`",
                "color": 16776960
              }
            ],
            "attachments": []
          }
          requests.post(config['Webhook'], json = webhook)
      elif not after.channel and config["LeaveChannel"]:
        if member.id in config['StalkID(s)']:
          webhook = {
            "embeds": [
              {
                "title": f"{member} left `{before.channel}`",
                "color": 16711680
              }
            ],
            "attachments": []
          }
          requests.post(config['Webhook'], json = webhook)


try:
  system('cls' if name=='nt' else 'clear')
  print(f"{Fore.RESET}Stalking user(s): {config['StalkID(s)']}")
  asyncio.run(MyClient().run(config['Token']))
except:
  system('cls' if name=='nt' else 'clear')
  print(f"{Fore.RED}Error!{Fore.RESET}")