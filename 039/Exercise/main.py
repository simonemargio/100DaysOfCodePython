from telethon.sync import TelegramClient, events
import time

  api_id = 0000000 
api_hash = '################################'


with TelegramClient('name', api_id, api_hash) as client:
   print(time.asctime(), '-', 'Auto-replying...')

   @client.on(events.NewMessage(pattern='(?i)^help$', func=lambda e: e.is_private))
   async def handler(event):
      time.sleep(1) 
      await event.reply('**Hi there!**🧘‍♀️\nhow are you?')      
  

   @client.on(events.NewMessage(pattern='(?i)doge', func=lambda e: e.is_private))
   async def handler(event):
   	time.sleep(1) 
   	await event.reply('https://i.gifer.com/3O6sm.gif',link_preview=False)      

   @client.on(events.NewMessage(pattern='(?i)doges', func=lambda e: e.is_private))
   async def handler(event):
      time.sleep(1) 
      await event.reply('https://i.gifer.com/3O6sm.gif') 

   @client.on(events.NewMessage(pattern='(?i)^wow$|^ToTheMoon$', func=lambda e: e.is_private))
   async def handler(event):
   	time.sleep(1) 
   	await event.reply('woof 🐶') 

   @client.on(events.NewMessage(pattern='(?i)^🧐$|^❤️$', func=lambda e: e.is_private))
   async def handler(event):
   	time.sleep(1) 
   	await event.reply('👀') 
	   
   client.run_until_disconnected()
   print(time.asctime(), '-', 'Stopped!')





