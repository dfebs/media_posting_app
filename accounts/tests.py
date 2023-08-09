from django.test import TestCase

class UsersPage(TestCase):
    def test_not_logged_in(self):
        response = self.client.get('/accounts/users/')
        self.assertEqual(response.status_code, 302)

class UserPage(TestCase):
    def test_not_logged_in(self):
        response = self.client.get('/accounts/users/dfebs/')
        self.assertEqual(response.status_code, 302)

# look into self.assertRedirects for making sure 302 redirects to the right place

# example of logging in
# >>> from django.test import Client
# >>> c = Client()
# >>> response = c.post("/login/", {"username": "john", "password": "smith"})
# >>> response.status_code
# 200
# >>> response = c.get("/customer/details/")
# >>> response.content