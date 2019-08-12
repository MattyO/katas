def anigram(word):
    return filter(lambda y: y not in s, map(lambda x: ''.join(x), itertools.permutations(list(word))))
