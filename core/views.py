from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import View, TemplateView
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from catalog.models import Category


class IndexView(TemplateView):

    template_name = 'index.html'

index = IndexView.as_view()


def contact(request):

    import os
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {
        'form': form,
        'success': success,
        'SECRET_KEY': os.getenv('SECRET_KEY'),
        'DEBUG': os.getenv('DEBUG')
    }
    return render(request, 'contact.html', context)

