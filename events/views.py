from django.shortcuts import render
from django.utils import timezone

# Create your views here.
from .models import Event

def event_list(request):
    events = Event.objects.filter(is_published=True, date__gte=timezone.now()).order_by('date')
    return render(request, 'event_list.html', {'events': events})