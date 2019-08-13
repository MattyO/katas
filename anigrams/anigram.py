import functools
import itertools
import collections

s = set(map(lambda w: w.replace("\n", ''), open("wordlist.txt", encoding='utf-8', errors='surrogateescape').readlines()))

def perms(word):
    return map(lambda x: ''.join(x), itertools.permutations(list(word)))

def real_words(ps):
    return set(filter(lambda word: word in s, ps))

def count_anitgram():
    return map(lambda kv: kv[1], functools.reduce(lambda memo, x: [memo[tuple(sorted(dict(collections.Counter(list(x))).items()))].append(x), memo][1], s, collections.defaultdict(list)).items())

def anigram():
    s2 = ['vang', 'BSDs',  'prizewoman',  'unessence', 'lenitives', 'pawnor', 'alible', 'chameleons', 'clotted', 'spiders', 'bazooms', 'wombats', 'Nampa', 'sperrylite', 'trawling', 'comically', 'labile']
    s3 = ['labile', 'vang']
    return functools.reduce(lambda memo, word: memo +  list(real_words(perms(word)) - set(memo)) + [None], s, list())


def hash_anigram():
    pass
