from django.test import TestCase
from ..models import Faculty
from ..models import Course
from ..models import Room

# Create your tests here.
class FacultyTests(TestCase):
    # def setUp(self):
    #     Faculty.objects.create(name='f', email='mail@mail.com', role='chair')
    #     Course.objects.create(name='c1',)
    #     Course.objects.create(name='c2',)
    #     Course.objects.create(name='c3',)
        
    
    def testrun(self):
        d = Faculty(name='d', email= 'mail@mail.com')
        d.save()
        c1 = Course(name='c1')
        c1.save()
        c2 = Course(name='c2')
        c2.save()
        d.course_preference.add(c1, c2)
        Faculty.objects.filter(course_preference=c1)
        assert(Faculty.objects.filter(pk=c1.pk, course_preference__pk=c2.pk).exists())
    #     f = Faculty.objects.get(name='f')
    #     c1 = Course.objects.get(name='c1')
    #     c2 = Course.objects.get(name='c2')
    #     c3 = Course.objects.get(name='c3')
    #     f.course_preference.add(c1, c2, c3)

class CourseTests(TestCase):
    def test_course_creation(self):
        name = 'COMP151'
        section=1
        crn=123
        units = 3
        needs_computer = True
        has_lab = True
        lab_needs_computer = True
        c = Course(name=name, section=section, crn=crn, units=3,
            needs_computer=needs_computer, has_lab=has_lab,
            lab_needs_computer=lab_needs_computer)
        c.save()
        self.assertEqual(str(c), name)
        self.assertEqual(c.section, section)
        self.assertEqual(c.crn, crn)
        self.assertEqual(c.units, units)
        self.assertEqual(c.needs_computer, needs_computer)

    def test_course_deletion(self):
        name = 'COMP151'
        section=1
        crn=123
        units = 3
        needs_computer = True
        has_lab = True
        lab_needs_computer = True
        c = Course(name=name, section=section, crn=crn, units=3,
            needs_computer=needs_computer, has_lab=has_lab,
            lab_needs_computer=lab_needs_computer)
        c.save()
        self.assertEqual(str(c), name)
        self.assertEqual(c.section, section)
        self.assertEqual(c.crn, crn)
        self.assertEqual(c.units, units)
        self.assertEqual(c.needs_computer, needs_computer)
        c.delete()
        # self.assertRaises(DoesNotExist, c)

class RoomTests(TestCase):
    def create_room(self):
        r = Room(building='Loma', number=306)
        self.assertEqual(str(r), 'Loma')

    def test_room_number(self):
        r = Room(building='Loma', number=306)
        self.assertEqual(r.number, 306)

    def testrun(self):
        d = Faculty(name='d', email= 'mail@mail.com')
        d.save()
        c1 = Course(name='c1')
        c1.save()
        c2 = Course(name='c2')
        c2.save()
        d.course_preference.add(c1, c2)
        Faculty.objects.filter(course_preference=c1)
        assert(Faculty.objects.filter(pk=c1.pk, course_preference__pk=c2.pk).exists())