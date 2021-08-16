
import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^rev(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("`Кручу барабан, и бахаю!🔫`")
	sleep(1)
	import random
   
 s = True
   
 revolver_drum = [0, 0, 0, 0, 0, 1]
 
 import random   s = True   revolver_drum = [0, 0, 0, 0, 0, 1]
    while s:
           shot = random.choice(revolver_drum)
           if k == 1 :
                 s = False
         typew.edit('Убит!')
      else :
               typew.edit('Живой!')
       while s:
                shot = random.choice(revolver_drum)
                 if k == 1 :
                          s = False
         typew.edit('Убит!')
      else :
               typew.edit('Живой!')
	await typew.edit("`крутим барабан еще раз?`")
