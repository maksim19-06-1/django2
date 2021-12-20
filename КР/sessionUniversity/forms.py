from django import forms
from django.forms import ModelForm
from .models import Exam, Student, Subject

class ExamForm(ModelForm):
    class Meta:
        model=Exam
        fields = ['subject','student','date','mark']
        # fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields = '__all__'
class SubjectForm(ModelForm):
    class Meta:
        model=Subject
        fields = '__all__'