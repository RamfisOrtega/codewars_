import re
from unittest import TestCase

import count_words
import collections


class Test(TestCase):
    def test_splitWordBySpace_first_word(self):
        result = count_words.splitWordBySpace("welcome to the jungle")
        self.assertEqual(result[0], "welcome")

        long_text = """I’d been using my sphere as a stool. I traced counterclockwise circles on it with my 
        fingertips and it shrank until I could palm it. My bolt had shifted while I’d been sitting. I pulled it up 
        and yanked the pleats straight as I careered around tables, chairs, globes, and slow-moving fraas. I passed 
        under a stone arch into the Scriptorium. The place smelled richly of ink. Maybe it was because an ancient 
        fraa and his two fids were copying out books there. But I wondered how long it would take to stop smelling 
        that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must be 
        deep into everything. """

        rsult = count_words.splitWordBySpace(long_text)

    def test_splitWordBySpace_last_word(self):
        result = count_words.splitWordBySpace("welcome to the jungle")
        self.assertEqual(result[3], "jungle")

    def test_num_of_split_words(self):
        n_words = len(count_words.splitWordBySpace("welcome to the jungle"))
        self.assertEqual(n_words, 4)

    def test_disregarding_no_alphabetic_characters(self):
        result = count_words.disregarding_no_alphabetic_characters("Hello there, little user5453 374 ())$. I’d been "
                                                                   "using my sphere")
        lst_result = result.split()
        self.assertTrue(collections.Counter(lst_result) == collections.Counter(re.sub('[^a-zA-Z]', ' ', "Hello there, "
                                                                                                        "little user "
                                                                                                        "I d been "
                                                                                                        "using my "
                                                                                                        "sphere").split()))

    def test_exclude_words(self):
        test_list = ['Hello', 'there', 'little', 'user', 'I', 'd', 'been', 'using', 'my', 'sphere', 'as', 'a', 'stool',
                     'Slow']
        correct_list = ['Hello', 'there', 'little', 'user', 'I', 'd', 'been', 'using', 'my', 'sphere', 'stool', 'Slow']

        result = count_words.exclude_words(test_list)
        self.assertTrue(collections.Counter(result) == collections.Counter(correct_list))

    def test_word_count(self):
        self.assertEqual(count_words.word_count("hello there"), 2)
        self.assertEqual(count_words.word_count("hello there and a hi"), 4)
        self.assertEqual(count_words.word_count("I'd like to say goodbye"), 6)
        self.assertEqual(count_words.word_count("Slow-moving user6463 has been here"), 6)
        self.assertEqual(count_words.word_count("%^&abc!@# wer45tre"), 3)
        self.assertEqual(count_words.word_count("abc123abc123abc"), 3)
        self.assertEqual(count_words.word_count("Really2374239847 long ^&#$&(*@# sequence"), 3)
        self.assertEqual(count_words.word_count("Hello there, little user5453 374 ())$."), 4)

        long_text = """I’d been using my sphere as a stool. I traced counterclockwise circles on it with my 
        fingertips and it shrank until I could palm it. My bolt had shifted while I’d been sitting. I pulled it up 
        and yanked the pleats straight as I careered around tables, chairs, globes, and slow-moving fraas. I passed 
        under a stone arch into the Scriptorium. The place smelled richly of ink. Maybe it was because an ancient 
        fraa and his two fids were copying out books there. But I wondered how long it would take to stop smelling 
        that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must be 
        deep into everything. """
        self.assertEqual(count_words.word_count(long_text), 112)

    def test_word_count_efficient(self):
        self.assertEqual(count_words.word_count_efficient("hello there"), 2)
        self.assertEqual(count_words.word_count_efficient("hello there and a hi"), 4)
        self.assertEqual(count_words.word_count_efficient("I'd like to say goodbye"), 6)
        self.assertEqual(count_words.word_count_efficient("Slow-moving user6463 has been here"), 6)
        self.assertEqual(count_words.word_count_efficient("%^&abc!@# wer45tre"), 3)
        self.assertEqual(count_words.word_count_efficient("abc123abc123abc"), 3)
        self.assertEqual(count_words.word_count_efficient("Really2374239847 long ^&#$&(*@# sequence"), 3)
        self.assertEqual(count_words.word_count_efficient("Hello there, little user5453 374 ())$."), 4)

        long_text = """I’d been using my sphere as a stool. I traced counterclockwise circles on it with my 
                fingertips and it shrank until I could palm it. My bolt had shifted while I’d been sitting. I pulled it up 
                and yanked the pleats straight as I careered around tables, chairs, globes, and slow-moving fraas. I passed 
                under a stone arch into the Scriptorium. The place smelled richly of ink. Maybe it was because an ancient 
                fraa and his two fids were copying out books there. But I wondered how long it would take to stop smelling 
                that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must be 
                deep into everything. """
        self.assertEqual(count_words.word_count_efficient(long_text), 112)