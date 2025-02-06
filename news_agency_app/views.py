from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from news_agency_app.models import Topic, Newspaper


class TopicListView(ListView):
    model = Topic
    template_name = "news_agency/topic_list.html"
    context_object_name = "topics"


class NewspaperListView(ListView):
    model = Newspaper
    template_name = "news_agency/newspaper_list.html"
    context_object_name = "newspapers"


class NewspaperDetailView(DetailView):
    model = Newspaper
    template_name = "news_agency/newspaper_detail.html"


class NewspaperCreateView(CreateView):
    model = Newspaper
    fields = ["title", "content", "published_date", "topic", "publishers"]
    template_name = "news_agency/newspaper_form.html"
    success_url = reverse_lazy("newspaper-list")


class NewspaperUpdateView(UpdateView):
    model = Newspaper
    fields = ["title", "content", "published_date", "topic", "publishers"]
    template_name = "news_agency/newspaper_form.html"
    success_url = reverse_lazy("newspaper-list")


class NewspaperDeleteView(DeleteView):
    model = Newspaper
    template_name = "news_agency/newspaper_confirm_delete.html"
    success_url = reverse_lazy("newspaper-list")
