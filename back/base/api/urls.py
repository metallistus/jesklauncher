from django.urls import path
from .views import auth, todo, today_tasks, messages, user, social_todos

urlpatterns = [
    # TODO: ____ todos _____
    path('todos', todo.todo_list_create, name='todo_list_create'),
    path('todos/<str:pk>', todo.todo_delete, name='todo_delete'),
    
    # TODO: ____ today notes _____
    path('today-notes', today_tasks.today_notes_list_create, name='today_notes_list_create'),
    path('today-notes/<str:pk>', today_tasks.today_notes_delete, name='today_notes_delete'),

    # TODO: ____ messages _____
    path('messages', messages.messages_list, name='messages_list'),  
    
    # TODO: ____ settings _____
    path('update-settings', user.update_settings, name='update_settings'), 
    
    # TODO: ____ todo _____
    path('social-todos', social_todos.list, name='social_todos_list'),
]