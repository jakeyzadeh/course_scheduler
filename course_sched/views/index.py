'''
index page
'''
from django.shortcuts import render

def index(request):
    ''' index page '''
    return render(request, 'course_sched/index.html')
