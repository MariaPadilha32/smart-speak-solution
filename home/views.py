from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import NewsletterForm
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from .models import SubscribedUsers
from django.core.mail import send_mail
from django.conf import settings
from .forms import NewsletterForm


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
            messages.error(
                request,
                "You must type legit name and email to subscribe"
            )
            return redirect("/")

        if User.objects.filter(email=email).exists():
            messages.error(
                request,
                f"Found registered user with associated {email} email."
                "You must login to subscribe or unsubscribe."
            )
            return redirect(request.META.get("HTTP_REFERER", "/"))

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(
                request,
                f"{email} email address is already subscriber."
            )
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

        messages.success(
            request,
            f'{email} email was successfully subscribed to our newsletter!'
        )
        return redirect(request.META.get("HTTP_REFERER", "/"))


@user_passes_test(lambda user: user.is_superuser)
def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            # Loop through the subscribed users
            for subscriber in SubscribedUsers.objects.all():
                unsubscribe_link = (
                    f"http://127.0.0.1:8000/unsubscribe/{subscriber.email}/"
                )
                email_message_with_unsubscribe = (
                    f"{email_message}\n\nUnsubscribe link: {unsubscribe_link}"
                )

                # Create and send the email to each subscriber individually
                mail = EmailMessage(
                    subject,
                    email_message_with_unsubscribe,
                    f"SmartSpeakSolutions <{request.user.email}>",
                    [subscriber.email]
                )
                mail.content_subtype = 'html'

                if mail.send():
                    messages.success(
                        request,
                        f"Newsletter sent to {subscriber.email}"
                    )
                else:
                    messages.error(
                        request,
                        f"Failed to send to {subscriber.email}"
                    )

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = NewsletterForm()
    form.fields['receivers'].initial = ', '.join(
        [active.email for active in SubscribedUsers.objects.all()]
    )
    return render(
        request=request,
        template_name='home/newsletter.html',
        context={'form': form}
    )


def unsubscribe(request, email):
    try:
        subscriber = SubscribedUsers.objects.get(email=email)
        subscriber.subscribed = False
        subscriber.save()

        messages.success(
            request,
            f"{email} has been successfully unsubscribed."
        )
    except SubscribedUsers.DoesNotExist:
        messages.error(request, f"No subscription found for {email}.")

    return redirect('/')
