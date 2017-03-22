# dkPyTalk
The Internet of Swings for Code &amp; Supply on March 22nd

## You are presently on Step 1
In Step 1, we will:
1. Update the standard django project to map our own URLs
   * Create `apps.py`
   * Add this as an `INSTALLED_APP` in `settings.py`
   * Add a `views.py` to handle requests
   * Update `urls.py` to point to our `views.py` for default requests
2. Check that our JSON 'Hello World' checks out!
   * `python manage.py runserver`

Some commentary here - Django makes a big deal about the difference between _apps_ & _projects_ that I'm just glazing over completely here. For my needs, I haven't had to care a lot about the difference. So I just hack this _project_ into also being an _app_. <3

## Compare a previous step to this step
* [Step 0](https://github.com/mressler/dkPyTalk/compare/step-0...step-1)