import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_word():
    user_word = input("Enter the word: ").upper()
    try:
        user_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, Only letters in the alphabet please!!")
        generate_word()
    else:
        print(user_list)


generate_word()
