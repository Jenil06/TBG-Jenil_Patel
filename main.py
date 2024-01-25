#TBG-Jenil_Patel
#Jan. 25, 2024
#This code creates a fun and interactive text-based game.
#Where you get to pcik who you play ad.
#Explore the haunted house to find your way out and some easter eggs.
#Enjoy



from map import *
from character import *
from inventory import *
import cmd
import os
import textwrap
import sys


living_room = Map(5, 5)

living_room.tiles[0][0] = 'D'
living_room.tiles[4][4] = 'R'
living_room.tiles[2][2] = 'b'
living_room.tiles[2][4] = 'k'
living_room.tiles[0][4] = 'B'
living_room.tiles[4][0] = 'K'
living_room.tiles[1][3] = 'W'
living_room.tiles[1][1] = 'f'


#Title Screen
def ts_option():
    option = input(' ')
    if option.lower() == ('play'):
        setup_game()
    elif option.lower() == ('help'):
        help_screen()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print('Try again')
        option = input(' ')
        if option.lower() == ('play'):
            setup_game()
        elif option.lower() == ('help'):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()
            
def ts():
    print('---------------')
    print('-Haunted House-')
    print('-             -')
    print('-     Play    -')
    print('-     Help    -')
    print('-     Quit    -')
    print('-             -')
    print('---------------')
    ts_option()
    
def help_screen():
    print('---------------')
    print('-Haunted House-')
    print('-             -')
    print('-             -')
    print('-             -')
    print('-             -')
    print('-             -')
    print('------Map------')
    print(living_room.print_map(0))
    ts()


def tile_option():
    print('What would you like to do?')
    action = input(' ')
    action_options = ['move', 'interact', 'quit', 'inventory']
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() == 'move':
        hero_move()
    elif action.lower() == 'interact':
        hero_interact()
    while action.lower() not in action_options:
        print('unkown action, try again')
        action = input(' ')
        if action.lower() == 'quit':
            sys.exit()
        elif action.lower() == 'move':
            hero_move()
        elif action.lower() == 'interact':
            hero_interact()

