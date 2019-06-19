'''
Forms for easily putting in templates
'''
from django.forms import ModelForm

from .models import Course


class CoursePost(ModelForm):
    ''' Create html form from course model info '''
    class Meta:
        model = Course
        fields = '__all__'
