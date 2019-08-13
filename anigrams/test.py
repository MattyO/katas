import unittest
import anigram
from anigram import real_words, perms
import timeit


class FooTest(unittest.TestCase):

    def test_bar(self):
        #print(list(perms('labile')))
        #print(list(perms('labile'))[0] in anigram.s)
        #print(list(real_words(perms('labile'))))
        #print("after")
        print(timeit.Timer('import anigram; print(anigram.anigram())', 'gc.enable()').timeit(1))
        
        self.assertEqual(0,1)
