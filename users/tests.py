from datetime import datetime
from django.test import TestCase
from users.templatetags.user_templatetags import is_allowed, BizzFuzz
from .models import MyUser as User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            username='testusername',
            email='testuseremail@test.com',
            first_name='testfirstname',
            last_name='testlstname',
            birthday=datetime.strptime('1992-11-11', '%Y-%m-%d'),
            is_active=True,
        ),
        User.objects.create(
            username='testusername1',
            email='testuseremail1@test.com',
            first_name='testfirstname1',
            last_name='testlstname1',
            birthday=datetime.strptime('2011-12-12', '%Y-%m-%d'),
            is_active=True,
        ),
        User.objects.create(
            username='testusername2',
            email='testuseremail2@test.com',
            first_name='testfirstname2',
            last_name='testlstname2',
            birthday=datetime.strptime('2011-12-11', '%Y-%m-%d'),
            is_active=True,
        )

    def test_is_allowed(self):
        user1 = User.objects.get(username='testusername')
        user2 = User.objects.get(username='testusername1')

        self.assertEqual(is_allowed(user1.birthday), 'Allowed')
        self.assertEqual(is_allowed(user2.birthday), 'Blocked')

    def test_BizzFuzz(self):
        user1 = User.objects.get(username='testusername')
        user2 = User.objects.get(username='testusername1')
        user3 = User.objects.get(username='testusername2')
        user1.random_number = 40
        user2.random_number = 36
        user3.random_number = 30
        self.assertEqual(BizzFuzz(user1.random_number), 'Fuzz')
        self.assertEqual(BizzFuzz(user2.random_number), 'Bizz')
        self.assertEqual(BizzFuzz(user3.random_number), 'BizzFuzz')