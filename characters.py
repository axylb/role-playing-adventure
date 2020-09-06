import random, sys

def roll():
        return random.randint(1, 20)

class character:
    def __init__(self,name,age,home,intel,char,agil,stre,luck,type, life, batt):
        self.name = name
        self.age = age
        self.home = home
        self.intel = intel
        self.char = char
        self.agil = agil
        self.stre = stre
        self.luck = luck
        self.type = type
        self.life = life
        self.batt = batt

def translate(word):
    lordex = 0
    lord = ""
    for letter in word:
        if random.randint(1,5) > 3:
            if letter.lower() in "aiu":
                letter = "o"
                lord += letter
            elif letter.lower() in "eoy":
                letter = "i"
                lord += letter
            elif letter.lower() in "h":
                letter = "u"
                lord += letter
            elif letter.lower() in "spt":
                letter = "z"
                lord += letter
            elif letter.lower() in "mlt":
                letter = "n"
                lord += letter
            elif letter.lower() in "djz":
                letter = "ch"
                lord += letter
            elif letter.lower() in "nv":
                letter = "m"
                lord += letter
        else:
            lord += letter
        # print(letter)
    return lord

def fight(good, bad):
    atk = good.stre+random.randint(-3,7)
    if atk < 0:
        atk = 0
    bad.life = bad.life - atk
    if bad.life < 1:
        print("\nYou caused " + str(atk) + " damage...\n" + bad.name + " has been destroyed.\n")
        return "break"
    else:
        print("\nYour attack did " + str(atk) + " damage.")
        print(bad.name + " is still alive with " + str(bad.life) +
              " life points remaining.")
        atk = bad.stre + random.randint(-3, 5)
        if atk < 0:
            atk = 0
        good.life = good.life - atk
        if good.life > 0:
            print("\n" + bad.name + " attacked you and caused " + str(atk) + " damage...\nYou have " + str(good.life) + " remaining.\n")
        else:
            print("\n" + bad.name + " attacked you with " + str(atk) + " damage...\nYou died.\n\n")
            sys.exit()

def stats(npc):
    return ("name:  " + npc.name + "\nhome town:  " + npc.home + "\nage:  " + str(npc.age) + "\ntype:  " + str(npc.type) +
      "\n\nintelligence:  " + str(npc.intel) + "\ncharisma:  " + str(npc.char) +
      "\nagillity:  " + str(npc.agil) + "\nstrength:  " + str(npc.stre) +
      "\nLife points:  " + str(npc.life) + "\n")

def action(hero,npc):
    choice = input("what do you want to do:  ").lower()
    if "fight" in choice:
        hero.batt = True
        if fight(hero, npc) == "break":
            return "break"
        hero.batt = True
    elif "leave" in choice:
        if hero.batt == True:
            if roll() + hero.luck > npc.life:
                print("You've succesfully escaped.")
                return "break"
            else:
                print("\nYou can't do that now.")
                atk = npc.stre + random.randint(-3, 5)
                if atk < 0:
                    atk = 0
                hero.life = hero.life - atk
                if hero.life > 0:
                    print(npc.name + " attacked you and caused " + str(atk) + " damage...\nYou have " + str(
                        hero.life) + " remaining.\n")
                else:
                    print(npc.name + " attacked you with " + str(atk) + " damage...\nYou died.")
                    return "break"
                    sys.exit()
        else:
            print("You walk away")
            return "break"
    elif "stat" in choice:
        print(stats(npc))
    elif "talk" in choice:
        if hero.batt == False:
            if hero.char >= npc.char:
                if npc.talked == False:
                    talk_list = open("/Users/Axyl Brosseau/PycharmProjects/role playing adventure/" + npc.type + "_dialogue", "r")
                    speech = "My name is, " + npc.name.title() + ".  " + random.choice(list(talk_list)).lower().capitalize().replace("\n", "")
                    talk_list.close()
                    print(npc.name + " says, \"" + speech + "\"")
                    npc.talked = True
                else:
                    talk_list = open( "/Users/Axyl Brosseau/PycharmProjects/role playing adventure/" + npc.type + "_dialogue", "r")
                    speech = random.choice(list(talk_list)).lower().capitalize().replace("\n", "")
                    talk_list.close()
                    print(npc.name + " says, \"" + speech + "\"")
            else:
                talk_list = open("/Users/Axyl Brosseau/PycharmProjects/role playing adventure/" + npc.type + "_bad_dialogue", "r")
                speech = random.choice(list(talk_list)).lower().capitalize().replace("\n", "")
                talk_list.close()
                print(npc.name + " says, \"" + speech + "\"")
        else:
            print("It's too late for words!")

def enemy():

    name_list = open("/Users/Axyl Brosseau/PycharmProjects/role playing adventure/names", "r")
    name = translate(random.choice(list(name_list))).lower().title()
    name_list.close()

    if random.randint(1,35) == 1:
        age = random.randint(3,200)
    elif random.randint(1,12) == 1:
        age = random.randint(6,105)
    else:
        age = random.randint(10,65)

    skillpts = 20
    try:
        if random.randint(0,15) < 6:
            intel = random.randint(0, 12)
            skillpts = skillpts - intel
            char = random.randint(0, 7)
            skillpts = skillpts - char
            agil = random.randint(0, 5)
            skillpts = skillpts - agil
            stre = random.randint(0, skillpts)
            skillpts = skillpts - stre
            luck = skillpts
        elif random.randint(0,15) > 9:
            intel = random.randint(0, 5)
            skillpts = skillpts - intel
            char = random.randint(0, 6)
            skillpts = skillpts - char
            agil = random.randint(0, 7)
            skillpts = skillpts - agil
            stre = random.randint(0, skillpts)
            skillpts = skillpts - stre
            luck = skillpts
        else:
            intel = random.randint(2, 6)
            skillpts = skillpts - intel
            char = random.randint(2, 6)
            skillpts = skillpts - char
            agil = random.randint(2, 6)
            skillpts = skillpts - agil
            stre = random.randint(0, skillpts)
            skillpts = skillpts - stre
            luck = skillpts
    except:
        intel = random.randint(3, 7)
        char = random.randint(2, 6)
        agil = random.randint(2, 7)
        stre = random.randint(2, 8)
        luck = random.randint(2, 8)
    type_try = random.randint(1, 7)
    if type_try == 1:
        type = "wizard"
        intel += 4
        luck += 2
        life = 20+stre+(luck%4)
    elif type_try == 2:
        type = "thief"
        agil += 3
        luck += 2
        life = 17+stre+(luck%4)
    elif type_try == 3:
        type = "warrior"
        stre += 2
        char += 2
        life = 23+stre+(luck%4)
    elif type_try == 4:
        type = "orc"
        stre += 5
        life = 25+stre+(luck%4)
    else:
        type = "villager"
        stre = stre%4
        life = 5+stre+(luck%4)


    town_list = open("/Users/Axyl Brosseau/PycharmProjects/role playing adventure/towns", "r")
    town = translate(random.choice(list(town_list))).lower().title()
    town_list.close()

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
    talked = False
    new_bad = [name, age, town, intel, char, agil, stre, luck, type, life, talked]
    return new_bad