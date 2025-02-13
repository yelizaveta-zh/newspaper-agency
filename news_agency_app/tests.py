from django.test import TestCase
from news_agency_app.models import Topic, Redactor, Newspaper
from django.contrib.auth import get_user_model
from datetime import datetime


class TopicModelTest(TestCase):
    def test_create_topic(self):
        topic = Topic.objects.create(name="Politics")
        self.assertEqual(str(topic), "Politics")


class RedactorModelTest(TestCase):
    def test_create_redactor(self):
        redactor = get_user_model().objects.create_user(
            username="editor1", password="password123"
        )
        self.assertEqual(str(redactor), "editor1")


class NewspaperModelTest(TestCase):
    def test_create_newspaper(self):
        topic = Topic.objects.create(name="Sports")
        redactor = get_user_model().objects.create_user(
            username="editor2", password="password123"
        )
        newspaper = Newspaper.objects.create(
            title="Big Match",
            content="Match details...",
            published_date=datetime.now(),
            topic=topic,
        )
        newspaper.publishers.add(redactor)

        self.assertEqual(str(newspaper), "Big Match")
        self.assertEqual(newspaper.topic.name, "Sports")
        self.assertIn(redactor, newspaper.publishers.all())
