import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

df = pandas.DataFrame(data)
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(nato_dict)

user_input = input("Enter a word: ").upper()
code_word = [nato_dict[letter] for letter in user_input]
print(code_word)
