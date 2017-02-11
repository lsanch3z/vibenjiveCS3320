from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from forms import UserForm, AddMusicForm
from forms import RegistrationForm
from vibenjive.models import VibenjiveUser, UserMusic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url="/login/")
def home(request):
    return render(request,"template.html")

def login(request):
    return render(request, 'login.html')

def delete_account_success(request):
    return render(request, 'delete_account_success.html')

def login_error(request):
    return render(request, 'login_error.html')

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)

    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login_error')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')

def auth_reg(request):
    username = request.POST.get('username', '')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    if email and password:
        user, created = User.objects.get_or_create(username=username,
                                                   first_name=first_name,
                                                   last_name=last_name,
                                                   email=email)
        if created:
            user.set_password(password)
            user.save()

        user = authenticate(username=username, password=password)
        auth_login(request, user)
        return HttpResponseRedirect('/registration/')
    else:
        HttpResponseRedirect('login')

@login_required(login_url="/login/")
def chpasswd(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        new_password1 = request.POST.get('new_password1','')
        form = PasswordChangeForm(request.user, request.POST)
        form.fields['old_password'].widget.attrs = {'class': 'input'}
        form.fields['new_password1'].widget.attrs = {'class': 'input'}
        form.fields['new_password2'].widget.attrs = {'class': 'input'}
        if form.is_valid():
            form.save()
            authenticate(username=username, password=new_password1)
            return HttpResponseRedirect('/update_success/')
        else:
            return render(request, 'chpasswd_error.html')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'updatepassword.html', {
        'form': form
    })

@login_required(login_url="/login/")
def account_management(request):
	return render(request, 'accountmanagement.html')

@login_required(login_url="/login/")
def account_management(request):
	return render(request, 'accountmanagement.html')

@login_required(login_url="/login/")
def update_email(request):
	return render(request, 'updateemail.html')

@login_required(login_url="/login/")
def email_error(request):
	return render(request, 'email_error.html')

@login_required(login_url="/login/")
def ch_email(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    email1 = request.POST.get('email1', '')
    email2 = request.POST.get('email2','')
    user = authenticate(username=username, password=password)
    e = User.objects.get(username=username)

    if user is not None:
        if email1 == email2:
            e.email = email1
            e.save()
            return HttpResponseRedirect('/update_success/')
    else:
        return HttpResponseRedirect('/email_error/')

@login_required(login_url="/login/")
def update_info(request):
	current = request.user
	context = {"currentuser": current}
	return render(request, 'updateinfo.html',context)

@login_required(login_url="/login/")
def ch_info(request):
    username = request.POST.get('username','')
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    zipcode = request.POST.get('zipcode', '')
    genres = request.POST.get('genres', '')
    instruments = request.POST.get('instruments', '')

    u = User.objects.get(username=username)
    v = VibenjiveUser.objects.get(username=username)

    if not first_name:
        u.first_name = first_name

    if not last_name:
        u.last_name = last_name

    if not zipcode:
        u.zipcode = zipcode

    if not genres:
        v.genres = genres

    if not instruments:
        v.genres = genres

    return HttpResponseRedirect('/update_success/')

@login_required(login_url="/login/")
def update_password(request):
	return render(request, 'updatepassword.html')

@login_required(login_url="/login/")
def delete_account(request):
	return render(request, 'deleteaccount.html')

@login_required(login_url="/login/")
def uploadaudio(request):
    return render(request, 'uploadaudio.html')

@login_required(login_url="/login/")
def search(request):
	try:
		if 'q' in request.GET and request.GET['q']:
			q = request.GET['q']
			queryR = UserMusic.objects.filter(genres__icontains=q) | UserMusic.objects.filter(instruments__icontains=q) | UserMusic.objects.filter(zipcode__icontains=q)
			context = {"object_lists": queryR, "username": "List"}
			return render(request,'searchresults.html',context)
	except ObjectDoesNotExist:
		return render(request,'searchresults.html')
	else:
		return render(request,'searchresults.html')


@login_required(login_url="/login/")
def del_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)

    if user is not None:
        user.delete()
        return render(request, 'delete_account_success.html')

    return render(request, 'delete_account_error.html')

@login_required(login_url="/login/")
def registration(request):
	return render(request, 'registration.html')

@login_required(login_url="/login/")
def add_user_info(request):
    if request.method == 'POST':
        f = RegistrationForm(request.POST)
	if f.is_valid:
        	f.save()
    return HttpResponseRedirect('/')

@login_required(login_url="/login/")
def update_success(request):
	return render(request, 'update_success.html')

@login_required(login_url="/login/")
def uploadaudio_success(request):
	return render(request, 'uploadaudio_success.html')

@login_required(login_url="/login/")
def deleteaudio_success(request):
	return render(request, 'deleteaudio_success.html')

@login_required(login_url="/login/")
def add_music(request):
    username = request.user.username
    u = VibenjiveUser.objects.get(username=username)
    f = AddMusicForm(request.POST)

    if f.is_valid():
        a = f.save()
        a.zipcode = u.zipcode
        a.save()
    return HttpResponseRedirect('uploadaudio_success')

@login_required(login_url="/login/")
def del_music(request):
    if request.method == 'POST':
        song_id = request.POST.get('song_id', '')
        a = UserMusic.objects.get(song_id=song_id)
        a.delete()
    return HttpResponseRedirect('deleteaudio_success')

@login_required(login_url="/login/")
def manageaudio(request):
    username = request.user.username
    try:
		queryR = UserMusic.objects.filter(username=username)
		context = {"object_lists": queryR, "username": "List"}
		return render(request,'manageaudio.html',context)
    except ObjectDoesNotExist:
		return render(request,'manageaudio.html')

@login_required(login_url="/login/")
def sendemail(request):
    username = request.user.username
    u = User.objects.get(username=username)
    username1 = request.POST.get('username1', '')
    u2 = User.objects.get(username=username1)

    send_mail(
    'Another Vibenjive wants to connect with you!',
    'User ' + username + ' would like to connect with you and can be contacted at ' + u.email,
    'contact@vibenjive.com',
    [u2.email],
    fail_silently=False,
    )
    return HttpResponseRedirect('email_success')

@login_required(login_url="/login/")
def email_success(request):
	return render(request, 'searchresults.html')
