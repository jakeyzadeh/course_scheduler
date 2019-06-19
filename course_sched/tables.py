'''
Table objects to send to client for rendering
'''
import django_tables2 as tables
from .models import Faculty
from .models import Course

class FacultyTable(tables.Table):
    name = tables.TemplateColumn('<button class="editEntryButton" onclick="editFaculty(\'{{record.id}}\', \'{{record.name}}\', \'{{record.email}}\', \'{{record.role}}\')">{{record.name}}</button>')
    class Meta:
        model = Faculty
        fields = ('name', 'email', 'role')

class FacultyPreferences(tables.Table):
    class Meta:
        model = Faculty
        exclude = ('id', 'email', 'role')

class CourseTable(tables.Table):
    name = tables.TemplateColumn('<button class="editEntryButton" onclick="editCourse(\'{{record.id}}\', \'{{record.name}}\', \'{{record.crn}}\', \'{{record.units}}\', \'{{record.needs_computer}}\', \'{{record.has_lab}}\', \'{{record.lab_needs_computer}}\')">{{record.name}}</button>')
    class Meta:
        model = Course
        exclude = ('id', )