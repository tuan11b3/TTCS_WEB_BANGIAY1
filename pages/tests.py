from django.test import SimpleTestCase # is subset of TestCase
from django.urls import reverse, resolve # use for testing URLS

from .views import HomePageView # new

# Create your tests here.
class HomepagesTests(SimpleTestCase):


    # SETUP METHOD, that will run before every test
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)


    # TEST FOR STATUS OF URLS
    def test_homepage_status_code(self):
        # response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200) # 200 means that it exists

    # def test_homepage_url_name(self):
    #     response = self.client.get(reverse('home'))
    #     self.assertEqual(response.status_code, 200)
    
    # TEST TEMPLATES
    def test_homepage_template(self): #new
        # response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'home.html')

    # TEST HTML
    def test_homepage_contains_correct_html(self): # new
        # response = self.client.get('/')
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self): # new
        # response = self.client.get('/')
        self.assertNotContains(self.response, 'Hi there! I should no be on the page.')
    
    # TEST RESOLVE
    def test_homepage_url_resolves_homepageview(self):  #new
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
# for to test on pages using
        # python manage.py test pages
