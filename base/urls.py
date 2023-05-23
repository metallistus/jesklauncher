from django.urls import path

from .views.base_auth_view import sign_in_view, sign_up_view, sign_out_view, sign_in_social_media_view
from .views.index_view import index_view, delete_comment_view

app_name ='base'

urlpatterns = [
   path('',index_view, name='index'),
   path('tasks/<int:task_id>/delete', delete_comment_view, name='task_delete'),
   
   path('sign-in', sign_in_view, name='sign-in'),
   path('sign-up', sign_up_view, name='sign-up'),
   path('sign-out', sign_out_view, name='sign-out'),
   
   path('sign-in-social-media-view', sign_in_social_media_view, name='sign-in-social-media'),
]
