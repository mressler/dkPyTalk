from django.db import models


class User(models.Model):
    # Hugely important to Django that you include a field marked a primary_key=True
    userId = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=50)

    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    profileImageUrl = models.CharField(max_length=120, null=True)

    class Meta:
        db_table = 'users'
        default_related_name = db_table
        app_label = 'internetOfSwings'

    def __str__(self):
        return "%s %s (%s)" % (self.firstName, self.lastName, self.email)


class Swing(models.Model):
    swing = models.IntegerField(primary_key=True)

    # Relate back to the owning User
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        db_column='user'
    )

    data = models.TextField()

    # Representative metric placeholder
    batSpeed = models.FloatField(null=True)

    class Meta:
        db_table = 'swings'
        default_related_name = db_table
        app_label = 'internetOfSwings'
