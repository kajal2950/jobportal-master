from django.shortcuts import render,redirect
from django.contrib import messages
from . models import  Category2,JobApply,Job2,Company,Certificate,Contact,Curriculum,Service
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    service=Service.objects.all
    s=Service.objects.order_by('-name')[1:5]
    company=Company.objects.all
    certificate=Certificate.objects.all
    catt=Category2.objects.all
    job2=Job2.objects.order_by('-id')[0:4]
    data={
        'category':category,
        'job':job2,
        'catt':catt,
        'company':company,
        'certificate':certificate,
        'service':service,
        's':s
    }
    return render(request,'index.html',data)

def about(request):
    service=Service.objects.all
    company=Company.objects.all
    data={
        
        'company':company,
        'service':service
        
    }
    return render(request,'about.html',data)


def service_detail(request,slug):

    company=Company.objects.all
    service=Service.objects.all
    services=Service.objects.filter(slug=slug)
    data={
        
        'service':service,
        'company':company,
        'services':services,

        
    }
    return render(request,'service.html',data)


def category(request,slug):
    service=Service.objects.all
    
    job2=Job2.objects.filter(slug=slug)
    data={
       
        'job':job2,
        'service':service
    }

    return render(request,'category.html',data)

def detail(request,slug):
    job2=Job2.objects.order_by('-id')[0:4]
    company=Company.objects.filter(slug=slug)
    service=Service.objects.all

    data={
        'company':company,
        'job':job2,
        'service':service
    }
    return render(request,'company-details.html',data)
   

# def category(request,id):
#     jobs=Job.objects.filter(id=id)
#     data={
        
#         'jobs':jobs
#     }
   
#     return render(request,'category.html',data)


def job_oppening(request):
    service=Service.objects.all
    job2=Job2.objects.all
    data={
        'job':job2,
        'service':service
    }

    return render(request,'current_job_openning.html',data)


def apply(request):
    service=Service.objects.all
    data={
        
        'service':service
    }
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        city=request.POST.get('city')
        field=request.POST.get('field')
        exp=request.POST.get('exp')
        resume=request.FILES['resume']
        print(resume)

        apply=JobApply(name=name,email=email,phone=phone,address=address,city=city,criteria=field,exp=exp,resume=resume)
        apply.save()
        # messages.info(request,"Applied Successfully")
        # return redirect('/')

        subject=name
        message=name
        resume=resume
        email_from=settings.EMAIL_HOST_USER
        try:
            send_mail(subject,message,email_from ,['payalkasayp2950@gmail.com'])
            apply.save()
            messages.info(request,"Applied Successfully")
            return redirect('apply')
        
        except Exception as e:
            print(e)
            return redirect("apply")

    return render(request,'apply.html',data)

def contact(request):
    service=Service.objects.all
    data={
        
        'service':service
    }
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        address=request.POST.get('address','')

        print(name)

        contact=Contact(name=name,email=email,phone=phone,desc=desc,address=address)
       
        subject=name
        message=desc
        email_from=settings.EMAIL_HOST_USER
        try:
            send_mail(subject,message,email_from ,['payalkasayp2950@gmail.com'])
            contact.save()
            messages.info(request,"Message Sent Successfully")
            return redirect('/')
             
        except Exception as e:
            return redirect('contact')

    return render(request,'contact.html',data)


   



def userlogin(request):
    service=Service.objects.all
    data={
       
        'service':service
    }
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        

        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request, user)
            
            messages.success(request,'Successfully logged In')
            return redirect("/")

        else:
            messages.error(request,'User not Signup')
            return redirect('userlogin') 

    return render(request,'userlogin.html',data)


def signup(request):
    service=Service.objects.all
    data={
        
        'service':service
    }
    if request.method=="POST":
        username=request.POST.get('username')
        
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

       
        
        if User.objects.filter(email=email).exists():
            messages.info(request,"Email already taken")
            return redirect("registration")


       
        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return redirect("signup")
        
        if pass1 != pass2:
            messages.error(request,"Password do not matched")
            return redirect("signup")

        
        myuser=User.objects.create_user(username,email,pass1)
        
        myuser.save()

        
        messages.success(request,"User Created")
        return redirect("signup")
        
    else:

        return render(request,'signup.html',data)


def userlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

def resume(request):
    catt=Category2.objects.all
    service=Service.objects.all
    data={
        'catt':catt,
        'service':service
    }
    if request.method=='POST': 
        name=request.POST.get('name','')
        gender=request.POST.get('gender','')
        address=request.POST.get('address','')
        phone=request.POST.get('phone','')
        resume=request.FILES['resume']
        carrier=request.POST.get('carrier','')
        email=request.POST.get('email','')
        salary=request.POST.get('salary','')
        exp=request.POST.get('exp','')
      
        desc=request.POST.get('desc','')
        
       
        print(resume)
        
        curriculum=Curriculum(name=name,gender=gender,address=address,phone=phone,resume=resume,carrier=carrier,email=email,salary=salary,exp=exp,desc=desc)
        curriculum.save()
        messages.info(request,"Successfully Submiited")
        return redirect('/')
    


    return render(request,'resume.html',data)


def search(request):
    service=Service.objects.all
    query=request.GET.get('query')
    job=Job2.objects.filter(name__icontains=query)

    data={
        'job':job,
        'service':service
    }

    return render(request,'search.html',data)