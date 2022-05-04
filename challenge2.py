# Challenge 2: Write a solution to find the character that has the highest number of occurences within a certain string, ignoring case. If there is more than one character with equal highest occurences, return the character that appeared first within the string.

def occurrences( certain_string ):

    # To make the function case-insensitive, we take the certain_string input and convert it to one case using either lower() or upper()

    string_insensitive = certain_string.lower()

    # Define a dictionary to keep characters in

    certain_dictionary = {}

    # Iterating through the positions in string_insensitive,

    for i in string_insensitive:

    # If the character is in the dictionary, the count in the dictionary is increased by 1

        if i in certain_dictionary:
            certain_dictionary[i] += 1

    # If the character is not in the dictionary, it is added to the dictionary with count 1

        else:
            certain_dictionary[i] = 1

    # Once the whole certain_string has been parsed, we evaluate the dictionary for the character with the highest occurrence

    result = max(certain_dictionary, key = certain_dictionary.get)

    # We print the character as output

    print (str(result))
    return

# QED
