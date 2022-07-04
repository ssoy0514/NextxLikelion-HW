from re import template
from django.shortcuts import redirect, render
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy

# Create your views here.
class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()

    return render(request,'home.html',{'majors':majors, 'subjects': subjects})

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

def statisticSubjectView(request):
    subjects = Subject.objects.all()
    statisticMajor = subjects.filter(major__name = '통계학과')

    return render(request, 'statistic.html',{'statisticMajor': statisticMajor})

def industrialSubjectView(request):
    subjects = Subject.objects.all()
    industrialMajor = subjects.filter(major__name = '산업경영공학과')

    return render(request, 'industrial.html',{'industrialMajor': industrialMajor})

class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')

def DeleteSubjectView(request, subject_pk):
    delSubject = Subject.objects.get(pk=subject_pk)
    delSubject.delete()
    return redirect('home')