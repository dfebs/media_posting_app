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
- [x] Make things look nicer using bootstrap's layout system (All layouts can be better, but I am happy with the layout I created. It even supports mobile!)
## Features planned
- [ ] Be able to delete comments
- [ ] Make reactions on posts (ideally with fetch)
- [ ] Full email authentication
- [ ] Product Level testing (probably with selenium)
- [ ] Unit Testing

## Nice to haves
- [ ] Sidebar that appears automatically on desktop, hamburger menu on mobile
- [ ] Have feed update on-the-fly when a different user makes a post
- [ ] Lazy loading posts
- [ ] Make template components more reusable. Currently, the feed and profiles have the same post list but both have to be updated separately. [This may be of use.](https://stackoverflow.com/questions/9472034/how-to-make-a-reusable-template-in-django)
- [ ] Use a modal to ask people if they're sure they want to delete a post

## Instructions for running locally
1. Create a virtual environment and activate it
2. Install the dependencies in the requirements.txt `python -m pip install -r requirements.txt`
3. Migrate with `python manage.py migrate` so that the database is functional
4. Run the django app with `python manage.py runserver`.


