try:from os import system,name
except:print('Error: Please install the required libaries');exit()
try:import json,discord;from colorama import Fore;import requests,asyncio
except:system('pip install discord discord.py-self requests colorama asyncio')
with open('config.json','r')as f:config=json.load(f)
class MyClient(discord.Client):
	async def on_voice_state_update(E,member,before,after):
		C=before;B=after;A=member
		if C.channel!=B.channel:
			if not C.channel and B.channel and config['JoinChannel']:
				if A.id in config['StalkID(s)']:D={'embeds':[{'title':f"{A} joined `{B.channel}`",'color':65280}],'attachments':[]};requests.post(config['Webhook'],json=D)
			elif C.channel and B.channel and config['SwitchChannel']:
				if A.id in config['StalkID(s)']:D={'embeds':[{'title':f"{A} switched channels from `{C.channel}` to `{B.channel}`",'color':16776960}],'attachments':[]};requests.post(config['Webhook'],json=D)
			elif not B.channel and config['LeaveChannel']:
				if A.id in config['StalkID(s)']:D={'embeds':[{'title':f"{A} left `{C.channel}`",'color':16711680}],'attachments':[]};requests.post(config['Webhook'],json=D)
try:system('cls'if name=='nt'else'clear');print(f"{Fore.RESET}Stalking user(s): {config['StalkID(s)']}");asyncio.run(MyClient().run(config['Token']))
except:system('cls'if name=='nt'else'clear');print(f"{Fore.RED}Error!{Fore.RESET}")