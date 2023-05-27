import requests
def get_google_calendar_auth_url(client_id, redirect_url, scope):
    """Gets the URL for authorizing access to Google Calendar."""
    return f'https://accounts.google.com/o/oauth2/auth?client_id={client_id}&redirect_uri={redirect_url}&scope={scope}&response_type=code'


def get_google_calendar_access_token(code, client_id, client_secret, redirect_url, grant_type):
    """Gets the access token for accessing Google Calendar."""
    token_url = 'https://accounts.google.com/o/oauth2/token'
    data = {
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_url,
        'grant_type': grant_type
    }
    response = requests.post(token_url, data=data)
    return response.json().get('access_token')


def get_google_calendar_events(access_token):
    """Gets the events from Google Calendar."""
    calendar_url = 'https://www.googleapis.com/calendar/v3/calendars/primary/events'
    headers = {'Authorization': f'Bearer {access_token}'}
    events_response = requests.get(calendar_url, headers=headers)
    return events_response.json().get('items', [])