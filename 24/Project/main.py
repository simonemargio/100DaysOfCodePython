"""
Project: Mail Merge
Create a letter using starting_letter.txt
for each name in invited_names.txt
Replace the [name] placeholder with the actual name.
Save the letters in the folder "ReadyToSend".
"""

file_letter = open("Input/Letters/starting_letter.txt", mode="r")
file_names = open("Input/Names/invited_names.txt", mode="r")

letter = file_letter.read()

for line in file_names:
    new_name = line.strip()
    new_letter = letter.replace("[name]", new_name)
    file_new_letter = open(f"Output/ReadyToSend/letter_for_{new_name}.txt", mode="w")
    file_new_letter.write(new_letter)
    file_new_letter.close()
    if 'str' in line:
        break

file_letter.close()
file_names.close()










