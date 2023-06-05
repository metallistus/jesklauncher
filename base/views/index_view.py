from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Profile, Todo, TodaysNotes
import google.auth
import requests


from allauth.socialaccount.models import SocialToken, SocialApp
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from rest_framework.authtoken.models import Token
from ..utils import  get_email_text, get_header_value

import base64


@login_required(login_url='base:sign-in')
def index_view(request):
   email_list = []
   socialApp = SocialApp.objects.get(provider='google')
   
   socialGoogleToken = SocialToken.objects.filter(account__user=request.user, account__provider='google').last()
   
   socialGoogleToken = SocialToken.objects.filter(account__user=request.user, account__provider='google').last()
   if socialGoogleToken:
      access_token = socialGoogleToken.token
   
      responseEmail = requests.get('https://www.googleapis.com/gmail/v1/users/me/messages', params={
         'access_token': access_token,
         'maxResults': 10
      })
      
      
      # print('______________response______________', response)
      if responseEmail.status_code == 200:
         emails = responseEmail.json().get('messages', [])
         # print('____________emails______________', emails)
         
         email_list = []
         for email in emails:
               email_id = email['id']
               email_response = requests.get(f'https://www.googleapis.com/gmail/v1/users/me/messages/{email_id}', params={
                  'access_token': access_token
               })
               
               if email_response.status_code == 200:
                  email_data = email_response.json()
                  message_id = email_data['id']
                  sender = get_header_value(email_data['payload']['headers'], 'From')
                  title = get_header_value(email_data['payload']['headers'], 'Subject')
                  created_time = get_header_value(email_data['payload']['headers'], 'Date')
                  
                  email_list.append({
                     'id': message_id,
                     'sender': sender, 
                     'title': title, 
                     'created_time': created_time[:-6],
                  })
   
   today_notes = TodaysNotes.objects.filter(user=request.user)
   todos = Todo.objects.filter(user=request.user)

   if request.method == 'POST':
      type = request.POST.get('type')
      
      if type == 'todays_notes':
         today_note_message = request.POST.get('today_note_message')
            
         message = TodaysNotes.objects.create(
            user = request.user,
            message = today_note_message
         )
         
         return redirect('base:index')
      
      if type == 'todo':
         todo = request.POST.get('note')
            
         message = Todo.objects.create(
            user = request.user,
            message = todo
         )
         
         return redirect('base:index')
                  
   context = {
      'today_notes': today_notes,
      'todos': todos,
      
      'emails': email_list,
   }
   return render(request, 'base/index.html', context)
   
@login_required(login_url='base:sign-in')
def delete_comment_view(request, task_id):
   task = Todo.objects.get(id=task_id)
   task.delete()
   return redirect('/')

@login_required(login_url='base:sign-in')
def delete_today_note_view(request, task_id):
   task = TodaysNotes.objects.get(id=task_id)
   task.delete()
   return redirect('/')

