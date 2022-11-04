from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from csl.models import StudentInform
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


@login_required(login_url='common:login')
def upload(request):
    data = {}
    if "GET" == request.method:
        return render(request, "common/upload.html", data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return HttpResponseRedirect(reverse("common:upload"))
        # if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
            return HttpResponseRedirect(reverse("common:upload"))

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")
        # loop over the lines and save them in db. If error , store as string and then display

        for line in lines[1:]:
            fields = line.split(",")
            try:
                question = StudentInform.objects.filter(student_id=User.objects.get(username=fields[0]).pk)
                question.delete()
            except Exception as e:
                pass
            try:
                form = StudentInform()
                form.student_id = User.objects.get(username=fields[0]).pk
                form.inform1 = fields[1]
                form.inform2 = fields[2]
                form.inform3 = fields[3]
                form.inform4 = fields[4]
                form.inform5 = fields[5]
                form.inform6 = fields[6]
                form.inform7 = fields[7]
                form.inform8 = fields[8]
                form.inform9 = fields[9]
                form.inform10 = fields[10]
                form.save()
            except Exception as e:
                pass

    except Exception as e:
        messages.error(request, "Unable to upload file. " + repr(e))

    messages.success(request, str(len(lines)-1) + " 명의 정보가 추가 되었습니다.")
    student_list = StudentInform.objects.all()
    context = {
                'student_list': student_list,
               }

    return render(request, 'csl/csl_list.html', context)

