from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse



class SignUpPageTest(TestCase):
    def test_signup_page_form(self):
        data1 = {
            'username':'jack',
            'password1':'S10011001sh',
            'password2':'S10011001sh',
            'age':23,
            'phone_number':'7484950'

        }
        res = self.client.post(reverse('signup'),data=data1)
        self.assertEqual(res.status_code,302)

    def test_model_signup(self):
        user = get_user_model().objects.create_user(
            'jack',
            'jack@jack.com',
        )
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,'jack')
        self.assertEqual(get_user_model().objects.all().last().username,'jack')