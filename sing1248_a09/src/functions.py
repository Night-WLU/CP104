"""
-------------------------------------------------------
[Functions for Assignment 9]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""


def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    counter = 0
    data = ""
    line = file_handle.readline()
    while counter < count:
        data += f"{line.strip()}"
        line = file_handle.readline()
        data += "\n"
        counter += 1
    print(data)
    return None


def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []
    line = file_handle.readline()
    while line != '':
        separator = line.split(',')
        for i in range(len(separator)):
            num = separator[i]
            if num.strip().isdigit():
                num = int(num)
                number_list.append(num)
        line = file_handle.readline()
    return number_list


def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = 0
    content = file_handle.read()
    for i in content:
        if i.isupper():
            ucount += 1
        elif i.islower():
            lcount += 1
        elif i.isdigit():
            dcount += 1
        elif i.isspace():
            wcount += 1
        else:
            rcount += 1
    return ucount, lcount, dcount, wcount, rcount


def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    count = 0
    line = fh_read.readline()
    while line != "":
        fh_write.write(f"[{count}] {line}")
        line = fh_read.readline()
        count += 1
    return None


def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    # look at the first line of the file and assign the base values based on that line
    temp_line = file_handle.readline()
    temp_lowest = temp_line.strip().split(',')
    lowest_mark = float(temp_lowest[3])
    tot = lowest_mark
    count = 1
    l_id = temp_lowest[2]
    h_id = temp_lowest[2]
    highest_mark = 0
    # go through all other lines in file and compare to the first for first iteration
    for line in file_handle:
        content = line.strip().split(',')
        student_id = content[2]
        grade = float(content[3])
        tot += grade
        count += 1
        if grade < lowest_mark:
            lowest_mark = grade
            l_id = student_id
        if grade > highest_mark:
            highest_mark = grade
            h_id = student_id
    avg = tot / count
    l_id = str(l_id)
    h_id = str(h_id)
    return l_id, h_id, avg
