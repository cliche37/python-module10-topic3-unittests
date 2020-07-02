from class_definitions.student import Student
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.person = Student('Smith', 'John', 'Software Engineering')

    def tearDown(self):
        del self.person

    def test_object_created_required_attributes(self):
        self.assertEqual('Smith', self.person.last_name)
        self.assertEqual('John', self.person.first_name)
        self.assertEqual('Software Engineering', self.person.major)

    def test_object_created_all_attributes(self):
        student = Student('Smith', 'John', 'Software Engineering', 2.1)

        self.assertEqual('Smith', self.person.last_name)
        self.assertEqual('John', self.person.first_name)
        self.assertEqual('Software Engineering', self.person.major)
        self.assertEqual(2.1, student.gpa)

    def test_student_str(self):
        self.assertEqual("Smith, John has major Software Engineering with gpa: 0.0", self.person.__str__())

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = Student(7, 'John', 'Software Engineering')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            p = Student('Smith', '123', 'Software Engineering')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = Student('Smith', 'John', '234123')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            p = Student('Smith', 'John', 'History', "omcprre")
            p = Student('Smith', 'John', 'History', 44)
            p = Student('Smith', 'John', 'History', -1)


if __name__ == '__main__':
    unittest.main()
