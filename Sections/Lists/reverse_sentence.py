'''
Given a string of words, reverse all the words. For example:
Given:'This is the best'
Return:'best the is This'
As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
'  space here'  and 'space here      '
both become:
'here space'
'''
def rev_word(s):

    s = s.replace(' ', ',')
    #s = s.replace()
    print(s)
    store_words = set()
    temp_word_store = ''
    for letter in s:
        if letter != ',' and temp_word_store == '':
            temp_word_store = letter
        elif letter != ',' and temp_word_store != '':
            temp_word_store = temp_word_store + letter
        else:
            store_words.add(temp_word_store)
            temp_word_store = ''
            

    print(store_words)


rev_word('Hi John,   are you ready to go?')# 'go? to ready you are John, Hi'
#rev_word('    space before') #'before space'