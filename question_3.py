def swap_pair(user_input):
    new_word = ""
    last_letter = ""
    list_word_char = [letter for letter in user_input]
    odd_char = [letter for letter in list_word_char[:-1:2]] #List comprehension does the same thing a a for loop but better. Example of a fore loop below
    # odd_char = []
    # for letter in user_input[:-1:2]:
    #   odd_char.append(letter)
    even_char = [letter for letter in list_word_char[1::2]]
    if len(user_input) % 2 == 1: #Checks to see if the the user word length is odd
        last_letter = list_word_char[-1]
        odd_char = [letter for letter in list_word_char[:-1:2]]

    for n in range(len(user_input)//2):
        new_word += f"{even_char[n]}{odd_char[n]}"
    new_word += last_letter
    return new_word

user_word = input("Enter a word: ")

print(swap_pair(user_word))
