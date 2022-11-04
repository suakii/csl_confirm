from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from csl.models import StudentInform
from csl.models import SubjectInform

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



        for i, line in enumerate(lines):
            fields = line.split(",")
            if (i == 0):
                try:
                    informs = SubjectInform.objects.all().delete()
                except Exception as e:
                    pass
                try:
                    form = SubjectInform()
                    form.inform0 = fields[0]
                    try:
                        form.inform0 = fields[0]
                    except Exception as e:
                        form.inform0 = ""

                    try:
                        form.inform1 = fields[1]
                    except Exception as e:
                        form.inform1 = ""
                    try:
                        form.inform2 = fields[2]
                    except Exception as e:
                        form.inform2 = ""
                    try:
                        form.inform3 = fields[3]
                    except Exception as e:
                        form.inform3 = ""
                    try:
                        form.inform4 = fields[4]
                    except Exception as e:
                        form.inform4 = ""
                    try:
                        form.inform5 = fields[5]
                    except Exception as e:
                        form.inform5 = ""
                    try:
                        form.inform6 = fields[6]
                    except Exception as e:
                        form.inform6 = ""
                    try:
                        form.inform7 = fields[7]
                    except Exception as e:
                        form.inform7 = ""
                    try:
                        form.inform8 = fields[8]
                    except Exception as e:
                        form.inform8 = ""
                    try:
                        form.inform9 = fields[9]
                    except Exception as e:
                        form.inform9 = ""
                    try:
                        form.inform10 = fields[10]
                    except Exception as e:
                        form.inform10 = ""

                    form.save()
                except Exception as e:
                    pass

            else:
                try:
                    informs = StudentInform.objects.filter(student_id=User.objects.get(username=fields[0]).pk)
                    informs.delete()
                except Exception as e:
                    pass
                try:
                    form = StudentInform()
                    form.student_id = User.objects.get(username=fields[0]).pk

                    try:
                        form.inform1 = fields[1]
                    except Exception as e:
                        form.inform1 = ""
                    try:
                        form.inform2 = fields[2]
                    except Exception as e:
                        form.inform2 = ""
                    try:
                        form.inform3 = fields[3]
                    except Exception as e:
                        form.inform3 = ""
                    try:
                        form.inform4 = fields[4]
                    except Exception as e:
                        form.inform4 = ""
                    try:
                        form.inform5 = fields[5]
                    except Exception as e:
                        form.inform5 = ""
                    try:
                        form.inform6 = fields[6]
                    except Exception as e:
                        form.inform6 = ""
                    try:
                        form.inform7 = fields[7]
                    except Exception as e:
                        form.inform7 = ""
                    try:
                        form.inform8 = fields[8]
                    except Exception as e:
                        form.inform8 = ""
                    try:
                        form.inform9 = fields[9]
                    except Exception as e:
                        form.inform9 = ""
                    try:
                        form.inform10 = fields[10]
                    except Exception as e:
                        form.inform10 = ""


                    form.save()
                except Exception as e:
                    print(e)
                    pass

    except Exception as e:
        messages.error(request, "Unable to upload file. " + repr(e))

    messages.success(request, str(len(lines)-1) + " 명의 정보가 추가 되었습니다.")
    student_list = StudentInform.objects.all()
    subject_list = SubjectInform.objects.all()

    context = {
                'student_list': student_list,
                'subject_list' : subject_list,
               }
    return render(request, 'csl/csl_list.html', context)

