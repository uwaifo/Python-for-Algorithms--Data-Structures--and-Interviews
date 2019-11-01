def uni_char2(s):
    characters = set()

    for letter in s:
        print(letter)
        #check if letter is in set , if not
        if letter in characters:
            return False
                #then add to set
        else:
            characters.add(letter)
    return True


print(uni_char2('goo'))#false
#print(uni_char2('abcdefg'))