def hero_move():
    move = input("Enter direction (W/A/S/D): ").upper()
    
    #movement
    if move == 'W' and hero.position[0] > 0:
        hero.position = (hero.position[0] - 1, hero.position[1])
    elif move == 'A' and hero.position[1] > 0:
        hero.position = (hero.position[0], hero.position[1] - 1)
    elif move == 'S' and hero.position[0] < living_room.height - 1:
        hero.position = (hero.position[0] + 1, hero.position[1])
    elif move == 'D' and hero.position[1] < living_room.width - 1:
        hero.position = (hero.position[0], hero.position[1] + 1)
    living_room.print_map(hero.position)
    
    #tile test and what to do if tile match
    current_tile = living_room.tiles[hero.position[0]][hero.position[1]]
    if current_tile == 'D':
        print("You are at the main door.Would you like to leave?(y/n)")
        choice4 = input('')
        if choice4.lower() == 'y':
            print('goodbye')
            print('you thought')
            print('you will never leave')
            return
        elif choice4.lower() == 'n':
            return
    elif current_tile == 'R':
        print("You are on the Room tile. Would you like to enter?(y/n)")
        choice = input('')
        if choice.lower() == 'y':
            print('You see an old photo. Would you like to look at it?(y/n)')
            choice2 = input('')
            if choice2.lower() == 'y':
                print('it a family photo of the old owners')
            elif choice2.lower() == 'n':
                return 
        elif choice.lower() == 'n':
            return 
    elif current_tile == 'b':
        bat = Inventory(name="Baseball Bat", damage=15)
        print("You have a baseball bat that does 15 damage.")
        choice3 = input('Would you like to pick up the baseball bat?(y/n)')
        if choice3.lower() == 'y':
            hero.inventory = bat
            living_room.tiles[2][2] = 'O'
            return
        elif choice3.lower() == 'n':
            return
    elif current_tile == 'k':
        key = Inventory(name="Basement Key", damage=5)
        print("You have a basement key which might help you leave this place.")
        choice5 = input('Would you like to pick up the key?(y/n)')
        if choice5.lower() == 'y':
            hero.inventory = key
            living_room.tiles[2][4] = 'O'
            return
        elif choice5.lower() == 'n':
            return
    elif current_tile == 'B':
        print('The door to the basement is locked, Do you have the key?(y/n)')
        choice6 = input('')
        if choice6.lower() == 'y':
            if living_room.tiles[2][4] == 'O':
                print('there was an exit in the basement, do you want to leave?(y/n)')
                choice7 = input('')
                if choice7.lower() == 'y':
                    print('thanks for playing have a great day!!!')
                    sys.exit()
                elif choice7.lower() == 'n':
                    print('keep exploring')
                    return
            elif living_room.tiles[2][4] != 'O':
                print("Your house key doesn't count, keep looking")
                return
        elif choice6.lower() == 'n':
            print('keep looking around')
            return
                
    elif current_tile == 'K':
        print('Would you like to enter the kitchen?(y/n)')
        choice8 = input('')
        if choice8.lower() == 'y':
            print('You have entered the kitchen. You spot a recipe book, would you like to keep it?(y/n)')
            choice9 = input('')
            if choice9.lower() == 'y':
                print('On the back of it there is a statment writen from blood')
                print('Find the key, it is you only way out. FIND IT NOW')
                return
            elif choice9.lower() == 'n':
                print('You hear a sound from the fridge. Do you dare go look at it')
                choice10 = input('')
                if choice10.lower() == 'y':
                    print('You got pulled into the fridege, you tried your best not to be sucked in, now you are traped in the fridge for ever')
                    print('You lost, goodbye')
                    sys.exit()
                elif choice10.lower() == 'n':
                    return
            return
        
        elif choice8.loer() == 'n':
            return
    elif current_tile == 'W':
        print('Would you like to enter the washroom?(y/n)')
        choice11 = input('')
        if choice11.lower() == 'y':
            print('Theres nothing here')
            return
        elif choice11.lower() == 'n':
            print('You here a voice call you from the wash room do you want to enter?(y/n)')
            choice12 = input('')
            if choice12.lower() == 'y':
                print('You find some on the wall')
                if living_room.tiles[1][1] == 'O':
                    print('You use your flashlight and find something writen on the wall')
                    print('Why did the bathroom ghost become a plumber?')
                    answer = input('')
                    print('Because he was great at dealing with spooky leaks and eerie clogs!')
                elif living_room.tiles[1][1] != 'O':
                    print('Go look for the flashlight it is worth it')
            elif choice12.lower() == 'n':
                return
        return
    
    elif current_tile == 'f':
        flashlight = Inventory(name="Flashlight", damage=10)
        print("Might be needed to look at someting in the washroom.")
        choice13 = input('Would you like to pick up the flashlight?(y/n)')
        if choice13.lower() == 'y':
            hero.inventory = flashlight
            living_room.tiles[1][1] = 'O'
            return
        elif choice13.lower() == 'n':
            return
    elif current_tile == 'O':
        return

def main_game_loop():
    while hero.game_over == False:
        tile_option()
        
def setup_game():
    #Player options
    for player, player_info in players.items(): 
        print(f"\n{player}:")
        hp = player_info['Health Points']    #store thire health points
        print(f"{player} has {hp} health points.")
        dam = player_info['Damage']
        print(f"{player} does {dam} damage.")
    #character select
    sel_player = input("What character do you want to be?: ")
    if sel_player.title() in ['Peter', 'Miles', 'Gwen', 'Miguel']:
        player_info = players[sel_player.title()]
        
        # Extract individual variables
        name = sel_player.title()
        health_points = player_info['Health Points']
        damage = player_info['Damage']
        
    while sel_player.title() not in ['Peter', 'Miles', 'Gwen', 'Miguel']:
        print(f'{sel_player} is not a character.')
        sel_player = input('')
        if sel_player.title() in ['Peter', 'Miles', 'Gwen', 'Miguel']:
            player_info = players[sel_player.title()]
            
            # Extract individual variables
            name = sel_player.title()
            health_points = player_info['Health Points']
            damage = player_info['Damage']
            
    global hero
    hero = hero(name,health_points,damage)
    
    print(f'You have slected {name}, who has {health_points} health, and does {damage} damage.')
    main_game_loop()

ts()
    
