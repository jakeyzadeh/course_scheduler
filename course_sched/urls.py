from django.urls import path

from . import views

urlpatterns = [
    # path(add_faculty, views.Faculty().save()),
    path('', views.index, name='index'),
    path('chair_portal/', views.chair_portal, name='chair_portal'),
    path('faculty_portal/', views.faculty_portal, name='faculty_portal'),
    # path('admin', views.admin, name='admin'),
    path('faculty_manager/', views.faculty_manager, name='faculty_manager'),
    path('faculty_manager/add/', views.add_faculty, name='add_faculty'),
    path('faculty_manager/edit/', views.edit_faculty, name='edit_faculty'),
    path('faculty_manager/delete/', views.delete_faculty, name='delete_faculty'),

    path('course_manager/', views.course_manager, name='course_manager'),
    path('course_manager/add/', views.add_course, name='add_course'),
    path('course_manager/edit/', views.edit_course, name='edit_course'),
    path('course_manager/delete/', views.delete_course, name='delete_course'),

    path('semester_manager/', views.semester_manager, name='semester_manager'),
    # path('semester_manager/add_course/', views.add_course, name='add_course'),

    path('faculty_preferences/', views.faculty_preferences, name='faculty_preferences'),
]

