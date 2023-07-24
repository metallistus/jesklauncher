from django.http import JsonResponse
from allauth.socialaccount.models import SocialToken, SocialApp

from ...utils import  get_email_text, get_header_value
from ...services.google import google_calendar, google_todos , google_gmail


# @csrf_exempt
def list(request):
    if request.method == 'GET':
        todo_list = []
    
        socialGoogleToken = SocialToken.objects.filter(account__user=request.user, account__provider='google').last()
        if socialGoogleToken:
            access_token = socialGoogleToken.token
            
            #GOOGLE TODO
            google_todos.GoogleTodoService(todo_list, access_token)
            
            print(todo_list)
            
            if len(todo_list) > 0:
                data = [{
                        'id': todo['id'],
                        'title': todo['title'],
                        'created_time': str(todo['created_time']),
                    } for todo in todo_list]
                
                data = sorted(data, key=lambda x: x['created_time'])
                
                return JsonResponse({
                    'status':'success',
                    'messages': data[::-1],
                }, safe=False)