from django.shortcuts import render,render_to_response
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.files.base import ContentFile
# Create your views here.


def index(request):
    return render(request,'web/index.html')


def signup(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            new_user = form.save()
            return  HttpResponseRedirect('thanks')
    else:
        form = signup_form()
    return render(request,'web/signup.html',{'form':form})


def signup_thanks(request):
    return render(request,'web/signup_thanks.html')


@login_required
def profile(request):
    user = request.user
    return render(request,'web/profile.html',{'user':user})


@login_required
def edit_profile(request):
    if request.POST:
        user = User.objects.get(pk=request.user.id)
        user.username = request.POST.get('user')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()

        tutee = Tutee.objects.get(user=request.user)
        profile_pic = ContentFile(request.FILES['profile_pic'].read())
        tutee.profile_pic.save(request.FILES['profile_pic'].name,profile_pic)

        return HttpResponseRedirect('/web/accounts/profile/')

    user_profile = request.user.profile
    return render_to_response('web/edit_profile.html',{'profile':user_profile},context_instance=RequestContext(request))


@login_required
def view_profile(request):
    user = User.objects.get(pk=request.user.id)
    user_profile = request.user.profile
    return render(request,'web/view_profile.html',{'profile':user_profile})


@login_required
def verify_student(request):
    if request.POST:
        user = User.objects.get(pk=request.user.id)
        tutee = Tutee.objects.get(user=request.user)
        matric_photo = ContentFile(request.FILES['matric_photo'].read())
        tutee.matric_photo.save(request.FILES['matric_photo'].name, matric_photo)

        return HttpResponseRedirect('/web/accounts/profile/')

    user_profile = request.user.profile
    return render_to_response('web/verify_student.html', {'profile': user_profile},
                                  context_instance=RequestContext(request))


@login_required
def join_tutor_form(request):
    if request.method == 'POST':
        form = tutor_form(request.POST)
        if form.is_valid():
            tutor = form.save(commit=False)
            tutor.user = request.user
            tutor.save()
            form.save_m2m()
            return HttpResponseRedirect('/accounts/join-tutor/thanks/')
    else:
        form = tutor_form()
    return render_to_response('web/join_tutor.html', {'form': form},context_instance=RequestContext(request))


def join_tutor_thanks(request):
    return render(request,'web/join_tutor_thanks.html')
    
def advanced_search(request):
    form = adv_search_form(request.POST or None)
	return render(request, 'web/adv_search_results.html')
