# dkPyTalk
The Internet of Swings for Code &amp; Supply on March 22nd

## You are presently on Step 3
In Step 3, we will:
1. Apply a SQL migration in Django
   * Be sure to run `python manage.py makemigrations internetOfSwings`
   * Diamond Kinetics' installation does not rely on migrations (see note below)
   * Then add in some test data to the migration
2. Add some data and start using the QuerySet API!
   * There is some small amount of magic that must be applied before using Python Console in PyCharm
   * Same magic that `python manage.py shell` does

Heads up on Django here - it expects to have write access to your database and will fail any tests if it can't manage migrations on your behalf. Turning this behavior off isn't well documented. In general, it assumes it is the primary client of the database and doesn't always play nicely with others in this regard.
* I had to do quite a bit of gymnastics to get it to stop caring about the `django_migrations` table.
* Inside the inner `class Meta` you can add [`managed = False`](https://docs.djangoproject.com/en/1.10/ref/models/options/#managed) to turn off table creation/deletion for this model - but not overall.

## Compare a previous step to this step
* [Step 2](https://github.com/mressler/dkPyTalk/compare/step-2...step-3)
* [Step 1](https://github.com/mressler/dkPyTalk/compare/step-1...step-3)
* [Step 0](https://github.com/mressler/dkPyTalk/compare/step-0...step-3)