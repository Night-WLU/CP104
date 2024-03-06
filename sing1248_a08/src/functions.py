"""
-------------------------------------------------------
[Functions for Assigment 8]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""


def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    spaced = ""
    for i in range(0, len(sentence), 1):
        if i == 0:
            spaced += sentence[i]
        elif sentence[i].isupper():
            spaced += " " + sentence[i].lower()
        else:
            spaced += sentence[i]
    return spaced


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    pluralized = ""
    for i in range(0, len(string)-1, 1):
        pluralized += string[i]
    length = len(string)-1
    if string[length] == 's' or (string[length] == 'h' and string[length-1] == 's') or (string[length] == 'h' and string[length-1] == 'c'):
        pluralized = string + 'es'
    elif string[length] == 'y':
        if string[length-1] == 'a' or string[length-1] == 'o':
            pluralized = string + 's'
        else:
            pluralized += 'ies'
    else:
        pluralized = string + 's'
    return pluralized


def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    suffix = ''
    temp = ''
    length1 = len(str1)
    length2 = len(str2)
    count = 1
    i = 0
    while i < length1:
        if str1[(length1 - count)] in str2:
            if str1[(length1 - count)] == str2[(length2 - count)]:
                suffix += str1[(length1 - count)]
            count += 1
        i += 1
    count = 1
    i = 0
    while i < len(suffix):
        temp += suffix[len(suffix)-count]
        i += 1
        count += 1
    suffix = temp
    return suffix


def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    isbn_length = len(isbn)
    if isbn_length == 17:
        if isbn[16].isdigit():
            if isbn[15].isdigit() == False:
                if isbn.startswith('978') or isbn.startswith('979'):
                    if isbn.count('-') == 4:
                        if '--' in isbn:
                            is_valid = False
                        else:
                            is_valid = True
                    else:
                        is_valid = False
                else:
                    is_valid = False
            else:
                is_valid = False
        else:
            is_valid = False
    else:
        is_valid = False
    return is_valid


def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    i = 0
    while i < (len(words)-1):
        str1 = words[i]
        str2 = words[i+1]
        if str1[len(str1)-1].upper() == str2[0].upper():
            word_chain = True
        else:
            word_chain = False
            break
        i += 1
    return word_chain
