'''
Chair portal page
'''
from django.shortcuts import render

def chair_portal(request):
    ''' index page '''
    return render(request, 'course_sched/chair_portal.html')
