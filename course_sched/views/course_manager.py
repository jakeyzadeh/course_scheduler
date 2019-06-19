'''
Course manager views
'''
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from django_tables2 import RequestConfig
from django.shortcuts import render

from ..models import Course
from ..tables import CourseTable
from ..forms import CoursePost


def course_manager(request):
    ''' Landing page for course manager'''
    table = CourseTable(Course.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'course_sched/course_manager.html', {'table': table})


@csrf_exempt
def add_course(request):
    courses = Course.objects.all()
    if request.method == 'POST' and request.is_ajax():
        data = {
            'isCrnTaken': any(str(c.crn) == request.POST['crn'] for c in courses)
        }
        info = request.POST
        if not data['isCrnTaken']:
            Course(name=info['name'], crn=info['crn'], units=info['units'], 
                needs_computer='needs_computer' in info, has_lab='has_lab' in info, lab_needs_computer='lab_needs_computer' in info).save()
        return JsonResponse(data)

    return HttpResponse('course_sched/course_manager.html')

@csrf_exempt
def edit_course(request):
    courses = Course.objects.all()
    if request.method == 'POST' and request.is_ajax():
        data = {
            'isCrnTaken': any(str(c.crn) == request.POST['crn'] and str(c.id) != request.POST['id'] for c in courses)
        }
        if not data['isCrnTaken']:
            info = request.POST
            course = Course.objects.get(id=info['id'])
            course.name=info['name']
            course.crn=info['crn']
            course.units=info['units']
            course.needs_computer='needs_computer' in info
            course.has_lab='has_lab' in info
            course.lab_needs_computer='lab_needs_computer' in info
            course.save()
        return JsonResponse(data)

    return HttpResponse('course_sched/course_manager.html')

@csrf_exempt
def delete_course(request):
    if request.method == 'POST' and request.is_ajax():
        course = Course.objects.get(id=request.POST['id'])
        data = {
            'courseExists': course is not None
        }
        if data['courseExists']:
            course.delete()
        return JsonResponse(data)

    return HttpResponse('course_sched/faculty_manager.html')