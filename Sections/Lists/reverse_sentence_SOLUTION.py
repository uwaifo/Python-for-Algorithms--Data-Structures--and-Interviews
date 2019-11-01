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
    word = []
    length = len(s)
    spaces = [' ']

    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i = i + 1
            
            word.append(s[word_start:i])
        i = i + 1
    return ' '.join(reversed(word))


print(rev_word('Hi John,   are you ready to go?'))# 'go? to ready you are John, Hi'
#rev_word('    space before') #'before space'