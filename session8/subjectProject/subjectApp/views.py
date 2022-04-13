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


def home(request):
    majors= Major.objects.all()
    subjects= Subject.objects.all()
    return render(request, 'home.html', {'majors': majors, 'subjects':subjects})

def businessSubjectView(request):
    bizsubjects = Subject.objects.filter(major__name= '경영학과')
    return render(request,'business.html', {'bizsubjects':bizsubjects} )

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectmodelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')



def delete(request,	subject_pk):
    subject= Subject.objects.get(pk=subject_pk)
    subject.delete()

    return redirect('home')



class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectmodelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')




