from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from allauth.socialaccount.models import SocialToken

def get_gmail_service(request):
    social_account = SocialAccount.objects.get(provider='google', user=request.user)
    
    # social_token = SocialToken.objects.get(account=social_account)
    # social_token = SocialToken.objects.get(account__user=request.user, account__provider='google')
    # creds = Credentials.from_authorized_user_info(info=social_token.token)
    # service = build('gmail', 'v1', credentials=creds)
    return social_account