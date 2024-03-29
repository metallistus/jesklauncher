import requests
import asyncio


def GoogleYoutubeService(email_list, access_token):
   async def fetch_todos():
      response = requests.get('https://www.googleapis.com/youtube/v3/activities', params={
            'access_token': access_token,
            'maxResults': 10,
            'mine': True,
            'part': 'snippet',
      })     
      
      
      for task_list in response.json().get('items', []):         
         activity = task_list.get('snippet', {})
         print('___________youtube______ activity', activity)
         video_id = task_list['id']
         created_time = activity['publishedAt']
         
         # # Process the tasks for the current list
         email_list.append({
            'id':  video_id,
            'type': 'YouTube',
            'title':  activity['title'],
            'sender' : '',
            'link': "",   
            'text': activity['description'],
            'created_time': created_time,
         })
         
      print('Google YouTube loaded successfully ✅')
                     
      return email_list
   
   asyncio.run(fetch_todos())