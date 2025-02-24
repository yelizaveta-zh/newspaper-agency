from django import forms
from django.contrib.auth.models import User

from news_agency_app.models import Newspaper, Redactor, Topic


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=Redactor.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Newspaper
        fields = ["title", "content", "published_date", "topic", "publishers"]


class RedactorExperienceUpdateForm(forms.ModelForm):
    years_of_experience = forms.IntegerField(min_value=0)

    class Meta:
        model = Redactor
        fields = ["years_of_experience"]


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["name"]


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error("password_confirm", "Passwords do not match")

        return cleaned_data
