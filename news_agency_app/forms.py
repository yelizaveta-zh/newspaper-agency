from django import forms

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
