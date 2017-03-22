# dkPyTalk
The Internet of Swings for Code &amp; Supply on March 22nd

## You are presently on Step 0
In Step 0, we will:
1. I'm running Python 2.7.13 - this may work as is on Python 3
   * Mea culpa: Some machine learning libraries have dependencies on Python 2
2. Set up our virtual environment
   * `mkvirtualenv dkPyTalk`
   * `workon dkPyTalk`
3. Install our required libraries
   * `pip install django matplotlib numpy`
4. Build the scaffolding for the django project
   * `django-admin startproject internetOfSwings .`
5. Test that [everything checks out](http://localhost:8000)
   * `python manage.py runserver`