import pandas

program = True
nato_dict = {}
nato_alphabet_list = pandas.read_csv("nato_phonetic_alphabet.csv")

for (index, row) in nato_alphabet_list.iterrows():
    nato_dict[row.letter] = row.code

while program is True:
    try:
        user_word = input("Enter a word:").strip()
        nato_user_word = [nato_dict[letter.upper()] for letter in user_word]
        program = False
        print(nato_user_word)
    except KeyError:
        print("Sorry, only letters in the alphabet please!")