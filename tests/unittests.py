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
        student = Student('Smith', 'John', 'Software Engineering', 2.1)

        self.assertEqual(student.last_name, 'Smith')
        self.assertEqual(student.first_name, 'John')
        self.assertEqual(student.major, 'Software Engineering')
        self.assertEqual(student.gpa, 2.1)

    def test_student_str(self):
        self.assertEqual("Smith, John has major Software Engineering with gpa: 0.0", self.person.__str__())

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = Student(56, 'John', 'Software Engineering')


if __name__ == '__main__':
    unittest.main()