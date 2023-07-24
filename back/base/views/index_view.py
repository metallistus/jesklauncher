from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='base:sign-in')
def index_view(request):
   return render(request, 'base/index.html')

