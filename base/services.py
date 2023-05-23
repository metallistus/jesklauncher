from allauth.socialaccount.models import SocialAccount
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


def get_gmail_service(request):
    # Get the user's Google OAuth2 credentials from their social account
    social_account = SocialAccount.objects.get(user=request.user, provider='google')
   #  credentials = Credentials.from_authorized_user_info(social_account.extra_data)
   #  print(credentials)
    # Build the Gmail API service using the user's credentials
    service = build('gmail', 'v1', credentials=credentials)
    print(service)
    return service