from django.shortcuts import HttpResponse,render,HttpResponseRedirect
from .models import*
# Create your views here.

# def hello(self):
#     return HttpResponse("hello")

# def structure(self):
#     return HttpResponse("<h1>3d structure</h1>")

def store(request):    
    context=''
    if request.method== 'GET':
        name=request.GET.get('na','')
        email=request.GET.get('email','')
        password=request.GET.get('password','')
        print("name is", name)
        print("\n email is", email)
        print("\n password is", password)
        
        
        context={'name':name, 'email':email, 'password':password}
        user=Store()
        user.name=name
    return render(request, "store.html", context)

def mac(request):
    users=Store.objects.all()
    print("users>>",users)
    context={'allusers',users}
    
    return render(request, "mac.html", context)

def ipad(request):
    return render(request,"ipad.html")

def edit(request):
    ii=request.GET['iii']
    usersss=Mac.objects.get(id=ii)
    context={'uu':usersss}
    
    if request.method=='POST':
        idd=request.POST['rr']
        na=request.POST['na2']
        emm=request.POST['email1']
        passs=request.POST['password']
        try:
            us12=Mac.objects.get(id=idd)
        except Exception as ex:
            pass
        else:
            us12.name=na
            us12.email=emm
            us12.password=passs
            us12.save()
            return HttpResponseRedirect('../mac')
    return render(request, 'edit.html',context)

def delete1(request):
    i=request.GET['ii']
    userss=Mac.objects.get(id=i)
    userss.delete()
    #return render(request, 'home.html')
    return HttpResponseRedirect('../mac')