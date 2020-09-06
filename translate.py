def translate(lord)
    lordex = 0

    for letter in name:
        if letter.lower() in "aiu":
            letter = "o"
            lord += letter
        elif letter.lower() in "oy":
            letter = "i"
            lord += letter
        elif letter.lower() in "h":
            letter = "u"
            lord += letter
        elif letter.lower() in "dspj":
            letter = "z"
            lord += letter
        elif letter.lower() in "ml":
            letter = "n"
            lord += letter
        elif letter.lower() in "t":
            letter = "ch"
            lord += letter
        elif letter.lower() in "nv":
            letter = "m"
            lord += letter
        else:
            lord += letter
        #print(letter)
    return lord
