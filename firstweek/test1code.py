def alphabet_filter(word):
    # Write your code here

    vowel_list = ["a","e","i","o","u"]
    word_vowels = []
    word_consonants = []
    for char in word:
        if (vowel_list.count(char) > 0):
            word_vowels.append(char)
        else:
            word_consonants.append(char)



    return word_consonants, word_vowels



print(alphabet_filter("codecool"))