import json    
    
# Armor categories: Helm, Leg Armor, Chest Armor, Gauntlets
# Scaling categories: weapons, shields

def LoadData():
    """
    param: None
    Return:  map giving a key to each category of data
    Reads json files to extract data. The extracted data is put into a map
    for easy categorization.
    """
    master_dict = dict()
    
    # Opens and loads the ammo json file as a map
    ammoFile = open('data/ammos.json')
    ammo = json.load(ammoFile)
    master_dict["ammos"] = ammo
    
    # Opens and loads the armor json file as a map
    armorFile = open('data/armors.json')
    armor = json.load(armorFile)
    master_dict["armors"] = armor
    
    # Opens and loads the ashes json file as a map
    ashesFile = open('data/ashes.json')
    ashes = json.load(ashesFile)
    master_dict["ashes"] = ashes
    
    # Opens and loads the bosses json file as a map
    bossesFile = open('data/bosses.json')
    bosses = json.load(bossesFile)
    master_dict["bosses"] = bosses
    
    # Opens and loads the classes json file as a map
    classesFile = open('data/classes.json')
    classes = json.load(classesFile)
    master_dict["classes"] = classes
    
    # Opens and loads the creatures json file as a map
    creaturesFile = open('data/creatures.json')
    creatures = json.load(creaturesFile)
    master_dict["creatures"] = creatures
    
    # Opens and loads the incantations json file as a map
    incantationsFile = open('data/incantations.json')
    incantations = json.load(incantationsFile)
    master_dict["incantations"] = incantations
    
    # Opens and loads the items json file as a map
    itemsFile = open('data/items.json')
    items = json.load(itemsFile)
    master_dict["items"] = items
    
    # Opens and loads the locations json file as a map
    locationsFile = open('data/locations.json')
    locations = json.load(locationsFile)
    master_dict["locations"] = locations
    
    # Opens and loads the npcs json file as a map
    npcsFile = open('data/npcs.json')
    npcs = json.load(npcsFile)
    master_dict["npcs"] = npcs
    
    # Opens and loads the shields json file as a map
    shieldsFile = open('data/shields.json')
    shields = json.load(shieldsFile)
    master_dict["shields"] = shields
    
    # Opens and loads the sorceries json file as a map
    sorceriesFile = open('data/sorceries.json')
    sorceries = json.load(sorceriesFile)
    master_dict["sorceries"] = sorceries
    
    # Opens and loads the spirits json file as a map
    spiritsFile = open('data/spirits.json')
    spirits = json.load(spiritsFile)
    master_dict["spirits"] = spirits
    
    # Opens and loads the talismans json file as a map
    talismansFile = open('data/talismans.json')
    talismans = json.load(talismansFile)
    master_dict["talismans"] = talismans
    
    # Opens and loads the weapons json file as a map
    weaponsFile = open('data/weapons.json')
    weapons = json.load(weaponsFile)
    master_dict["weapons"] = weapons
    
    return master_dict
    
class DatabaseConnection(object):
    def __init__(self):
        self.data = LoadData()

def WeaponSearchBasedOnAttributeScaling(attribute,tier):
    """
    param attribute: Determines what attribute returned weapons will scale with
    param tier: Determines the strength of the attribute scaling for returned     
    weapons
    return: A map with keys that are weapon names and values that conatin their info
    Returns a map of weapons that have matching attribute scaling.
    """
    dbCon = DatabaseConnection()
    weapon_map = {}
    for weapon in dbCon.data['weapons']:
        for wAttribute in weapon["scalesWith"]:
            
            if wAttribute["name"].lower() == attribute.lower() and\
            wAttribute["scaling"].lower() == tier.lower():
                weapon_map[weapon["name"]] = weapon
                break
    return weapon_map

def ArmorSearch(armorType):
  dbCon = DatabaseConnection()
  armor_set = set()
  for armor in dbCon.data['armors']:
    if armor['category'] == armorType and '(altered)' not in armor['name']:
      armor_set.add(armor['name'])
  return armor_set

def WeaponSearch(weaponType):
  pass