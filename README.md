# dkPyTalk
The Internet of Swings for Code &amp; Supply on March 22nd

## You are presently on Step 3
In Step 3, we will:
1. Apply a SQL migration in Django and start using the QuerySet API
2. Add some data!

Heads up on Django here - it expects to have write access to your database and will fail tests if it can't manage migrations on your behalf. Turning this behavior off isn't well documented. In general, it assumes it is the primary client of the database and doesn't always play nicely with others in thie regard.
* I had to do quite a bit of gymnastics to get it to stop caring about the django_migrations table.
* Inside the inner `class Meta` you can add [`managed = False`](https://docs.djangoproject.com/en/1.10/ref/models/options/#managed) to turn off table creation/deletion for this model - but not overall.

## Compare a previous step to this step
* [Step 2](https://github.com/mressler/dkPyTalk/compare/step-2...step-3)
* [Step 1](https://github.com/mressler/dkPyTalk/compare/step-1...step-3)
* [Step 0](https://github.com/mressler/dkPyTalk/compare/step-0...step-3)