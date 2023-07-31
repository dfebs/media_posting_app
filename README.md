# Media Posting App with Django
This repository is a practice application that is under construction. It is an attempt at learning the Django library from top to bottom.

## Current features
- [x] Basic login/logout system
- [x] Make posts with images
- [x] Make comments on posts
- [x] Delete your own posts
- [x] See all listed users
- [x] See user profiles
- [x] Edit own user profile
- [x] Follow users and see only their posts
- [x] Add follow button to user list
- [x] Encourage user that isn't following users to follow users (perhaps use a jumbotron, cause jumbotrons are cool **Edit: A jumbotron was used**)
## Features planned

- [ ] Make reactions on posts (ideally with fetch)
- [ ] Full email authentication
- [ ] Make things look nicer using bootstrap's layout system
- [ ] Automated testing

## Nice to haves
- [ ] Sidebar that appears automatically on desktop, hamburger menu on mobile
- [ ] Have feed update on-the-fly when a different user makes a post
- [ ] Lazy loading posts

## Instructions for running locally
1. Create a virtual environment and activate it
2. Install the dependencies in the requirements.txt `python -m pip install -r requirements.txt`
3. Migrate with `python manage.py migrate` so that the database is functional
4. Run the django app with `python manage.py runserver`.


