from django.shortcuts import render

def index():
    pass

from .models import Exam, Student, Subject
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExamForm,StudentForm,SubjectForm
from rest_framework.decorators import action

def index(request):
    return render(request,"sessionUniversity/index.html", {"sessionUniversity": Exam.objects.all()})

def exam(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    return render(request, "sessionUniversity/exam.html", {"exam": exam})

def forms(request, d):
    if(int(d)==1):
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
        form = ExamForm()
        return render(request, "sessionUniversity/form.html", {'form':form})
    if(int(d)==2):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        form = StudentForm()
        return render(request, "sessionUniversity/form.html", {'form':form})
    if(int(d)==3):
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
        form = SubjectForm()
        return render(request, "sessionUniversity/form.html", {'form':form})
    return 1
    
def ex1(request, id=0):
    if(id!=0):
        return render(request, "sessionUniversity/ex1.html", {"id": int(id),"exams": Exam.objects.all(),"sessionUniversity": Subject.objects.all()})
        
    return render(request,"sessionUniversity/ex1.html", {"sessionUniversity": Subject.objects.all()})

@action(detail=True, methods=['get'])
def ex2(request, id=0, date=''):
    if 'select' in request.GET:
        return render(request, "sessionUniversity/ex2.html", {"id": int(request.GET['select']),"dateEx": request.GET['date'],"exams": Exam.objects.all(),"sessionUniversity": Subject.objects.all()})
        
    return render(request,"sessionUniversity/ex2.html", {"sessionUniversity": Subject.objects.all(),"exams": Exam.objects.all()})

def ex3(request, id=0, date=''):
    
    return render(request,"sessionUniversity/ex3.html", {"exams": Exam.objects.all()[:5]})