import os
from django.http import JsonResponse
from django.conf import settings
from django.views import View
from django.shortcuts import redirect
from .utils import get_google_calendar_auth_url, get_google_calendar_access_token, get_google_calendar_events


class GoogleCalendarInitView(View):
    def get(self, request):
        client_id = os.getenv('CLIENT_ID')
        redirect_url = settings.REDIRECT_URL
        scope = 'https://www.googleapis.com/auth/calendar'
        auth_url = get_google_calendar_auth_url(client_id, redirect_url, scope)
        return redirect(auth_url)


class GoogleCalendarRedirectView(View):
    def get(self, request):
        code = request.GET.get('code')
        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')
        redirect_url = settings.REDIRECT_URL
        grant_type = 'authorization_code'

        access_token = get_google_calendar_access_token(
            code, client_id, client_secret, redirect_url, grant_type)
        events = get_google_calendar_events(access_token)
        return JsonResponse(events, safe=False)
