#write function tests here, don't add input('') statements here!
import unittest
import sys
sys.path.insert(0, '/workspaces/final-jessebIII')

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_c.question_c import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())


class Test_Question_C(unittest.TestCase):

    def test_get_most_likely_ancestor_consensus(self):
        pos1, pos2, pos3 = get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT")
        self.assertEqual(2, pos1)
        self.assertEqual(4, pos2)
        self.assertEqual(10, pos3)


