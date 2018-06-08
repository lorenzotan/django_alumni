from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Student

from .forms import StudentForm

# Create your views here.

def index(request):

    #template = loader.get_template('alumni/index.html')
    #student = get_object_or_404(Student)
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            #form.save()
            post = form.save(commit=False)
            post.save()
            #return HttpResponseRedirect(reverse('alumni:student', args=(post.id)))
            #return HttpResponseRedirect('alumni/thankyou.html') # need to map in url
            return render(request, 'alumni/thankyou.html')      # just goes to thank you page

    else:
        form = StudentForm()
    return render(request, 'alumni/index.html', {'form': form })


def student(request, student_id):
    template = loader.get_template('alumni/student.html')
    student = Student.objects.get(id=student_id)
    context = {
        'student': student,
    }
    return HttpResponse(template.render(context, request))


def students(request):
    template = loader.get_template('alumni/students.html')
    student_list = Student.objects.all()
    context = {
        'students': student_list,
    }

    return HttpResponse(template.render(context, request))
