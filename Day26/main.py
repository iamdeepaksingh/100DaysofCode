# Author: Deepak Kumar Singh
# Description: Dictionary comprehension, pandas iterrows
# Date Created: 21/01/2022
# Date Modified: 23/1/2022

import pandas
new_dict = {}
df = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter:row.code for (index, row) in df.iterrows()}
phonetic_list = []


def generate_phonetic():
    inp = str(input("Enter a word : ")).upper()

    try:
        phonetic_list = [new_dict[i] for i in inp]
    except KeyError as error_msg:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()

