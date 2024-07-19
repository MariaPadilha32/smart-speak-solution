from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import NewsletterForm
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import SubscribedUsers
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import NewsletterForm
from .models import SubscribedUsers


def index(request):
    """
    View to return the index page
    """

    return render(request, "home/index.html")


def privacy_policy(request):
    """
    Render privacy_policy.html view
    """
    return render(request, "home/info/privacy_policy.html")


def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("/")

        if User.objects.filter(email=email).exists():
            messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
            return redirect(request.META.get("HTTP_REFERER", "/")) 

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()

        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))


@user_passes_test(lambda user: user.is_superuser)
def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            for subscriber in SubscribedUsers.objects.all():
                unsubscribe_link = (
                    f"http://127.0.0.1:8000/unsubscribe/{subscriber.email}/"
                )
                email_message_with_unsubscribe = (
                    f"{email_message}\n\nUnsubscribe link: {unsubscribe_link}"
                )

            mail = EmailMessage(subject, email_message, f"SmartSpeakSolutions <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Email sent succesfully")
            else:
                messages.error(request, "There was an error sending email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join([active.email for active in SubscribedUsers.objects.all()])
    return render(request=request, template_name='home/newsletter.html', context={'form': form})
