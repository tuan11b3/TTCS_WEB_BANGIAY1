from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve


from .forms import CustomUserCreationForm
from .views import SignupPageView
# Create your tests here.
# No longer need any
# class CustomUserTests(TestCase):
    
#     def test_create_user(self): 
#         User = get_user_model()
#         user = User.objects.create_user(
#             username = 'tuan11b3',
#             email= 'tuan11b32001@gmail.com',
#             password='testpass123'
#         )
#         self.assertEqual(user.username, 'tuan11b3')
#         self.assertEqual(user.email, 'tuan11b32001@gmail.com')
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_superuser)

#     def test_create_superuser(self):
#         User = get_user_model()
#         admin_user = User.objects.create_superuser(
#             username='superadmin',
#             email='superadmin@gmail.com',
#             password='testpass123'
#         )
#         self.assertEqual(admin_user.username, 'superadmin')
#         self.assertEqual(admin_user.email, 'superadmin@gmail.com')
#         self.assertTrue(admin_user.is_active)
#         self.assertTrue(admin_user.is_staff)
#         self.assertTrue(admin_user.is_superuser)

# class SignUpTest(TestCase):

#     def setUp(self):
#         url = reverse('signup')
#         self.response = self.client.get(url)

#     def test_signup_template(self):
#         self.assertEqual(self.response.status_code, 200) # Check url status 
#         self.assertTemplateUsed(self.response, 'signup.html') # Check templates
#         self.assertContains(self.response, 'Sign Up') # Check include & exclude
#         self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

#     # test for signup form
#     def test_signup_form(self):
#         form = self.response.context.get('form')
#         self.assertIsInstance(form, CustomUserCreationForm)
#         self.assertContains(self.response, 'csrfmiddlewaretoken')


    # # test for signup view
    #     view = resolve('/accounts/signup/')
    #     self.assertEqual(view.func.__name__,SignupPageView.as_view().__name__)
        
# New Sigup Test
class SignupTests(TestCase):    # new

    username = 'newuser'
    email = 'newuser@gmail.com'
    
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200) # 200 page exist
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi ther! I should not be on the pag.')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
