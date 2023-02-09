from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

def index(request):
    return render(request, 'main/index.html')

def projects(request):
    return render(request, 'main/projects.html')

def resume(request):
    return render(request, 'main/resume.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sender_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email_address']
            email_message = form.cleaned_data['message']
            send_mail(sender_name + " (" + email_address + ")", email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)

            return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/contact.html', context)
