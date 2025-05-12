from django.shortcuts import render, redirect
from django.contrib import messages

from django.utils import timezone
from datetime import timedelta

from .models import Contact
from .forms import ContactForm


def add_contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            telegram = form.cleaned_data['telegram']
            one_hour_ago = timezone.now() - timedelta(minutes=5)

            recent_contact = Contact.objects.filter(
                telegram=telegram, created_at__gte=one_hour_ago
            ).exists()

            if recent_contact:
                messages.error(request, "Please wait 5 minutes to send another message.")
            else:
                form.save()
                messages.success(request, 'Your message sent successfully')

            return render(request, 'app/index.html', {'form': ContactForm()})

    else:
        form = ContactForm()

    return render(request, 'app/index.html', {'form': form})

