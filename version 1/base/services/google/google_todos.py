import requests

def GoogleTodoService(email_list, access_token, response_tasks):
   for task_list in response_tasks.json().get('items', []):
      list_id = task_list['id']
      list_title = task_list['title']
      
      # Request tasks for the current list
      response_tasks = requests.get(f'https://www.googleapis.com/tasks/v1/lists/{list_id}/tasks', params={
         'access_token': access_token,
         'maxResults': 10
      })
      
      # Process the tasks for the current list
      for task in response_tasks.json().get('items', []):
         task_id = task['id']
         task_title = task['title']
         task_updated = task['updated']
         email_list.append({
            'id':  task['id'],
            'type': 'google_todo',
            'title':  task['title'],
            'link': f"https://mail.google.com/tasks/canvas?pli=1&vid=default&task={task['id']}",   
            'created_time': task['updated'][:-5]
         })
         
         # Print or do something with the task details
         # print('____________________________________', task)
         
   return email_list