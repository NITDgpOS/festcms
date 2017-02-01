from django.test import TestCase
from festflow.models import About


class AboutTestCase(TestCase):

    def setUp(self):
        About.objects.create(identifier='thisIsValidIdentifier',
                             content='<p>Rich Text Content<p>')

    def test_about_model(self):
        """Animals that can speak are correctly identified"""
        obj = About.objects.get(identifier="thisIsValidIdentifier")
        self.assertEqual(str(obj), 'thisIsValidIdentifier')
        self.assertEqual(obj.content, '<p>Rich Text Content<p>')
