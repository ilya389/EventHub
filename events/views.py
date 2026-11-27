from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.utils import timezone
from .models import Event, Registration
from .forms import RegistrationForm

# Create your views here.
from .models import Event

def event_list(request):
    events = Event.objects.filter(is_published=True, date__gte=timezone.now()).order_by('date')
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, is_published=True)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Registration.objects.filter(event=event, email=email).exists():
                form.add_error('email', 'Вы уже зарегистрированы на это мероприятие.')
            else:
                registration = form.save(commit=False)
                registration.event = event
                registration.save()
                send_mail(
                    subject=f'Подтверждение регистрации: {event.title}',
                    message=f'Привет, {registration.name}!\n\nВаша заявка на мероприятие "{event.title}" на {event.date} принята. Статус: Новая.',
                    from_email='noreply@eventhub.com',
                    recipient_list=[registration.email],
                    fail_silently=False,
                )
                return redirect(f'/events/{event.id}/?success=1')
    else:
        form = RegistrationForm()
    return render(request, 'event_details.html', {'event': event, 'form': form})