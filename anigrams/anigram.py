import functools
import itertools

s = set(map(lambda w: w.replace("\n", ''), open("wordlist.txt", encoding='utf-8', errors='surrogateescape').readlines()))

def perms(word):
    return map(lambda x: ''.join(x), itertools.permutations(list(word)))

def real_words(ps):
    return set(filter(lambda word: word in s, ps))


#filter(lambda y: y  in s, set(map(lambda x: ''.join(x), itertools.permutations(list('clotted')))))

def anigram():
    s2 = ['vang', 'BSDs',  'prizewoman',  'unessence', 'lenitives', 'pawnor', 'alible', 'chameleons', 'clotted', 'spiders', 'bazooms', 'wombats', 'Nampa', 'sperrylite', 'trawling', 'comically', 'labile']
    s3 = ['labile', 'vang']
    return functools.reduce(lambda memo, word: memo +  list(real_words(perms(word)) - set(memo)) + [None], s, list())

