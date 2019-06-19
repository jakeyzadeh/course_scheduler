from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.forms import modelformset_factory

from ..models import Course

from ..forms import CoursePost

def semester_manager(request):
    ''' render faculty manager page '''
    courses = Course.objects.all()
    return render(request, 'course_sched/semester_manager.html', {'courses': courses})

# def add_course(request):
#     ''' 
#     TODO CHECK NO RE ADD SAME COURSE
#     deleete things
#     '''
#     courses = Course.objects.all()
#     form = CoursePost()
#     if request.method == 'POST' and request.is_ajax():
#         data = {
#             'courseExists': any(c.crn == request.POST['crn'] for c in courses)
#         }
#         form = CoursePost(request.POST)
#         if form.is_valid() and not data['courseExists']:
#             form.save()
#         return JsonResponse(data)
#     return HttpResponse('course_sched/semester_manager.html')
#     # return render(request, 'course_sched/semester_manager.html', {'courses': courses, 'form': form})
