class Student(object):
    def __init__(self, idnum, firstname, midname,lastname, gender, course, yearlevel):
        self.idNum = idnum
        self.fstName = firstname
        self.midName = midname
        self.lstName = lastname
        self.gender = gender
        self.course = course
        self.yrLevel = yearlevel


class Course(object):
    def __init__(self, courseid, coursedesc):
        self.courseid = courseid
        self.coursedesc= coursedesc
