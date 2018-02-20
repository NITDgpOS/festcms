from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from django.test import TestCase


class IndexTest(TestCase):

    def setUp(self):
        # Setup a client.
        self.client = Client()

    def test_basic(self):
        """
        Test if the view is working atall or not
        """

        # Issue a GET request.
        url = reverse('index')
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


class LoginTest(TestCase):

    def setUp(self):
        # Setup a client.
        self.client = Client()

        # Setup a user
        self.test_user = User.objects.create_user('testuser',
                                                  'test@test.com',
                                                  'testpass')

    def test_basic(self):
        """
        Test if the view is working atall or not
        """

        # Issue a GET request.
        url = reverse('login_page')
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Login as user
        self.client.login(username='testuser', password='testpass')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.test_user.delete()


class AboutTest(TestCase):

    def setUp(self):
        # Setup a client.
        self.client = Client()

    def test_basic(self):
        """
        Test if the view is working atall or not
        """

        # Issue a GET request.
        url = reverse('about')
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


class SponsorsTest(TestCase):

    def setUp(self):
        # Setup a client.
        self.client = Client()

    def test_basic(self):
        """
        Test if the view is working atall or not
        """

        # Issue a GET request.
        url = reverse('sponsors')
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


class ContactTest(TestCase):

    def setUp(self):
        # Setup a client.
        self.client = Client()

    def test_basic(self):
        """
        Test if the view is working atall or not
        """

        # Issue a GET request.
        url = reverse('contact')
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


class EventsTest(TestCase):

    def setUp(self):
        # Setup a client.
        self.client = Client()

    def test_basic(self):
        """
        Test if the view is working atall or not
        """

        # Issue a GET request.
        url = reverse('events')
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


class KeynotesTest(TestCase):

    def setUp(self):
        # Setup a client.
        self.client = Client()

    def test_basic(self):
        """
        Test if the view is working atall or not
        """

        # Issue a GET request.
        url = reverse('keynotes')
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


class ReachUsTest(TestCase):

    def setUp(self):
        # Setup a client.
        self.client = Client()

    def test_basic(self):
        """
        Test if the view is working atall or not
        """

        # Issue a GET request.
        url = reverse('reachus')
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


class FaqTest(TestCase):

    def setUp(self):
        # Setup a client.
        self.client = Client()

    def test_basic(self):
        """
        Test if the view is working atall or not
        """

        # Issue a GET request.
        url = reverse('FAQ')
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


class SubscribeTest(TestCase):

    def setUp(self):
        # Setup a client.
        self.client = Client()

    def test_basic(self):
        """
        Test if the view is working atall or not
        """

        # Issue a GET request.
        url = reverse('subscribe')
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
