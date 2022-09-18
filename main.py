import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
import DataLoad

client = discord.Client()

####### For encouragement bot #################
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragments = [
    "Cheer up!", "Hang in there.", "You are a great person / bot!"
]

def get_quote():
    """
    Params: None
    Return: string
    Returns a random quote from zenquotes by qerying their api.
    """
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def update_encouragements(encouraging_message):
    """
    Param: string
    Return: None
    Updates the table of encouragements that can be produced with a new one.
    """
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db['encouragements'] = [encouraging_message]


def delete_encouragement(index):
    """
    Param: int
    Return: False if there are no encouragements to delete else true 
    Updates the table of encouragements that can be produced with a new one.
    """
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements
        return True
    else:
        return False
##############################################   

@client.event
async def on_ready():
    print("Ranni is online.")


@client.event
async def on_message(message):
    # Don't listen on bots own messages
    if message.author == client.user:
        return

    msg = message.content

    # Register user into database and create association map for categories
    if str(message.author.id) not in db.keys():
      db[str(message.author.id)] = {'kills':0,'helmeti':{},'chesti':{},'legsi':{},'gauntsi':{}}
    catMap = {'helmets':('Helm','helmeti'),'chest':('Chest Armor','chesti'),'legs':('Leg Armor','legsi'),'gauntlets':      ('Gauntlets','gauntsi')}
      
    ########### Encouragement bot ################
    # Sends an inspirational quote
    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    # Load new encouragements
    options = starter_encouragments
    if "encouragements" in db.keys():
        options.extend(db["encouragements"])

    # Detects if a sad word sent and sends an encouraging message
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    # Adds new encouragements: $new Main character energy.
    if msg.startswith('$new'):
        encouraging_message = msg.split("$new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")

    # Deletes unwanted encouraging messages: $del Don't be a loser.
    if msg.startswith('$del'):
        encouragments = []
        index = int(msg.split("$del", 1)[1])

        if not delete_encouragement(index):
            await message.channel.send(
                "There are not enough messages to delete the one you have selected."
            )

        encouragments = db["encouragements"]
        encouragements_str = ""
        for i, ch in enumerate(encouragments):
            encouragements_str += "{}. {}\n".format(i, ch)
        await message.channel.send("Updated list of encouragements:\n" +
                                   encouragements_str)

    # Displays the current encouragements
    if msg.startswith('$display_usr_msgs'):
        encouragments = db["encouragements"]
        encouragements_str = ""
        for i, ch in enumerate(encouragments):
            encouragements_str += "{}. {}\n".format(i, ch)
        await message.channel.send("List of encouragements with indexs:\n" +
                                   encouragements_str)
    ######################################################################

    ################ Elden Ring Bot #################
    ################ Sorted Alphabetically #############

    # Adds kills to player object: $add 4
    if msg.startswith('$add_kills'):
      kill_quant = int(msg.split("$add_kills ", 1)[1])
      db[str(message.author.id)]['kills'] += kill_quant
      await message.channel.send("The tarnished has logged {} conquered souls".format(kill_quant))

    # Promotes users to a higher roul if they have enough souls
    if msg.startswith('$ascend'):
      kills = int(db[str(message.author.id)]['kills'])
      
      if kills >= 1000:
        role = discord.utils.get(message.guild.roles,name = "Elden Lord")
        await message.author.add_roles(role)
        if role in message.author.roles:
          await message.channel.send("{} conquer more souls to ascend further...".format(message.author))
        else:
          await message.channel.send("OOOOOOoooOOoOoO... {} has become THE Elden Lord!".format(message.author))
        
      elif kills >= 750:
        role = discord.utils.get(message.guild.roles,name = "Lord of Cinder")
        await message.author.add_roles(role)
        if role in message.author.roles:
          await message.channel.send("{} conquer more souls to ascend further...".format(message.author))
        else:
          await message.channel.send("Congratulations! {} has become Lord of Cinder!".format(message.author))
        
      elif kills >= 500:
        role = discord.utils.get(message.guild.roles,name = "Gwyn's Dad")
        await message.author.add_roles(role)
        if role in message.author.roles:
          await message.channel.send("{} conquer more souls to ascend further...".format(message.author))
        else:
          await message.channel.send("Congratulations! {} has become Gwyn's Dad!".format(message.author))
          
      elif kills >= 250:
        role = discord.utils.get(message.guild.roles,name = "Pygmy Lord")
        await message.author.add_roles(role)
        if role in message.author.roles:
          await message.channel.send("{} conquer more souls to ascend further...".format(message.author))
        else:
          await message.channel.send("Congratulations! {} has become a Pygmy Lord!".format(message.author))
        
      elif kills >= 100:
        role = discord.utils.get(message.guild.roles,name = "Champion")
        await message.author.add_roles(role)
        if role in message.author.roles:
          await message.channel.send("{} conquer more souls to ascend further...".format(message.author))
        else:
          await message.channel.send("Congratulations! {} has become a Champion!".format(message.author))
        
      elif kills >= 50:
        role = discord.utils.get(message.guild.roles,name = "Lord")
        await message.author.add_roles(role)
        if role in message.author.roles:
          await message.channel.send("{} conquer more souls to ascend further...".format(message.author))
        else:
          await message.channel.send("Congratulations! {} has become a Lord!".format(message.author))
        
      elif kills >= 25:
        role = discord.utils.get(message.guild.roles,name = "Undead")
        await message.author.add_roles(role)
        if role in message.author.roles:
          await message.channel.send("{} conquer more souls to ascend further...".format(message.author))
        else:
          await message.channel.send("Congratulations! {} has become an Undead!".format(message.author))
          
      elif kills >= 5:
        role = discord.utils.get(message.guild.roles,name = "Hollow")
        await message.author.add_roles(role)
        if role in message.author.roles:
          await message.channel.send("{} conquer more souls to ascend further...".format(message.author))
        else:
          await message.channel.send("Congratulations! {} has gone Hollow!".format(message.author))
          
      else:
        await message.channel.send("{} conquer more souls to ascend...".format(message.author))

    # Provides users with a table displaying the amount of kills needed to gain higher roles
    if msg.startswith('$ascension_info'):
      table = "-----------------------------------------\n"+\
              "Verified Kill Requirement | Role Earned  \n"+\
              "-----------------------------------------\n"+\
              "            5             |   Hollow     \n"+\
              "-----------------------------------------\n"+\
              "            25            |    Undead    \n"+\
              "-----------------------------------------\n"+\
              "            50            |     Lord     \n"+\
              "-----------------------------------------\n"+\
              "           100            |   Champion   \n"+\
              "-----------------------------------------\n"+\
              "           250            |  Pygmy Lord  \n"+\
              "-----------------------------------------\n"+\
              "           500            |  Gwyn's Dad  \n"+\
              "-----------------------------------------\n"+\
              "           750            |  Lord of Cinder\n"+\
              "-----------------------------------------\n"+\
              "           1000           |  Elden Lord  \n"
      await message.channel.send(table)

    # Displays a table of available user commands
    if msg.startswith('$help'):
      helpMessage = "$add_kills 4 - This would add 4 kills to a player's logged kills\n" +\
      '$ascend - Checks to see if you are ready to elevate tiers, if you are ready you will\n' +\
      '$ascension_info - Gives a display of how many souls one needs to atain to ascend\n' +\
      '$show_kills - Provides the number of logged kills a player has\n' +\
      '$remove_kills 2 - This would remove 2 of a players logged kills\n' +\
      '$weapon_scale fai/str/dex/int C - Choose an attribute and a scaling level and this command will return a list of weapons that meet that criteria\n' +\
      '$view_armor legs/chest/helmets/gauntlets - This would show all the leg armor and whther or not you have logged it in your collection\n' +\
      "$log_armor chest 1 5 20 - This would log chest armor with ID's 1,5, and 20 as aquired"
      
      await message.channel.send(helpMessage)
      
    # Shows how many kills a user has
    if msg.startswith('$show_kills'):
      kills = int(db[str(message.author.id)]['kills'])
      if kills > 0:
        await message.channel.send('Total verified kills: ' + str(kills))
      else:
        await message.channel.send('No logged kills')

    # Removes a users kills: $remove_kills 2
    if msg.startswith('$remove_kills'):
      kill_quant = int(msg.split("$remove_kills ", 1)[1])
      if int(db[str(message.author.id)]) > 0:
        db[str(message.author.id)] -= kill_quant
      else:
        await message.channel.send('No logged kills')
        
    # Searches for weapons based on their attribute scaling: $weapon_scale dex/fai/str/int E/D/C/B/A/S
    if msg.startswith('$weapon_scale'):
      msgList = msg.split()
      attribute = msgList[1]
      scaling = msgList[2]
      weapon_map = DataLoad.WeaponSearchBasedOnAttributeScaling(attribute,scaling)
      weaponString = ''
      for weapon in weapon_map.keys():
        weaponString += weapon + '\n'
      await message.channel.send(weaponString)

    # Allows users to view what armors they have collected: $view_armor legs/chest/helmets/gauntlets
    if msg.startswith('$view_armor'):
      category = msg.split('$view_armor ',1)[1].lower()
      armorString = ''
      armorString += '{:>3s}. {:<30s}{:<14s}\n'.format('ID','Name','Status')
      available = DataLoad.ArmorSearch(catMap[category][0])
      achieved = db[str(message.author.id)][catMap[category][1]]
      count = 1
      for armor in available:
        if armor in achieved:
          armorString += '{:>3s}. {:<30s}{:<14s}\n'.format(str(count),armor,'AQUIRED')
        else:
          armorString += '{:>3s}. {:<30s}{:<14s}\n'.format(str(count),armor,'X')
        if count == int(len(available)*.2) or count == int(len(available)*.4) or count == int(len(available)*.6) or count == int(len(available)*.8):
          await message.channel.send(armorString)
          armorString = ''
        count += 1
          
      await message.channel.send(armorString)

    # Allows users to log what armor they have collected: $log_armor chest 1 4 5 56 60
    if msg.startswith('$log_armor'):
      category = msg.split()[1].lower()
      indexs = set(msg.split()[2:])
      available = DataLoad.ArmorSearch(catMap[category][0])
      achieved = db[str(message.author.id)][catMap[category][1]]
      for index,armor in enumerate(available):
        if str(index+1) in indexs and armor not in achieved:
          db[str(message.author.id)][catMap[category][1]][armor] = 1
      await message.channel.send('Armor logged! Use $view_armor to check collection.')
    
    if msg.startswith('$image'):
      await message.channel.send(file=discord.File('assets/Mint1/Elden_Image_Mint1GolDiamond1.png'))
    
keep_alive()
try:        
  client.run(os.environ['TOKEN'])
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  os.system('kill 1')
  os.system("python restarter.py")
  
  
  
    
