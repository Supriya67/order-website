from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import make_password, check_password
from .models import UserProfile
from django.views import View


# Create your views here.
'''def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request,'invalid username or password')
            return redirect('signin')

    else:
        return render(request, 'signin.html')

def signup(request):

    if request.method == 'POST':
        profile_form = UserProfileform(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        address=request.POST['address']
        phone1=request.POST['phone1']
        phone2=request.POST['phone2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name taken")
                return redirect('signup.html')
            elif User.objects.filter(email=email).exists():
                print("email already exists ")
                return redirect('signup')
            if len(phone2)!=10:
                print("invalid no.")
                return redirect('signup')
            if len(phone1)!=10:
                print('invalid no.')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email,phone1=phone1,phone2=phone2,address=address)
                user.save()
                if profile_form.is_valid():
                    profile=profile_form.save(commit=False)
                    profile.user = user
                    profile.save()
                print("user created")
                return redirect('signin')
        else:
            print("password not matching")
            return redirect('singup')
    else:
        profile_form=UserProfileform()
        context={'profile_form':profile_form}
        return render(request,'signup.html',context)
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
def sucesssignup(request,uid):
    template = render_to_string('automatemsg.html',{'name':request.user.profile.first_name})
    email=EmailMessage('welcome!!', template ,settings.EMAIL_HOST_USER,[request.user.profile.email],)
    email.fail_silently=False
    email.send()
    project=User.objects.get(id=uid)
    context={'project':project}
    return render(request,'signup.html',context)
def signout(request):
    auth.logout(request)
    return redirect('/')'''
class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self , request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        username = postData.get('username')
        email = postData.get('email')
        phone1 = postData.get('phone1')
        phone2 = postData.get('phone2')
        password = postData.get('password')
        password2 = postData.get('password2')
        address = postData.get('address')
        user = UserProfile(username=username, password=password, first_name=first_name, last_name=last_name,
                           email=email, phone1=phone1, phone2=phone2, address=address)
        # validation
        value = {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email,
                 'phone1': phone1, 'phone2': phone2, 'address': address}
        error_msg = None
        if password != password2:
            error_msg = 'password not matching'
        if UserProfile.objects.filter(username=username).exists():
            error_msg = 'username taken'
        if UserProfile.objects.filter(email=email).exists():
            error_msg = 'email already exists'
        if len(phone1) != 10:
            error_msg = 'invalid number'
        if (len(phone2) != 10 and len(phone2) > 0):
            error_msg = 'invalid number'
        # saving
        if not error_msg:
            user.password = make_password(user.password)
            user.register()
            return redirect('signin')
        else:
            return render(request, 'signup.html', {'error_msg': error_msg, 'value': value})


class Signin(View):
    def get(self,request):
        return render(request, 'signin.html')
    def post(selfself, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserProfile.get_user_by_username(username)
        error_msg = None
        if user:
            flag = check_password(password, user.password)
            if flag:
                request.session['user_id']=user.id
                request.session['username'] = user.username
                request.session['email']=user.email
                return redirect('index')
            else:
                error_msg = "email id or password invalid !!"
        else:
            error_msg = "email id or password invalid !!"
        print(username, password)
        return render(request, 'signin.html', {'error_msg': error_msg})




def signout(request):
    request.session.clear()
    return redirect('index')