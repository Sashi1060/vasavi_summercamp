from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import EnquiryForm


def home(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("summercamp:thank_you"))
    else:
        form = EnquiryForm()

    return render(request, "summercamp/home.html", {"form": form})


def thank_you(request):
    return render(request, "summercamp/thank_you.html")
