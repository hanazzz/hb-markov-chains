"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)
    text = file.read()
    file.close()
    return text



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    words = text_string.split()

    
    
    for i in range(len(words)-2):
        if chains.get((words[i], words[i+1])) == None:
            chains[(words[i], words[i+1])] = [words[i+2]]
        else:
            chains[(words[i], words[i+1])].append(words[i+2])
        # (words[i], words[i+1]) 
        # create value-pairs for the dictionary chains
        # use .get method to check if key exists in dictionary
        # if it does not exist: create it
        # if it does exist: add to it
        # chains(words[i], words[i+1]) = [words[i+2]]
        # (would, you) = [could, could]
        # (you, could) = you

    return chains



def make_text(chains):
    """Return text from chains."""
    key_lst = list(chains.keys())
    

    # (word, word2)


    # SETTING UP INITIAL KEY-VALUE
    #when we're selecting the key list 
    #make sure we pick a key where the first word in that tuple is capitalized
    #if key[0][0]
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True: 
        current_key = choice(key_lst)
        first_letter = current_key[0][0]
        if first_letter in capital_letters:
            break

    current_value = choice(chains[current_key])
    words = [current_key[0], current_key[1], current_value]

    # CONTINUE BY ITERATING THROUGH CHAINS
    while True: 
        try:
            current_key = (current_key[1], current_value)
            current_value = choice(chains[current_key])
        except:
            break
        words.append(current_value)
        # try/except : if except then break out of loop
        # current_key = use the second word in the last key + the value as new key
        # random_value = choice(chains[random_key])
        # append random_value to words (list)

    return ' '.join(words)


# input_path = 'gettysburg.txt'
# input_path = sys.argv[1] 

# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1])

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
