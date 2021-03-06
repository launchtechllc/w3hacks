from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from datetime import datetime, date
from home import models


def index(request):
    return render(request, "home/index.html")


def contact(request):
    return render(request, "home/contact.html")


def team(request):
    return render(request, "home/team.html")


def join(request):
    return render(request, "home/join.html")


def faqs(request):
    return render(request, "home/faqs.html")


def events(request):
    events = models.Event.objects.all().order_by('-datetime')
    return render(request, "home/events/events.html", context={
        "events": events
    })


def event(request, event_url):
    if models.Event.objects.filter(url_extension=event_url).exists():
        event = models.Event.objects.get(url_extension=event_url)
        return render(request, "home/events/event.html", context={
            "event": event
        })

    else:
        return render(request, "errors/does-not-exist.html", context={
            "title": "Event doesn't exist!",
            "content": "We're sorry, but we couldn't find the event you were looking for! It has either been removed, or you have navigated to the wrong page. Please go back to the previous page if possible."
        })


# LEGAL PAGES
def terms_of_service(request):
    return render(request, "home/legal/terms-of-service.html")

def privacy_policy(request):
    return render(request, "home/legal/privacy-policy.html")

def code_of_conduct(request):
    return render(request, "home/legal/code-of-conduct.html")
