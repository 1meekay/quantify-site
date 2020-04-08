from django.shortcuts import render, redirect
from .models import BusinessInfo
from .forms import BusinessForm
from django.contrib import messages


def view_all(request):
    all_businesses = BusinessInfo.objects.all()

    return render(
        request=request,
        template_name='businesses.html',
        context={
            'all_businesses': all_businesses
        }
    )


def add_new(request):
    filled_form = BusinessForm(request.POST)

    if filled_form.is_valid():
        filled_form.save()

        # if request.user.is_authenticated:
        #     instance = filled_form.save(commit=False)
        #     instance.author = request.user
        #     instance.save()
        # else:
        #     filled_form.save()

        messages.info(request=request, message="Business info added successfully.")

        return redirect(
            '/business/'
        )
    else:
        return render(
            request=request,
            template_name='new_business_form.html',
            context={
                'business_form': BusinessForm()
            }
        )


def individual_business(request, business_id):
    business = BusinessInfo.objects.get(id=business_id)

    return render(
        request=request,
        template_name='business_info.html',
        context={
            'business': business
        }
    )