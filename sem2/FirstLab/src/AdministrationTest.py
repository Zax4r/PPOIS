import unittest
from Administration import Administration

class AdministrationTest(unittest.TestCase):
    def setUp(self):
        self.students = []
        self.tests = {}
        self.teachers = []
        self.subjects = set()

    def test_add_students(self):
        self.students = Administration.add_student(self.students)
        self.assertEqual(len(self.students),1)

    def test_add_tests(self):
        self.tests,self.subjects = Administration.add_test(self.tests,self.subjects)
        self.assertEqual(len(self.tests),1)
        self.assertEqual(len(self.subjects),1)

    def test_add_teacher(self):
        self.teachers = Administration.add_teacher(self.teachers)
        self.assertEqual(len(self.teachers),1)
