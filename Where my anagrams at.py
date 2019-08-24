# https://www.codewars.com/kata/where-my-anagrams-at/train/python
def anagrams(word, words=[]):
    word_length = len(word)
    letters = []
    matching_words = []
    for i in word:
        letters.append(i)
    for j in words:
        count = 0
        matching_letters = 0
        list_words = list(j)
        for a in letters:
            count += 1
            if a in list_words and word_length == len(j):
                matching_letters += 1
                list_words.remove(a)
                if matching_letters == word_length:
                    matching_words.append(j)
    return matching_words
    print(letters)


def anagrams2(word, words): return [item for item in words if sorted(item)==sorted(word)]


print(anagrams2('racer', ['crazer', 'carer', 'racer']))