from django.db import models
import datetime

class TimeSlot(models.Model):
    beg = models.TimeField(default=datetime.time(8, 00))
    end = models.TimeField(default=datetime.time(20, 00))
    pass


class Day(models.Model):
    time_slots = models.ManyToManyField(TimeSlot)
    name = models.CharField(max_length=3, default='mon')

    def __str__(self):
        return self.name
    pass

class Course(models.Model):
    name = models.CharField(max_length=100)
    crn = models.IntegerField(default=0)
    units = models.IntegerField(default=3)
    needs_computer = models.BooleanField(default=False)
    has_lab = models.BooleanField(default=False)
    lab_needs_computer = models.BooleanField(default=False)
    cannot_conflict = models.ManyToManyField("self")
    suggested_faculty = models.ManyToManyField("Faculty")

    def __str__(self):
        return self.name
    pass

class SemesterCourse(models.Model):
    course = models.OneToOneField(Course, on_delete=models.PROTECT)
    section = models.IntegerField(default=1)

    def __str__(self):
        return self.course.name
    pass

class Faculty(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default='@sandiego.edu')
    role = models.CharField(max_length=50, default='Faculty')
    course_preference = models.ManyToManyField(Course)
    day_preference = models.ManyToManyField(Day)

    def __str__(self):
        return self.name

class WeekView(models.Model):
    days = models.ManyToManyField(Day)
    pass


class Room(models.Model):
    building = models.CharField(max_length=50, default='Serra')
    number = models.IntegerField(default=0)
    reserved_time = models.OneToOneField(WeekView, default=None, on_delete=models.PROTECT)

    def __str__(self):
        return self.building + ' ' + str(self.number)


class Semester(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(default=2019)

    def __str__(self):
        return self.name + ' ' + str(self.year)

'''
Room:
    start with all availability
        as classes are scheduled in rooms, 
        take that time out of room availability
            'soft checks'-  still let glick put things, but show that they conflict
'''