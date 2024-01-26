from django.shortcuts import render
from datetime import datetime
from event.models import Event


# Create your views here.
def landing_page(request):
    upcoming_events = Event.objects.filter(date_time__gt=datetime.now()).order_by(
        "date_time"
    )

    # Passer ces événements au contexte du template
    context = {"upcoming_events": upcoming_events}
    return render(request, "landing_page.html", context)
