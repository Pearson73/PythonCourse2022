

class Person(object):

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def person_name(self):
        print("This person is called %s %s" % (self.firstname, self.lastname))


class Student(Person):

    def __init__(self, firstname, lastname, subject):
        #Person.__init__(self, firstname, lastname)
        super(Student, self).__init__(firstname, lastname)
        self.subject = subject

    def student_info(self):
        print("The student %s %s studies %s" % (self.firstname, self.lastname, self.subject))


class Teacher(Person):

    def __init__(self, firstname, lastname, course):
        super(Teacher,self).__init__(firstname, lastname)
        self.course = course

    def teacher_info(self):
        print("The teacher %s %s teaches the course %s" % (self.firstname, self.lastname, self.course))



