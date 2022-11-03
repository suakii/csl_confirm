from django.shortcuts import render
from .models import StudentInform
from django.contrib.auth.decorators import login_required


@login_required(login_url='common:login')
def index(request):
    student_list = StudentInform.objects.all()
    context = {'student_list': student_list}
    return render(request, 'csl/csl_list.html', context)