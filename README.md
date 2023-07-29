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

## Features planned
- [ ] Follow users and see only their posts
- [ ] Make reactions on posts (ideally with ajax)
- [ ] Full email authentication
- [ ] Make things look nicer using bootstrap's layout system
- [ ] Automated testing

## Nice to haves
- [ ] Have feed update on-the-fly when a different user makes a post
- [ ] Lazy loading posts

## Instructions for running locally
1. Creating a virtual environment and activating it
2. Installing the dependencies in the requirements.txt `python -m pip install -r requirements.txt`
3. Migrating with `python manage.py migrate` so that the database is functional
4. Running the django app with `python manage.py runserver`.


