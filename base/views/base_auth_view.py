from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken

from django.http import HttpResponse, HttpResponseRedirect

from ..forms import CreateUserForm
from ..models import Profile


def sign_in_view(request):
   if request.user.username:
      return redirect('base:index')
   
   page_type = 'sign-in'
   
   if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')
      
      try: 
         user = User.objects.get(username=email)
      except:
         messages.error(request, '')
         
      user = authenticate(username=email, password=password)
      
      
      if user is not None:
         login(request, user)
         
         refresh  = RefreshToken.for_user(user)
         token = str(refresh.access_token)
         
         response = HttpResponseRedirect('/')
         
         response.set_cookie('access_token', token)
      
         #  redirect('base:index')
         return response
      else:
         messages.error(request, 'Invalid password or username')
      
   context = {
      'page_type': page_type
   }
   return render(request, 'base/auth.html', context)

def sign_up_view(request):
   page_type = 'sign-up'
   form = CreateUserForm()
   
   if request.method == 'POST':
      form = CreateUserForm(request.POST)
      
      if form.is_valid():
         new_user = form.save(commit=False)
         new_user.save()
         login(request, new_user,  backend='django.contrib.auth.backends.ModelBackend' )
         
         profile = Profile(user = request.user)
         
         return redirect('base:sign-in-social-media')
      
   context = {
      'page_type': page_type,
      'form': form
   }
   return render(request, 'base/auth.html', context)

#apple id
@login_required(login_url='base:sign-in')
def sign_out_view(request):
   response = HttpResponseRedirect('/')
   response.delete_cookie('access_token')
   
   logout(request)
   return response


@login_required(login_url='base:sign-in')
def sign_in_social_media_view(request):
   user = request.user
   proifle = Profile.objects.get(user=user)
      
   context = {
      'profile': profile
   }
   return render(request, 'base/authIncludeAccounts.html', context)