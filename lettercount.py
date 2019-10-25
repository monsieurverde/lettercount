import string

def lettercount(test):

    sentence = test.lower()   # convert to all lowercase

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    letter_count = {} # empty dictionary
    for char in sentence:
        if char in alphabet: # ignore any punctuation, numbers, etc
            if char in letter_count:
                letter_count[char] = letter_count[char] + 1
            else:
                letter_count[char] = 1
        else:
            pass

    keys = letter_count.keys()
    keys.sort()
    print(letter_count)

def main():

    test = "hello world"
    lettercount(test)

if __name__ == '__main__':
    main()