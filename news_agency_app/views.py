from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from news_agency_app.models import Topic, Newspaper, Redactor


def index(request):
    """View function for the home page of the site with visit count."""

    request.session["num_visits"] = request.session.get("num_visits", 0) + 1
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()

    context = {
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
        "num_redactors": num_redactors,
        "num_visits": request.session["num_visits"],
    }

    return render(request, "news_agency/index.html", context=context)


class TopicListView(ListView):
    model = Topic
    template_name = "news_agency/topic_list.html"
    context_object_name = "topics"


class TopicDetailView(DetailView):
    model = Topic
    template_name = "news_agency/topic_detail.html"


class TopicCreateView(CreateView):
    model = Topic
    fields = ["name"]
    template_name = "news_agency/topic_form.html"
    success_url = reverse_lazy("news_agency:topic_list")


class TopicUpdateView(UpdateView):
    model = Topic
    template_name = "news_agency/topic_form.html"
    fields = ["name"]
    success_url = reverse_lazy("news_agency:topic-list")


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


class RedactorListView(ListView):
    model = Redactor
    template_name = "news_agency/redactor_list.html"
    context_object_name = "redactors"


class RedactorDetailView(DetailView):
    model = Redactor
    template_name = "news_agency/redactor_detail.html"


class CustomLoginView(LoginView):
    template_name = "registration/login.html"


class CustomLogoutView(LogoutView):
    template_name = "registration/logged_out.html"


class SearchListView(generic.ListView):
    search_fields = []

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")

        if search:
            q_objects = Q()
            for field in self.search_fields:
                q_objects |= Q(**{f"{field}__contains": search})
            queryset = queryset.filter(q_objects)

        return queryset
