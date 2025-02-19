import unittest
from Marks import Marks

class MarksTest(unittest.TestCase):
    def setUp(self):
        self.marks = Marks()

    def test_add_test_results(self):
        self.marks.add_test_results("Math", 8, 10)
        self.assertIn("Math", self.marks._Marks__subjects)
        self.assertEqual(len(self.marks._Marks__test_results), 1)

    def test_marking(self):
        self.marks.add_test_results("Math", 8, 10)
        self.marks.marking()
        self.assertEqual(self.marks._Marks__marks["Math"], [8])

    def test_analytic(self):
        self.marks.add_test_results("Math", 8, 10)
        self.marks.marking()
        self.marks.analytic()
        self.assertEqual(self.marks._Marks__analytics["Math"], ["Зачёт!"])


    def test_marking_no_results(self):
        output = self.marks.marking() 
        self.assertIsNone(output)  

    def test_analytic_no_marks(self):
        output = self.marks.analytic() 
        self.assertIsNone(output) 
