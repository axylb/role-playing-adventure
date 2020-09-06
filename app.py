from characters import character, translate, enemy, fight, roll, stats, action
import random, sys

name = ""
age = 0
home = ""
name = str(input("\nWhat is your character name:  \n")).lower().title()
type = ""
x = 0
skillpoints = 20

while x == 0:
    try:
        age = int(input("What is your character's age:  \n"))
        if age <= 0:
            print("You are not that young!")
        elif age >= 100:
            print("Wow, a long lived life!")
            x+=1
            break
        else:
            x += 1
            break
    except:
        print("Invalid input")
x = 0
#age^^^


home = str(input("What is your character hometown:  \n")).lower().title()
print("Choose your stats.  You have 20 points to use.\n"
      "The stats are intelligence, charisma, agility, strength, and luck.")

while x == 0:
    try:
        intel = int(input("Intelligence:  \n"))
        if intel > skillpoints:
            print("Invalid... ")
        elif intel < 0:
            print("Invalid")
        else:
            skillpoints = skillpoints - intel
            break
    except:
        print("Invalid")
if skillpoints > 0:
    print("You have " + str(skillpoints) + " remaining")
else:
    print("You have no points left")
x = 0
#intelligence^^^

if skillpoints > 0:
    while x == 0:
        try:
            char = int(input("Charisma:  \n"))
            if char > skillpoints:
                print("Invalid... ")
            elif char < 0:
                print("Invalid")
            else:
                skillpoints = int(skillpoints - char)
                x += 1
                break
        except:
            print("Invalid")

    if skillpoints > 0:
        print("You have " + str(skillpoints) + " remaining")
    else:
        print("You have no points left")
    x = 0
else:
    char = 0
#charisma^^^

if skillpoints > 0:
    while x == 0:
        try:
            agil = int(input("Agility:  \n"))
            if agil > skillpoints:
                print("Invalid... ")
            elif agil < 0:
                print("Invalid")
            else:
                skillpoints = int(skillpoints - agil)
                x += 1
                break
        except:
            print("Invalid")

    if skillpoints > 0:
        print("You have " + str(skillpoints) + " remaining")
    else:
        print("You have no points left")
    x = 0
else:
    agil = 0
#agility^^^

if skillpoints > 0:
    while x == 0:
        try:
            stre = int(input("Strength:  \n"))
            if stre > skillpoints:
                print("Invalid... ")
            elif stre < 0:
                print("Invalid")
            else:
                skillpoints = int(skillpoints - stre)
                x += 1
                break
        except:
            print("Invalid")

    if skillpoints > 0:
        print("You have " + str(skillpoints) + " remaining")
    else:
        print("You have no points left")
    x = 0
else:
    stre = 0
#strength^^^

if skillpoints > 0:
    while x == 0:
        try:
            luck = int(input("Luck:  \n"))
            if luck > skillpoints:
                print("Invalid... ")
            elif luck < 0:
                print("Invalid")
            else:
                skillpoints = int(skillpoints - luck)
                x += 1
                break
        except:
            print("Invalid")

    if skillpoints > 0:
        print("You have " + str(skillpoints) + " remaining")
    else:
        print("You have no points left")
    x = 0
else:
    luck = 0
#luck^^^

while x==0:
    type = input("\nWizard (+3 int, +2 luck)\n"
                 "Thief (+3 agil, +2 luck)\n"
                 "Warrior (+2 str, +2 agil, +1 char)\n"
                 "Orc (+4 str, +1 luck)\n"
                 "Pick your type:  ").lower()
    if "zard" in type:
        type = "wizard"
        intel += 3
        luck += 2
        break
    elif "th" in type:
        type = "theif"
        agil += 3
        luck += 2
        break
    elif "war" in type:
        type = "warrior"
        stre += 2
        agil += 1
        char += 2
        break
    elif "orc" in type:
        type = "orc"
        stre += 4
        luck += 1
        break
    else:
        print("Invalid type")
if age < 26:
    agil += 3
elif age < 40:
    stre += 3
elif age < 50:
    char += 3
elif age < 70:
    intel += 3
else:
    luck += 3


life = 20 + stre + (luck%4)
hero = character(name, age, home, intel, char, agil, stre, luck, type, life, False)



print("\nSo you are the " + type + " " + str(hero.name).capitalize() + " from " + str(hero.home).capitalize() + ", and you are " + str(hero.age) + "?\n"
    "Your stats are as follows:\n")
print("Intelligence: " + str(hero.intel))
print("Charisma: " + str(hero.char))
print("Agility: " + str(hero.agil))
print("Strength: " + str(hero.stre))
print("Luck: " + str(hero.luck) + "\n")
print("\nLife points: " + str(hero.life) + "\n")

input("...")
z = 0
npc_name = ""
while z == 0:
    class npc1:
        stats = enemy()
        name = stats[0].replace("\n","")
        age = stats[1]
        home = stats[2].replace("\n","")
        intel = stats[3]
        char = stats[4]
        agil = stats[5]
        stre = stats[6]
        luck = stats[7]
        type = stats[8]
        life = stats[9]
        talked = stats[10]

    print("\n" + npc1.name.capitalize() + " from " + npc1.home.capitalize() + " approaches you:  ")
    while hero.life>0:
        if action(hero, npc1) == "break":
            hero.batt = False
            break

print("You've left the area")