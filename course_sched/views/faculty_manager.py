from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django_tables2 import RequestConfig
from ..models import Faculty
from ..tables import FacultyTable

@csrf_exempt
def faculty_manager(request):
    table = FacultyTable(Faculty.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'course_sched/faculty_manager.html', {'table': table})

@csrf_exempt
def add_faculty(request):
    faculty = Faculty.objects.all()
    if request.method == 'POST' and request.is_ajax():
        data = {
            'isEmailTaken': any(fac.email == request.POST['email'] for fac in faculty)
        }
        info = request.POST
        if not data['isEmailTaken'] and len(info['email']):
            Faculty(name=info['name'], email=info['email'], role=info['role']).save()
        return JsonResponse(data)

    return HttpResponse('course_sched/faculty_manager.html')

@csrf_exempt
def edit_faculty(request):
    faculty = Faculty.objects.all()
    if request.method == 'POST' and request.is_ajax():
        data = {
            'isEmailTaken': any(fac.email == request.POST['email'] and str(fac.id) != request.POST['id'] for fac in faculty)
        }
        if not data['isEmailTaken']:
            info = request.POST
            fac = Faculty.objects.get(id=info['id'])
            fac.name = info['name']
            fac.email = info['email']
            fac.role = info['role']
            fac.save()
        return JsonResponse(data)

    return HttpResponse('course_sched/faculty_manager.html')

@csrf_exempt
def delete_faculty(request):
    if request.method == 'POST' and request.is_ajax():
        fac = Faculty.objects.get(id=request.POST['id'])
        data = {
            'userExists': fac is not None
        }
        if data['userExists']:
            fac.delete()
        return JsonResponse(data)

    return HttpResponse('course_sched/faculty_manager.html')