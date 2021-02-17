vowels = "euioa"

def num_of_vowels(user_input):
    vowels_in_word = [letter for letter in user_input if letter in vowels]
    if len(vowels_in_word) == 0 and "y" in user_input:
        vowels_in_word = [letter for letter in user_input if letter == "y"]
    return len(vowels_in_word)

def num_of_consonants(user_input):
    consonants_in_word = [letter for letter in user_input if letter not in vowels]
    vowels_in_word = [letter for letter in user_input if letter in vowels]
    if len(vowels_in_word) == 0 and "y" in user_input:
        vowels_in_word = [letter for letter in user_input if letter == "y"]
        return len(consonants_in_word) - len(vowels_in_word)
    else:
        return len(consonants_in_word)



user_word = input("Enter a string: ").lower()

user_words_vowels = num_of_vowels(user_word)
user_words_cons = num_of_consonants(user_word)

print(f"The string you entered includes {user_words_vowels} vowels and {user_words_cons} consonants")


