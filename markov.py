import random 


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    #Turning all lines in file into one string

    return contents


def make_chains(contents):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi'): ['there']}
    """
    #Opening an empty dictionary
    chains = {}
    
    #Split content string at all white spaces (including line breaks)    
    words = contents.split()
   
    #For each index (i)
    #Creates a list of the indices for the number of word in words - 2
    for i in range(len(words) - 2):
        #In order to bind word_keys to the first two words in every possible position (index). 
        #This creates our keys
        word_keys = (words[i], words[i + 1])
        #Same as above, only binds chosen_word to third word to create our values
        chosen_word = words[i + 2]
        
        #CODE BELOW HANGED AFTER CODE REVIEW
        #Bind word_keys_value to the list of values associated with this key if this key exists.
        #If the key doesn't exist, return an empty list
        # word_key_values = chains.get(word_keys, []) 
        #Add chosen word to list of word_key_values
        # word_key_values.append(chosen_word)
        #Assembles dictionary.
        # chains[word_keys] = word_key_values

        #checking for existence
        if word_keys not in chains:
            chains[word_keys] = []
        #Assembles dictionary
        chains[word_keys].append(chosen_word)
    
    #Line below was used to test number of keys in dictionary     
    #print len(chains)
    
    return chains



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    
    #Make a random choice of key from within a list of keys from the chains dictionary
    key = random.choice(chains.keys())
    text = ' '.join(key)

    #Creating a loop that will continue to iterate until the length of output is > 250 characters
    while len(text) < 1000:
        #Gets the values associated with the current key
        values = chains.get(key)
        #Because we have elements that have the value of None, but must have way to break out
        if values == None:
            break
        #Makes a random choice of value from within the set of values associate with the current key
        random_chosen_value = random.choice(values)
        #Adds additional text to existing text 
        text = text + ' ' + random_chosen_value
        #Create a new key using the second word in the current key and the current value
        key = key[1], random_chosen_value
    
    #for word_keys, word_key_values in chains.items():

    #Make a loop but make sure it is not an infinite loop
    return text


# input_path = "green-eggs.txt"
input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)



# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
