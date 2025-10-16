"""
find_most_frequent.py

Author: Liam Mills
Created: 2025-10-16
Last Modified: 2025-10-16

Implements functions that find the most frequent words from arrays based on various criteria, and
other functions to support them.

Functions:
    - findMostFrequentWord(inputList1: list[str], inputList2: list[str]) -> str: Returns a string of the most
    frequent word in inputList1 that does not appear in inputList2.
    - findMostFrequentFollower(inputList: list[str], targetWord: str) -> str: Returns a string of the most
    frequent following word of the targetWord, based on the inputList of strings.
    - findMaxValueFromDictionaryOfNumbers(dictionary: dict, target: str = "first") -> str: Returns a string of
    the key of the item in a dictionary with the highest value.
"""

def findMostFrequentWord(inputList1: list[str], inputList2: list[str]) -> str:
    """
    Function to find the most frequent word in an array, which was the result
    of subtracting the overlapping elements from array inputList2 from 
    array inputList1

    Args:
        - inputList1 (list of strings): List of strings.
        - inputList2 (list of strings): List of strings.

    Returns:
        - string: The word with the highest frequency count, or if
        an error occurs, the string of "-1" is returned. If there are
        multiple words with the same count, then the first word with
        that count will be returned.

    Side Effects:
        - Prints error messages to the console.
    """

    # if input arrays don't contain values, return error code
    if len(inputList1) == 0 or len(inputList2) == 0:
        print("Err: one or more of the parameters were empty.")
        return "-1"

    # create dicionary for count of each string
    string_count = {}

    # create a list by subtracking all items of inputList2 from inputList1
    subtracted_arr = [item for item in inputList1 if item not in inputList2]

    # if dictionary size is zero, return error code
    if len(subtracted_arr) == 0:
        print("Err: the resulting array was empty, inputList1 did not contain any differentiating strings.")
        return "-1"

    # loop the subtracted array to add count per word
    for str in subtracted_arr:
        if str in string_count:
            string_count[str] += 1
        else:
            string_count[str] = 1

    # if dictionary size is zero, return error code
    if len(string_count.keys()) == 0:
        print("Err: the resulting dictionary was empty.")
        return "-1"

    # find largest value in dictionary & return its key
    # or return the first if there are tying words
    return findMaxValueFromDictionaryOfNumbers(string_count)

def findMostFrequentFollower(inputList: list[str], targetWord: str) -> str:
    """
    Function to find the most frequent word in an array that follows
    a target word

    Args:
        - inputList1 (list of strings): List of strings.
        - targetWord (string): String used as the target word of the function.

    Returns:
        - string: The word with the highest frequency count, or if
        an error occurs, the string of "-1" is returned. If there are
        multiple words with the same count, then the last word with
        that count will be returned.

    Side Effects:
        - Prints error messages to the console.
    """

    # if input arrays don't contain values, return error code
    if len(inputList) == 0 or len(targetWord) == 0:
        print("Err: one or more of the parameters were empty.")
        return "-1" 

    # create dicionary for count of each string
    string_count = {}

    # loop indexes of the inputList array
    for index in range(0, len(inputList)):
        # if index + 1 doesn't overflow the container and current word
        # at index in inputList equals the target word
        if index + 1 != len(inputList) and inputList[index].lower() == targetWord.lower():
            # set the next work to a variable
            str = inputList[index + 1].lower()

            # up the count of the word in the string_count dictionary
            if str in string_count:
                string_count[str] += 1
            else:
                string_count[str] = 1

    # find largest value in dictionary & return its key
    # or return the last word if there are tying words
    return findMaxValueFromDictionaryOfNumbers(string_count, "last")

def findMaxValueFromDictionaryOfNumbers(dictionary: dict, target: str = "first") -> str:
    """
    Function to find the key of the item in a dictionary with the highest
    value. If multiple items have the same value, then the target will
    output the first or last element with that value.

    Args:
        - dictionary (dictionary): Dictionary with string keys and int values.
        target (string): String with the value of first or last, to
        target the output position.

    Returns:
        - string: The key of the item with the highest value, or if
        an error occurs, the string of "-1" is returned. 

    Side Effects:
        - Prints error messages to the console.
    """

    # if dictionary size is zero, return error code
    if len(dictionary.keys()) == 0:
        print("Err: the resulting dictionary was empty.")
        return "-1"
    
    # make sure target only targets first or last element
    if target not in ["first", "last"]:
        target = "first"
    
    # get max value in variable
    max_value = dictionary[max(dictionary, key=dictionary.get)]

    # create a list by subtracking all items of inputList2 from inputList1
    array_of_max_values = [key for key, value in dictionary.items() if value == max_value]

    return array_of_max_values[0 if target == "first" else -1]



# print(findMostFrequentWord(['test', 'b', 'test', 'three', 'four', 'fivef', 'b', 'fivef', 'fivef', 'bc'], ['three', 'four', 'fivef']))

# arr = ["This", "is", "the", "way", ".", "The", "way", "is", "shut", ".", "The", "door", "is", "the", "end", "."]
# print(findMostFrequentFollower(arr, "the"))
# print(findMostFrequentFollower(arr, "is"))
# print(findMostFrequentFollower(arr, "door"))