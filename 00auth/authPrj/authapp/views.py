import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from django.shortcuts import render
from django.shortcuts import render
from .utils.scrap import scrape_and_pretty_print
from django.contrib.auth.decorators import login_required

# @login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )



def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("index")))


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def index(request):
    # Check if the user is authenticated
    if request.session.get("user"):
        session_data = request.session.get("user")
        
        # Get the user's nickname from the session data
        nickname = session_data.get("userinfo", {}).get("nickname")
        
        if nickname:
            # Scrape and get HTML content for each profile
            medium_html = scrape_and_pretty_print(f"https://medium.com/@{nickname}")
            instagram_html = scrape_and_pretty_print(f"https://www.instagram.com/@{nickname}/")
            
            return render(
                request,
                "index.html",
                context={
                    "session": session_data,
                    "pretty": json.dumps(session_data, indent=4),
                    "medium_html": medium_html,
                    "instagram_html": instagram_html,
                },
            )
    
    # If the user is not authenticated, return to the index without scraped content
    return render(
        request,
        "index.html",
        context={
            "session": None,  # No user session
        },
    )