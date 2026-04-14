from django import forms

from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ["name", "phone", "child_age", "batch", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Parent name"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone number"}
            ),
            "child_age": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Child age"}
            ),
            "batch": forms.Select(attrs={"class": "form-select"}),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Anything you'd like us to know",
                    "rows": 4,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["message"].required = False
