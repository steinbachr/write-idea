from bs4 import BeautifulSoup
import csv
import random
import requests
import ipdb


#in the future, we can have this passed in to the program from command line
MAX_TO_CHOOSE = 3

def get_random_words(max_to_choose):
    """
    get one or more random words from the dictionary
    :return: list of words of at most size max_to_choose as chosen from the dictionary
    """
    all_words = []
    with open('dictionary.csv', 'rb') as dictionary:
        for word in dictionary:
            all_words.append(word.strip().replace("\n", ""))

    to_choose = random.randint(1, max_to_choose)
    return random.sample(all_words, to_choose)


def get_definition_from_merriam(word):
    """
    for the given word, get its definition from merriam webster
    :param word: str the word to get the definition for
    :return: str the definition of the word
    """
    api_key = 'c2b1a784-7bd2-4efe-b2c9-b328ce42ed4e'
    api_url = 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/{word}?key={key}'.format(word=word, key=api_key)
    resp = requests.get(api_url)

    try:
        soup = BeautifulSoup(resp.content)
        return soup.dt
    except Exception:
        return None


print "\n\nWords Of The Day:"
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>"
for word in get_random_words(MAX_TO_CHOOSE):
    definition = get_definition_from_merriam(word)
    if definition:
        print "{word}: {defn}\n".format(word=word, defn=definition)
