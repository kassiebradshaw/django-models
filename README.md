# Lab 27 - Django Models

*Author*: Kassie Bradshaw

[Link to my Pull Request](tbd)

---

## Overview

Django has a powerful Object Relational Mapper (ORM) that allows us to persist data using Python instead of SQL. Today you'll build out a project with one model and wire up that model using Django Views.

---

## Feature Tasks & Requirements

**Model**:

* [ ] Create `snack_tracker_project` project
* [ ] Create `snacks` app
* [ ] Add `snacks` app to project
* [ ] Create `snack` model
  * [ ] Make sure it extends from proper base class
  * [ ] Add `name` as a CharField with maximum length of 64 characters
  * [ ] Add `purchaser` ForeignKey related to Django's built-in user model with CASCADE delete option.
    * `from django.contrib.auth import get_user_model`
  * [ ] Add `description` TextField
* [ ] Add model to admin
* [ ] Modify `snack` model to have user-friendly display in admin
* [ ] Create migrations and migrate data
* [ ] Create a super user
* [ ] Run development server
* [ ] Add a few snacks via Admin panel
* [ ] Create another user and more snacks via Admin panel
* [ ] Confirm snacks behave as expected with proper name, purchaser and description

**Views for Snacks App**:

* [ ] Create `SnackListView`
  * [ ] Extend `ListView`
  * [ ] Give a template of `snack_list.html`
  * [ ] Associate `Snack` model

* [ ] Update URL patterns for project
  * [ ] Empty path should `include` snacks.urls

* [ ] Update Snacks app urls
  * [ ] Empty sub-path should be handled by SnackListView
    * [ ] Don't forget to use `as_view()`

* [ ] Add detail view
  * [ ] Link `snack_detail.html` template
  * [ ] Associate `Snack` model

* [ ] Update app urlpatterns to handle detail view
  * [ ] Account for primary key in url
  * [ ] Path would look like `localhost:8000/1/` to get to snack with id of 1

**Templates**:

* [ ] Add `templates` folder in root of project
  * [ ] Register `templates` folder in project settings TEMPLATES section

* [ ] Create `base.html` ancestor template
  * [ ] Add main html document
  * [ ] Use `Django Templating Language` to allow child templates to insert content

* [ ] Create `snack_list.html` template
  * [ ] Extend base template
  * [ ] Use `Django Templating Language` to display each snack's name

* [ ] View home page (aka snack_list) and confirm snacks showing properly
* [ ] Create `snack_detail.html` template
  * [ ] Template should extend base
  * [ ] Content should display snack's name, description, and purchaser.

* [ ] Add link in snack_list template to related detail page for each snack
* [ ] Add a link back to Home (aka snack_list) page from detail page.

---

## User Acceptance Tests

* [ ] Test snack pages
  * [ ] **NOTE** - make sure test extends `TestCase` instead of `SimpleTestCase` used in previous class
  * [ ] Verify status code
  * [ ] Verify correct template use
  * [ ] Use URL *name* instead of hard coded path
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
* [ ] Test Snack model
* [ ] Add multiple models
* [ ] Use an alternate test runner
* [ ] Add more advanced fields to the models, e.g. created time stamp

