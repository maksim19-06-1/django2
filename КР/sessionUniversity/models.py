from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=64)
    semester = models.IntegerField()
    credits =  models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.name} - {self.semester} - {self.credits}"

class Student(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    birthDate =  models.DateTimeField()
    gender =  models.CharField(max_length=2)

    def __str__(self):
        return f"{self.id}: {self.firstName} - {self.lastName} - {self.birthDate} - {self.gender}"

class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name="subject")
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name="student")
    date =  models.DateTimeField()
    mark =  models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.subject} - {self.student} - {self.date} - {self.mark}"

from sessionUniversity.models import *   
