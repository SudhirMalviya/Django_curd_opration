from django.shortcuts import render,HttpResponse,redirect
from .models import Signup,Query
from django.shortcuts import render, get_object_or_404
# from django.urls import reverse
# from django.contrib import messages


def home (request):
      return render(request,'app/home.html')
def product(request):
      return render(request,'app/product.html')
def about(request):
      return render(request,'app/about.html')   
def contact(request):
   return render(request,'app/contact.html')
def award(request):
   return render(request,'app/awrad.html')
# -------------------------------------------------------------------------------------------
# ------------------SIGNUP & LOGIN-----------------------------------------------------------
# -------------------------------------------------------------------------------------------
def singup(request):
   return render(request,'app/singup.html')

def savedata(req):
         if req.method == "POST":
            name=req.POST['nm']
            email=req.POST['em']
            mobile=req.POST['mobile']
            password=req.POST['pass']
            if(name==""):
                  msg="please enter your name"
                  return render(req,'app/singup.html',{"error":msg})
            elif(email==""):
                  msg="please enter your email"
                  return render(req,'app/singup.html',{"error":msg})      
            elif(len(password)<=5):
                  msg="password is too short password must be 5 char"
                  return render(req,'app/singup.html',{"error":msg})
            elif Signup.objects.filter(email=email).exists():
                  msg = "Email already exists"
                  return render(req, 'app/singup.html', {"error": msg})
            else:
                  Signup.objects.create(name=name,email=email,mobile=mobile,password=password)
                  msg="registraion suceses"
                  return render(req,'app/login.html',{"data":msg})
         else:
            return render(req,'app/singup.html')
#  --------------------------------------------------------------------------------------------
# --------------------------------------------------------------- -----------------------------
def login(req):
       return render (req,'app/login.html')

def logindata(req):
     if req.method =='POST':
          email=req.POST['em']
          password=req.POST['pass']
          if Signup.objects.filter(email=email,password=password).exists():
             data=Signup.objects.filter(email=email)
             data1 = Query.objects.filter(qemail=email)
             return render(req,'app/dashbord.html',{'key':data,'key1': data1})
          else:
             return render(req,'app/singup.html')
# ---------------------------------------------------------------------------------------------- 
            #  DASHBORD & QUERY CURD OPRATION---------------------------------------------------
# ----------------------------------------------------------------------------------------------

def dashbord(req):
   return render(req,'app/dashbord.html')

def query_view(request, email):
    if request.method == "POST":
        query_text = request.POST['query']
        user_exists = Signup.objects.filter(email=email).exists()
        if user_exists:
           data1= Query.objects.create(qemail=email, qname=query_text)
        data1 = Query.objects.filter(qemail=email)
        data=Signup.objects.filter(email=email)
        return render(request, 'app/dashbord.html', {'key1': data1,'key':data})
    else:
        return render(request, 'error_page.html', {'error_message': 'Invalid request'})
    
def showquery(request):
     return render(request,'app/dashbord.html')


def delete_view(request, pk):
    query_object = get_object_or_404(Query, id=pk)
    if request.method == 'POST':
         query_object.delete()
         data1 = Query.objects.filter(qemail=query_object.qemail)
         data = Signup.objects.filter(email=query_object.qemail)
         return render(request, 'app/dashbord.html', {'key1': data1,'key':data})
    else:
       return render(request, 'app/dashbord.html', {'query': query_object})

 
def edit_query(request, pk):
    obj = get_object_or_404(Query, id=pk)

    if request.method == 'POST':
        new_qname = request.POST.get('queryname')
        obj.qname = new_qname
        obj.save()
        data1 = Query.objects.filter(qemail=obj.qemail)
        data = Signup.objects.filter(email=obj.qemail)
        return render(request, 'app/dashbord.html', {'key1': data1, 'key': data})
    return render(request, 'app/dashbord.html', {'key1': [obj]})

# -----------------------------------------------------------------------------------------
#---------------------CURD END ------------------------------------------------------------
# -----------------------------------------------------------------------------------------


































































































# def showdata(req,pk):
#      data=Signup.objects.get(email=pk)
#      name=data.name
#      email=data.email
#      mobile=data.mobile
#      password=data.password
#      user={
#           "name":name,
#           "email":email,
#           "mobile":mobile,
#           "password":password,
          
#      }
#      all_data=Query.objects.filter(email=pk)
#      return render (req,'app/home.html',{'kuser':user,"kdata":all_data})



