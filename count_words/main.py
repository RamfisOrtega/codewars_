import re

"""
Code challenge developed following TDD technique
"""


def disregarding_forbidden_words(list_of_words):
    forbidden = ['a', 'the', 'on', 'at', 'of', 'in', "upon", 'as']
    if any(ele in list_of_words for ele in forbidden):
        for w in forbidden:
            while w in list_of_words: list_of_words.remove(w)
    return list_of_words


def disregarding_no_alphabetic_characters(bag_of_words):
    sentence = re.sub('[^a-zA-Z]', ' ', bag_of_words)
    return sentence.strip()


def splitWordBySpace(bag_of_words):
    words = disregarding_no_alphabetic_characters(bag_of_words).split()
    return words


def exclude_words(list_of_words):
    return disregarding_forbidden_words(list_of_words)



# DESIRED function
def word_count(s):
    # count words, which s contains
    list_of_words = splitWordBySpace(s.lower())
    return len(exclude_words(list_of_words))


"""
Code challenge developed with list comprehension 
"""


def word_count_efficient(s):
    words = re.sub('[^a-zA-Z]', ' ', s).strip().split()
    forbidden_words = ['a', 'the', 'on', 'at', 'of', 'in', "upon", 'as']
    words = [word for word in words if word.lower() not in forbidden_words]
    return len(words)

if __name__ == '__main__':
    word_count('PyCharm')


