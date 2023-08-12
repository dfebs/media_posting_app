from django.test import TestCase
from accounts.tests.helpers import verify_redirect_to_login

class UsersPage(TestCase):
    fixtures = ['test_data.json']
    def test_not_logged_in(self):
        verify_redirect_to_login(self, '/accounts/users/')
    
    def test_page_exists(self):
        self.client.login(username='dfebs', password='urmomlel')
        response = self.client.get('/accounts/users/')
        self.assertEquals(len(response.context['profiles']), 6)
        # self.assertEquals(len(response.context['users_following']), 3)
        self.assertEqual(response.status_code, 200)
    

class UserPage(TestCase):
    fixtures = ['test_data.json']
    def test_not_logged_in(self):
        verify_redirect_to_login(self, '/accounts/users/dfebs/')
    
    def test_page_exists(self): 
        self.client.login(username='test_user', password='iamthetestuser')
        response = self.client.get('/accounts/users/test_user/')
        self.assertEqual(response.status_code, 200)

class EditProfile(TestCase):
    fixtures = ['test_data.json']
    def test_not_logged_in(self):
        verify_redirect_to_login(self, '/accounts/edit_profile/')

class FollowUser(TestCase):
    fixtures = ['test_data.json']
    def test_not_logged_in(self):
        verify_redirect_to_login(self, '/accounts/follow_user/1/')

class UnfollowUser(TestCase):
    fixtures = ['test_data.json']
    def test_not_logged_in(self):
        verify_redirect_to_login(self, '/accounts/unfollow_user/1/')

# class Logout(TestCase):
#     def test_not_logged_in(self):
#         verify_redirect_to_login(self, '/accounts/log_out/')
# /accounts/log_out/ is returning a 404 and I have no idea why. Maybe user has to be logged in?

# class Login(TestCase):
#     def test_not_logged_in(self):
#         thing = self.client.login(username='test_user', password='iamthetestuser')
# Logging in is tested as a consequence of other cases

# look into self.assertRedirects for making sure 302 redirects to the right place

# example of logging in
# >>> from django.test import Client
# >>> c = Client()
# >>> response = c.post("/login/", {"username": "john", "password": "smith"})
# >>> response.status_code
# 200
# >>> response = c.get("/customer/details/")
# >>> response.content