# Author: Deepak Kumar Singh
# Description: Reading and writing to file using Python.
# Date Created: 14/01/2022
# Date Modified: 14/01/2022


with open("./Input/Names/invited_names.txt", "r") as f:
    invitee = f.readlines()

with open("./Input/Letters/starting_letter.txt", 'r') as f:
    content = f.read()

for each in invitee:
    nam = each.strip()
    new_ltr = content.replace("[name]", nam)
    with open(f"./Output/ReadyToSend/leter_for_{nam}", "w") as f:
        f.write(new_ltr)




