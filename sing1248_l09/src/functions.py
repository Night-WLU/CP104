"""
-------------------------------------------------------
[Functions for Lab 9]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-15"
-------------------------------------------------------
"""


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:]
    return pc, pi, pq


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """
    category_return = False
    digits_return = False
    qualifier_return = False
    if product_code.isspace() or product_code == '':
        category_return = False
        digits_return = False
        qualifier_return = False
    else:
        counter = 0
        for _ in product_code:
            counter += 1
        if counter < 3:
            category_return = False
        else:
            category = product_code[0:3]
            if category == category.upper():
                category_return = True
            else:
                category_return = False
            digits = product_code[3:7]
            if digits.isdigit():
                if counter < 7:
                    digits_return = False
                else:
                    digits_return = True
            else:
                digits_return = False
            if counter > 7:
                qualifiers = product_code[7:]
                if qualifiers[0].isupper():
                    qualifier_return = True
                else:
                    qualifier_return = False
    return category_return, digits_return, qualifier_return


def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """
    counter = 0
    for _ in password:
        counter += 1
    if counter < 8:
        print('not long enough')
    if password.isdigit() == False:
        print("no digits")
    if password.lower() == password:
        print('no upper case')
    if password.upper() == password:
        print('no lower case')
    return None


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    txt_num = 0
    for i in txt:
        txt_num += 1
    for i in range(0, txt_num, 1):
        if txt[i].isalpha():
            if txt[i].isupper():
                uppr += 1
            else:
                lowr += 1
        if txt[i].isspace():
            whtspc += 1
        if txt[i].isdigit():
            dgts += 1
    return uppr, lowr, dgts, whtspc


def comma_period_replace(string):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    comma = ','
    period = '.'
    out = ""
    for c in string:
        if c == comma:
            c = period
        out += c
    return out
