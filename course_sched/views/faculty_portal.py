
'''
Chair portal page
'''
from django.shortcuts import render

def faculty_portal(request):
    ''' index page '''
    return render(request, 'course_sched/faculty_portal.html')
