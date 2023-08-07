import requests

def CallendarService(email_list, access_token):
   response_calendar = requests.get('https://www.googleapis.com/calendar/v3/calendars/primary/events', params={
         'access_token': access_token,
         'maxResults': 10
      })
   events = response_calendar.json().get('items', [])
   for event in events:
      email_list.append({
         'id': event['id'],
         'type': 'google_event',
         'title':  event['summary'], 
         'link': f"https://calendar.google.com",
         'text': event['description'],
         'created_time': event['created'][:-5]
      })
      
   return email_list