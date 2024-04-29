#Noah French
#April 24, 2024
#This code is for the nested dictionaries assignment

#makes a list of all the characters
characters = {
    'mario': {
        'character_playable': 'mario',
        'character_discription': 'Mario is a plumber for the Mushroom Kingdom',
            },
    
    'daisy': {
        'character_playable': 'daisy',
        'character_discription': 'Dasiy is the princess of Sarasaland',
        },
    
    'rosalina': {
        'character_playable': 'rosalina',
        'character_discription': 'Rosalina is the protecter of the cosmos',
        },
    }

#makes a list of all the items
items = {
    'mushroom': {
        'item_usable': 'mushroom',
        'item_discription': 'This item increases your speed and power',
            },
    
    'blooper': {
        'item_usable': 'blooper',
        'item_discription': 'This item blinds any enemy it is used on for a short amount of time',
        },
    
    'fire_flower': {
        'item_usable': 'fire flower',
        'item_discription': 'This item gives you the poweer to throw fire balls',
        },
    }

#makes a list of all the items
locations = {
    'mushroom_kingdom': {
        'location': 'mushroom kingdom',
        'location_discription': 'This place is home to our hero Mario! A place filled with mushrooms and Toads',
            },
    
    'yoshis_island': {
        'location': "Yoshi's Island",
        'location_discription': 'This place is a Yoshi Sancuary, with lush green forests and amazing waterfalls',
        },
    
    'bosers_castle': {
        'location': "Bowser's Castle",
        'location_discription': "This place is Bowser's land! Filled with evil goombas and lava",
        },
    }

#print out the characters into a statement
print("Characters:")
for character, character_info in characters.items():
    """define the character and their discription and prints out the statement"""
    playable = character_info ['character_playable'].title()
    discription = character_info ['character_discription']
    print(f"You chose to play {playable}!")
    print(f"{discription}!")
    print("\n")
    
#print out the items into a statement
print("Items:")
for item, item_info in items.items():
    """define the items and their discription and prints out the statement"""
    item = item_info ['item_usable'].title()
    discription = item_info ['item_discription']
    print(f"You just got a {item}!")
    print(f"{discription}!")
    print("\n")
    
#print out the locations into a statement
print("Locations:")
for location, location_info in locations.items():
    """define the locations and their discription and prints out the statement"""
    location = location_info ['location']
    discription = location_info ['location_discription']
    print(f"You arrived at {location}!")
    print(f"{discription}!")
    print("\n")
    