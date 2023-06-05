import base64

def get_header_value(headers, name):
    for header in headers:
        if header['name'] == name:
            return header['value']
    return None

def get_email_text(payload):
    if 'parts' in payload:
        for part in payload['parts']:
            if 'body' in part:
                data = part['body'].get('data')
                if data:
                    return base64.urlsafe_b64decode(data).decode('utf-8')
    return None