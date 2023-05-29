from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
from pathlib import Path

from django.contrib.auth.models import User
from ...models import Profile, Todo
from ..serializers import ProfileSerializer, UserSerializer, TodoSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt import tokens


@api_view(['GET', 'POST'])
def update_profile_info(request):
   user = request.user
   
   if user == None or user == '':
      return Response({'status': '404 Not Found'})
   
   profile = Profile.objects.get(user=user)
   
   if request.method == 'GET':
      return Response(ProfileSerializer(profile, many=False).data)
   
   if request.method == 'POST':
      text = request.data.get('text')
      validate = False
         
      if text and profile.text != text:
         validate = True
         profile.text = text
         
      if 'image' in request.FILES:
         validate = True
         old_image = Profile.objects.get(id=id).image.name
         old_image_path = Path(old_image)
         
         if old_image_path.is_file():
            os.remove(old_image_path)
         
         new_image = request.FILES['image']
         
         profile.image= new_image
         
      if validate:
         profile.save()
          
      return Response(ProfileSerializer(profile, many=False).data)
      

# @csrf_exempt
@api_view(['GET', 'POST'])
def tasks_view(request):
   access_token = request.COOKIES.get('access_token')
   
   # print('_____________', access_token)
   # payload = tokens.AccessToken(access_token, verify=False)
   # user_id = payload['user_id']
   
   if request.method == 'GET':
      user = User.objects.get(id=1)
      
      todos = Todo.objects.filter(user = 1) 
            
      if todos:
         return Response({
            'status': 'success',
            'count': todos.count(),
            'data': TodoSerializer(todos, many=True).data,
         })
      else: 
         return Response({
            'status': 'success',
            # 'count': todos.count(),
            'message': ''
         })
   
   if request.method == 'POST':
      message =   request.data['message']
      
      user = User.objects.get(id=user_id)
      
      todo = Todo.objects.create(
         user = user,
         message = message
      )  
      return Response(TodoSerializer(todo, many=False).data)
      
      
@api_view(['DELETE'])
def task_view(request, task_id):
   access_token = request.COOKIES.get('access_token')
   
   payload = tokens.AccessToken(access_token, verify=False)
   user_id = payload['user_id']
   
   user = User.objects.get(id=user_id)   
   task = Todo.objects.get(id=task_id)
   
   if user.id == task.id:
      task.delete()