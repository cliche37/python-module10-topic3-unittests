from class_definitions.student import Student
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.person = Student('Smith', 'John', 'Software Engineering')

    def tearDown(self):
        del self.person

    def test_object_created_required_attributes(self):
        self.assertEqual(self.person.last_name, 'Smith')
        self.assertEqual(self.person.first_name, 'John')
        self.assertEqual(self.person.major, 'Software Engineering')

    def test_object_created_all_attributes(self):
        self.student = Student('Smith', 'John', 'Software Engineering', 2.1)

        self.assertEqual(self.student.last_name, 'Smith')
        self.assertEqual(self.student.first_name, 'John')
        self.assertEqual(self.student.major, 'Software Engineering')
        self.assertEqual(self.student.gpa, 2.1)


if __name__ == '__main__':
    unittest.main()