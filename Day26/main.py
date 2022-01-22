# Author: Deepak Kumar Singh
# Description: Dictionary comprehension, pandas iterrows
# Date Created: 21/01/2022
# Date Modified: 21/1/2022

import pandas
new_dict = {}
df = pandas.read_csv("nato_phonetic_alphabet.csv")


#Loop through rows of a data frame
# for (index, row) in df.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     #new_dict = {row.letter, row.code}
#     new_dict[row.letter] = row.code

new_dict = {row.letter:row.code for (index, row) in df.iterrows()}


#print(new_dict)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


inp = str(input("Enter a word : ")).upper()
phonetic_list = []
#for i in inp:
#    phonetic_list.append(new_dict.get(i))
#print(phonetic_list)

print([new_dict.get(i) for i in inp])

