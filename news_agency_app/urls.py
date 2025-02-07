from . import views
from django.urls import path

from news_agency_app.views import TopicCreateView, TopicUpdateView

urlpatterns = [
    path("", views.index, name="index"),
    path("newspapers/", views.NewspaperListView.as_view(), name="newspaper-list"),
    path(
        "newspapers/<int:pk>/",
        views.NewspaperDetailView.as_view(),
        name="newspaper-detail",
    ),
    path(
        "newspapers/create/",
        views.NewspaperCreateView.as_view(),
        name="newspaper-create",
    ),
    path(
        "newspapers/<int:pk>/update/",
        views.NewspaperUpdateView.as_view(),
        name="newspaper-update",
    ),
    path(
        "newspapers/<int:pk>/delete/",
        views.NewspaperDeleteView.as_view(),
        name="newspaper-delete",
    ),
    path("topics/", views.TopicListView.as_view(), name="topic-list"),
    path("topics/<int:pk>/", views.TopicDetailView.as_view(), name="topic-detail"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/<int:pk>/update/", TopicUpdateView.as_view(), name="topic-update"),
    path("redactors/", views.RedactorListView.as_view(), name="redactor-list"),
    path(
        "redactors/<int:pk>/",
        views.RedactorDetailView.as_view(),
        name="redactor-detail",
    ),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
]

app_name = "news_agency_app"
