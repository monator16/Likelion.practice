from django.shortcuts import render, redirect
from .models import Major,Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajormodelForm, SubjectmodelForm
from django.urls import reverse_lazy

# Create your views here.

class AddMajorView(CreateView):
    model = Major
    form_class = MajormodelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

    
class EditMajorView(UpdateView):
    model = Major
    form_class= MajormodelForm
    template_name = 'editMajor.html'
    success_url = reverse_lazy('home')       


def major(request):
    majors= Major.objects.all()
    return render(request, 'major.html', {'majors': majors})

def subject(request):
    subjects= Subject.objects.all()
    return render(request, 'subject.html', {'subjects':subjects})

def home(request):
    
    return render(request, 'home.html')




def businessSubjectsView(request):
    subjects = Subject.objects.all()
    bizmajor =subjects.filter(major__name='경영학과')
    return render(request,'business.html',{'bizmajor':bizmajor} )

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectmodelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

def DeleteSubjectView(request, subject_pk):
    delSubject = Subject.objects.get(pk=subject_pk)
    delSubject.delete()
    return redirect('home')

def DeleteMajorView(request, major_pk):
    delMajor = Major.objects.get(pk=major_pk)
    delMajor.delete()
    return redirect('home')
    

class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectmodelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')




