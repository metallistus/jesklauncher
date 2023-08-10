from django.contrib import admin
from django.urls import path, include

# from allauth.socialaccount.providers.microsoft.views import MicrosoftOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.views import OAuth2CallbackView, OAuth2LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
    
    path('accounts/', include('allauth.urls')),
    
    # url(r'^accounts/microsoft/login/$', OAuth2LoginView.as_view(adapter=MicrosoftOAuth2Adapter), name='microsoft_login'),
    # url(r'^accounts/microsoft/callback/$', OAuth2CallbackView.as_view(adapter=MicrosoftOAuth2Adapter), name='microsoft_callback'),
]
