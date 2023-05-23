from django.contrib.auth.models import User
from django_telegram_auth.backends import TelegramAuthBackend
from telegram_login import TelegramLoginButton


class CustomTelegramLoginButton(TelegramLoginButton):
    def get_request_data(self, request):
        data = super().get_request_data(request)
        data.update({'state': request.GET.get('next', '')})
        return data

class CustomTelegramAuthBackend(TelegramAuthBackend):
    def authenticate(self, request, telegram_user, **kwargs):
        user, created = User.objects.get_or_create(username=telegram_user.username)
        return user
