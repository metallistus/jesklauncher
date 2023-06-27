from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Profile, Todo, TodaysNotes
import google.auth
import requests
from ..services.google import google_calendar, google_todos , google_gmail


from allauth.socialaccount.models import SocialToken, SocialApp
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from rest_framework.authtoken.models import Token
from ..utils import  get_email_text, get_header_value
from telegram import Bot

import base64


@login_required(login_url='base:sign-in')
def index_view(request):
   email_list = []
   socialApp = SocialApp.objects.get(provider='google')
   
   socialGoogleToken = SocialToken.objects.filter(account__user=request.user, account__provider='google').last()
   if socialGoogleToken:
       access_token = socialGoogleToken.token
      
       # CALLENDAR GOOGLE
       google_calendar.CallendarService(email_list, access_token)
         
       # GOOGLE TASKS
       response_tasks = requests.get('https://www.googleapis.com/tasks/v1/users/@me/lists', params={
          'access_token': access_token,
          'maxResults': 10
       })      
       google_todos.GoogleTodoService(email_list, access_token, response_tasks)

       # GOOGLE GMAIL
       google_gmail.GoogleGmailService(email_list, access_token, get_email_text, get_header_value)
   
   
   bot_token = '6263736045:AAHXJM8S4NLQKEiH7O1f88pKOa6x9Y0pqLc'
   bot = Bot(token=bot_token)
   print('___________bot_______________', bot)

   
   today_notes = TodaysNotes.objects.filter(user=request.user)
   todos = Todo.objects.filter(user=request.user)

   if request.method == 'POST':
       type = request.POST.get('type')
     
       # Add today notes
       if type == 'todays_notes':
          today_note_message = request.POST.get('today_note_message')
            
          message = TodaysNotes.objects.create(
             user = request.user,
             message = today_note_message
          )
         
          return redirect('base:index')
      
       # ADD New Todo
       if type == 'todo':
          isJesk = request.POST.get('isJesk')
          isGoogle_todo = request.POST.get('isGoogle_todo')
   #       todo = request.POST.get('note')
        
          # Add New Google Todo
          if (isGoogle_todo):
             gooogle_data_task = response_tasks.json().get('items', [])
             google_task_id = gooogle_data_task[0]['id']
             responseTask = requests.post(f'https://www.googleapis.com/tasks/v1/lists/{google_task_id}/tasks', params={
                'access_token': access_token,
             }, json={"title": todo})
             print('_________________________response_cloas____________', responseTask)
            
             return redirect('base:index')
            
         
          else: # Add New Jesk Todo          
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

