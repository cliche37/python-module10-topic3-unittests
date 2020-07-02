class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):

        bad = set('1234567890')

        if not isinstance(lname, str) or not isinstance(fname, str) or not isinstance(major, str):
            raise ValueError

        if bad.issuperset(lname) or bad.issuperset(fname) or bad.issuperset(major):
            raise ValueError

        if not isinstance(gpa, float) or 0.0 > gpa > 4.0:
            raise ValueError

        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
