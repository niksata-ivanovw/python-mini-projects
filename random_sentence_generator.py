import random

def get_random_words(words):
    return random.choice(words)

names = ['Ivan', 'Nikola', 'Nikolay', 'Viktor', 'Mihal']
places = ['Varna', 'Sofia', 'Plovdiv', 'Chirpan', 'Burgas']
verbs = ['eats', 'smokes', 'watches', 'rides', 'hides']
nouns = ['cigarette', 'hamburger', 'cake', 'camppfire', 'bikes']
adverbs = ['slowly', 'carefully', 'fast', 'uncontrollably', 'miserably']
details = ['at school', 'after school', 'at home', 'near the sea', 'while being watched']


print('Hello, this is your first random sentence: \n')
while True:
    random_name = get_random_words(names)
    random_place = get_random_words(places)
    random_verb = get_random_words(verbs)
    random_noun = get_random_words(nouns)
    random_adverb = get_random_words(adverbs)
    random_detail = get_random_words(details)

    print(f'{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}.')
    if input('Press [Enter] to generate a new sentence or typpe [End] to end the program. \n') == 'End':
        break