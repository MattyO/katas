import unittest
import anigram
from anigram import real_words, perms
import timeit


class FooTest(unittest.TestCase):

    #def test_slow_alg(self):
        #print(list(perms('labile')))
        #print(list(perms('labile'))[0] in anigram.s)
        #print(list(real_words(perms('labile'))))
        #print("after")
        #print(timeit.Timer('import anigram; print(anigram.anigram())', 'gc.enable()').timeit(1))


    def test_counter_group(self):
        print(anigram.count_anitgram())

