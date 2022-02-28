from django import forms
from django.forms import ModelForm
from owner.models import Books
from owner.models import Employee


class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
        widgets = {
            "book_name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"}),
            "published_date": forms.DateInput(attrs={"class": "form-control","type":"date"}),
            # "image": forms.FileInput(attrs={"class": "form-control"}),

        }

    # book_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # author_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # price = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # copies = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")
        copies = cleaned_data.get("copies")
        if int(price) < 0:
            message = "invalid value"
            self.add_error("price", message)
        if int(copies) < 0:
            message = "invalid value"
            self.add_error("copies", message)

# class EmployeeForm(ModelForm):
#     class Meta:
#         model = Employee
#         fields = "__all__"
#
#     def clean(self):
#         cleaned_data = super().clean()
#         employee_name = cleaned_data.get("employee_name")
#         designation = cleaned_data.get("designation")
#         salary = cleaned_data.get("salary")
#         experience = cleaned_data.get("experience")
