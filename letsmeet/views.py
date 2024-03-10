from django.shortcuts import render, redirect
from .models import Linkup, Attendee
from .forms import RegistrationForm

# Create your views here.

def index(request):
    link_ups = Linkup.objects.all()
    return render(request, 'letsmeet/index.html', {
        'link_ups': link_ups
    })

def linkup_details(request, linkup_slug):
    try:
        selected_linkup = Linkup.objects.get(slug=linkup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
            
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                attendee, _ = Attendee.objects.get_or_create(email=user_email)
                selected_linkup.attendees.add(attendee)
                return redirect('confirm-event-signup', linkup_slug=linkup_slug)

        return render(request, 'letsmeet/linkup-details.html', {
                'linkup_found': True,
                'linkup': selected_linkup,
                'form': registration_form
            })
    except Exception as e:
        return render(request, 'letsmeet/letsmeet-details.html'),{
            'linkup_found': False
        }

def confirm_event_signup(request, linkup_slug):
    linkup = Linkup.objects.get(slug=linkup_slug)
    return render(request, 'letsmeet/confirmation-page.html', {
        'organizer_email': linkup.organizer_email
    })