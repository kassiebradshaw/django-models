# Lab 27 - Django Models

*Author*: Kassie Bradshaw

[Link to my Pull Request](https://github.com/kassiebradshaw/django-models/pull/1)

---

## Overview

Django has a powerful Object Relational Mapper (ORM) that allows us to persist data using Python instead of SQL. Today you'll build out a project with one model and wire up that model using Django Views.

---

## Feature Tasks & Requirements

**Model**:

* [x] Create `snack_tracker_project` project
* [x] Create `snacks` app
* [x] Add `snacks` app to project
* [x] Create `snack` model
  * [x] Make sure it extends from proper base class
  * [x] Add `name` as a CharField with maximum length of 64 characters
  * [x] Add `purchaser` ForeignKey related to Django's built-in user model with CASCADE delete option.
    * `from django.contrib.auth import get_user_model`
  * [x] Add `description` TextField
* [x] Add model to admin
* [x] Modify `snack` model to have user-friendly display in admin
* [x] Create migrations and migrate data
* [x] Create a super user
* [x] Run development server
* [x] Add a few snacks via Admin panel
* [x] Create another user and more snacks via Admin panel
* [ ] Confirm snacks behave as expected with proper name, purchaser and description

**Views for Snacks App**:

* [x] Create `SnackListView`
  * [x] Extend `ListView`
  * [x] Give a template of `snack_list.html`
  * [x] Associate `Snack` model

* [x] Update URL patterns for project
  * [x] Empty path should `include` snacks.urls

* [x] Update Snacks app urls
  * [x] Empty sub-path should be handled by SnackListView
    * [x] Don't forget to use `as_view()`

* [x] Add detail view
  * [x] Link `snack_detail.html` template
  * [x] Associate `Snack` model

* [x] Update app urlpatterns to handle detail view
  * [x] Account for primary key in url
  * [x] Path would look like `localhost:8000/1/` to get to snack with id of 1

**Templates**:

* [x] Add `templates` folder in root of project
  * [x] Register `templates` folder in project settings TEMPLATES section

* [x] Create `base.html` ancestor template
  * [x] Add main html document
  * [x] Use `Django Templating Language` to allow child templates to insert content

* [x] Create `snack_list.html` template
  * [x] Extend base template
  * [x] Use `Django Templating Language` to display each snack's name

* [x] View home page (aka snack_list) and confirm snacks showing properly
* [x] Create `snack_detail.html` template
  * [x] Template should extend base
  * [x] Content should display snack's name, description, and purchaser.

* [x] Add link in snack_list template to related detail page for each snack
* [x] Add a link back to Home (aka snack_list) page from detail page.

---

## User Acceptance Tests

* [x] Test snack pages
  * [x] **NOTE** - make sure test extends `TestCase` instead of `SimpleTestCase` used in previous class
  * [x] Verify status code
  * [x] Verify correct template use
  * [x] Use URL *name* instead of hard coded path
    * **TIP**: `django.urls.reverse` will help with that

* [ ] We can't easily test `SnackDetailView` just yet.
  * Can you figure out why?

---

## Stretch Goals

* [ ] Add styling
  * [ ] Create static folder at root of project
  * [ ] Update STATICFILES_DIRS
  * [ ] Create base.css file which styles base.html elements
  * [ ] Load static css in base.html file

* [ ] Test SnackDetailView
* [x] Test Snack model
* [ ] Add multiple models
* [x] Use an alternate test runner
* [ ] Add more advanced fields to the models, e.g. created time stamp
