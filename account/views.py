from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            mobile=form.cleaned_data['mobile']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            username=email.split("@")[0]
            user=Account.objects.create_user(firstname=firstname,lastname=lastname,email=email,mobile=mobile,username=username,password=password)
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your  account.'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
            messages.success(request,'User Registered Successfully')
            return redirect('register')
    else:
            form=RegistrationForm()

    context={'form':form}
    return render(request,'accounts/register.html',context)


def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Login')
            return redirect ('login')

    return render(request,'accounts/login.html')
#@login_required(login_url='login')
@login_required
def logout(request):

    auth.logout(request)
    messages.success(request,'You are Loged out')
    return redirect('login')
def activate(request, uidb64, token):
    return HttpResponse('OK')
