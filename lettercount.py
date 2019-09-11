import string
def lettercount():
    
    x = input("Enter a sentence: ")

    y = x.lower()   # convert to all lowercase
    sentence = y.split()

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

    lettercount()

if __name__ == '__main__':
    main()