from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from checkout.models import Order

from .models import UserProfile
from .forms import UserProfileForm, UpdateIndividualForm


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please ensure the form is valid.'
            )
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def profile_update(request):
    """
    View for updating a users information
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        individual_form = UpdateIndividualForm(
            request.POST, request.FILES, instance=profile
        )

        if form.is_valid() and individual_form.is_valid():
            form.save()
            individual_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile")
        else:
            messages.error(
                request,
                "Update failed. Please ensure the form is valid."
            )

    else:
        form = UserProfileForm(instance=profile)
        individual_form = UpdateIndividualForm(instance=profile)

    context = {
        "individual_form": individual_form,
        "orders": orders,
        "form": form,
    }
    return render(request, "profiles/profile_update.html", context)


@login_required
def profile_delete(request, pk):
    """
    Deletion of a user profile
    """
    user = get_object_or_404(User, id=pk)
    logout(request)
    user.delete()
    messages.warning(request, "Your account has been deleted")
    return redirect("home")


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
