from django.urls import path
from .views import index_views, auth

urlpatterns = [
   # ? auth
   path('sign-in', auth.sign_in_view, name='sign-in' ),
   path('sign-up', auth.sign_up_view, name='sign-up' ),
   
   # ? profile update
   path('update-profile',index_views.update_profile_info, name='update-profile' ),
   
   # ? notes
   path('notes', index_views.tasks_view, name='notes'),
   path('notes/<int:id>/', index_views.task_view, name='note'),
]
