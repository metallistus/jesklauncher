# import allauth.socialaccount.models
from allauth.socialaccount.signals import pre_social_login
# from allauth.socialaccount.models import SocialApp, SocialToken

from django.apps import AppConfig
    
class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        pre_social_login.connect(pre_social_login_callback)
        
def pre_social_login_callback(request, sociallogin, **kwargs):
    socialtoken = sociallogin.token
    socialaccount = sociallogin.account
    print('_________SocialToken_______', socialtoken)
    # google_socialapp = SocialApp.objects.get(provider="google")
    # socialtoken.app_id = google_socialapp.id
    # socialtoken.account_id = socialaccount.id
    # socialtoken.save()
    
    # no sql - use mongodb
    # deploy on railway
    
    