from django.test import TestCase
from django.test import LiveServerTestCase
from links.models import Link, Tag
from links import views
# Create your tests here.

class LinksApp(LiveServerTestCase):

    def setUp(self):
        # Create Links
        self.redux_link = Link.objects.create(
            title='Redux tutorial for beginners',
            url='https://www.valentinog.com/blog/redux'
        )
        self.redux_tag = Tag.objects.create(tag='redux')
        self.javascript_tag = Tag.objects.create(tag='javascript')
        self.redux_link.tags.add(self.redux_tag)
        self.redux_link.tags.add(self.javascript_tag)
        self.djangorest_link = Link.objects.create(
            title='Tutorial: Django REST with React (Django 2.0 and a sprinkle of testing)',
            url='https://www.valentinog.com/blog/tutorial-api-django-rest-react/'
        )
        self.djangorest_link.tags.add(self.javascript_tag)

    def test_get_list_of_related_links(self):
        views.index('redux')
