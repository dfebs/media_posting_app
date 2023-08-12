def verify_redirect_to_login(test_case, destination):
    response = test_case.client.get(destination, follow=True)
    test_case.assertRedirects( response, f'/accounts/login/?next={destination}')