"""
-------------------------------------------------------
[Lab 10, Task 10]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
from functions import count_frequency_word
fh = open("words.txt", "r", encoding="utf-8")
word = input("Word to count: ")
count = count_frequency_word(fh, word)
print(f"word repeated {count} times")
