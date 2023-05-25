from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..services import get_gmail_service
from ..models import Profile, Todo, TodaysNotes
import google.auth

from allauth.socialaccount.models import SocialToken, SocialApp
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from rest_framework.authtoken.models import Token
from .index_view import get_gmail_service


@login_required(login_url='base:sign-in')
def index_view(request):
   # service = get_gmail_service(request)
   
   # result = service.users().messages().list(userId='me', maxResults=10).execute()
   # messages = result.get('messages', [])
   # for message in messages:
   #      msg = service.users().messages().get(userId='me', id=message['id']).execute()
   #      print(msg['snippet'])
   # social_token = SocialToken.objects.get(account__user=request.user, account__provider='google')
   # access_token = social_token.token
   
   # credentials = Credentials.from_authorized_user_info(request.user.socialaccount_set.get(provider='google').extra_data)
   # service = build('people', 'v1', credentials=credentials)
   # results = service.people().get(resourceName='people/me', personFields='emailAddresses').execute()
   # email_addresses = results['emailAddresses']
   # print(email_addresses)
   
   access_token = request.COOKIES.get('access_token')
   today_notes = TodaysNotes.objects.filter(user=request.user)

   if request.method == 'POST':
      type = request.POST.get('type')
      
      if type == 'todays_notes':
         today_note_message = request.POST.get('today_note_message')
            
         message = TodaysNotes.objects.create(
            user = request.user,
            message = today_note_message
         )
         
         return redirect('base:index')
                  
   context = {
      'today_notes': today_notes
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

