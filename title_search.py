# Reference : https://data-panic.tistory.com/29

def find(word, char):
    # From the index just before the last index!
    for i in range(len(word) - 2, -1, -1):
        if word[i] == char:
            return len(word) - i - 1
    # If no character mathces, move along the length of the word
    return len(word)

def title_search(word, title):
    word_len = len(word)
    title_len = len(title)

    # Searching algorithm starts from here!
    i = 0
    while i <= title_len - word_len:
        j = word_len - 1 # Starts from the end index of word

        while j >= 0:
            if word[j] != title[i+j]:
                move = find(word, title[i+word_len-1])
                #print('Failed!')
                break
            j -= 1

        if j == -1: # Title found!
            #print('Title found')
            return True
        else: # Jump to next point!
            i += move

    return False # There's no news title corresponding to search word!

'''
# Test code
title = 'a pattern matching algorithm'
word = 'rithm'
print(title_search(word, title))
'''