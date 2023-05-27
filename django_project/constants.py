client_id = settings.CLIENT_ID
redirect_url = settings.REDIRECT_URL
scope = 'https://www.googleapis.com/auth/calendar'
auth_url = f'https://accounts.google.com/o/oauth2/auth?client_id={client_id}&redirect_uri={redirect_url}&scope={scope}&response_type=code'
        