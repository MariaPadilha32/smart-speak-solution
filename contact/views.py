from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContactForm, ContactGeneralForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Contact


def contact(request):
    """A view to return contact form and page"""
    form = ContactForm()

    """customer must be logged in to prevent spam."""
    if not request.user.is_authenticated:
        messages.error(request, 'Please login to contact us')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent')
            return redirect(reverse('home'))
        else:
            messages.error(request,
                           'Something went wrong. Please try again later')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form
    }
    return render(request, template, context)


def contactgeneral(request):
    """A view to return contact form and page"""
    form = ContactGeneralForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent')
            return redirect(reverse('home'))
        else:
            messages.error(request,
                           'Something went wrong. Please try again later')
    else:
        form = ContactForm()

    template = 'contact/contact-general.html'
    context = {
        'form': form
    }
    return render(request, template, context)


def contactfaq(request):

    return render(request, 'contact/contact-faq.html')


def is_admin(user):
    return user.is_superuser


@login_required
@user_passes_test(is_admin)
def view_contact_messages(request):
    """Admin view to display all contact messages"""
    contacts = Contact.objects.all().order_by('-id')
    template = 'contact/contact_messages.html'
    context = {
        'contacts': contacts
    }
    return render(request, template, context)
