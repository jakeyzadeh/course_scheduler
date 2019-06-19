from django.http import HttpResponse
from django.shortcuts import render
from ..tables import FacultyPreferences
from ..models import Faculty
from django_tables2 import RequestConfig

def faculty_preferences(request):
    ''' TODO '''
    table = FacultyPreferences(Faculty.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'course_sched/faculty_preferences.html', {'faculty': table})