from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from .models import userInfo, stuInfo, feed

# Create your views here.
def index_page(request):

    fd = feed.objects.order_by('date_time').reverse()[0]
    return render(request,'index.html',{'feedback' : fd})


def registration_page(request):

    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']

        user = userInfo( username = username, password = password)
        user.save()
        print('user created')
        return redirect('/login')
    else:
        return render(request,'registration.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if userInfo.objects.filter(username = username, password = password).exists():
            fd = feed.objects.order_by('date_time').reverse()[0]
            return render(request,'index.html', {"Data": username , 'feedback' : fd})
            
        else:
            return redirect('/login')
    else:
        return render(request,'login.html')


def stu_info(request,name):
    if request.method == 'POST':
       
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_no =  request.POST['phone_no']
        guardian_name = request.POST['guardian_name']
        caste = request.POST['caste']
        nationality = request.POST['nationality']
        gender = request.POST['gender']
        email = request.POST['email']
        age = request.POST['age']
        address = request.POST['address']

        stu = stuInfo(first_name = first_name, last_name = last_name, email = email, phone_no = phone_no, guardian_name = guardian_name,
        caste = caste, nationality = nationality, gender = gender, username = name, age = age, address = address)
        stu.save()
        context = stuInfo.objects.all().filter(username = name)
        return render(request,'stu-info-show.html',{'name' : context})
    
    else:
        if stuInfo.objects.filter(username = name).exists():
            context = stuInfo.objects.all().filter(username = name)
            if stuInfo.objects.filter(status = True):
                return render(request,'stu-info-show.html',{'name' : context, 'status' : True})
            else:
                return render(request,'stu-info-show.html',{'name' : context})
            
        else:
            return render(request, 'stuinfo.html', {'name' : name})


def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        feedback = request.POST['feedback']

        if name == '' and feedback == '':
            fed = feed(name = 'No Name', feedback = 'No recent Feedback')
        elif name == '':
            fed = feed(name = 'Annonymous', feedback = feedback)
        elif feedback == '':
            fed = feed(name = name , feedback = 'No Feedback provided')
        else:
            fed = feed(name = name, feedback = feedback)

        fed.save()
        return redirect('/')
    
   
def notice_1(request,name):
    return render(request, 'notice.html',{'name' : name} )


def notice_2(request):
    return render(request, 'notice.html')        



def dept_IT_1(request,name):
    return render(request, 'dept.html',{'name' : name} )


def dept_IT_2(request):
    return render(request, 'dept.html')    

    
