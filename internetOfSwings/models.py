import csv
import StringIO
import numpy as np
from matplotlib import pyplot as plt
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

    def get_data_as_matrix(self):
        reader = csv.reader(StringIO.StringIO(self.data), delimiter=',')
        matrix = [row for row in reader]

        return np.matrix(matrix)

    def plot_to_file(self, file_obj):
        matrix = self.get_data_as_matrix()
        time = matrix[:, 0]
        accel = matrix[:, (1, 2, 3)]
        gyro = matrix[:, (4, 5, 6)]

        fig = plt.figure(figsize=(14, 14))
        fig.subplots_adjust(hspace=.5)
        plt1 = fig.add_subplot(2, 1, 1)
        plt1.plot(time, accel)
        plt1.legend(['X', 'Y', 'Z'])
        plt1.set_xlabel('Time (microseconds)')
        plt1.set_ylabel('Accel (G)')
        plt.title('Accelerometer Data')

        plt1 = fig.add_subplot(2, 1, 2)
        plt1.plot(time, gyro)
        plt1.legend(['X', 'Y', 'Z'])
        plt1.set_xlabel('Time (microseconds)')
        plt1.set_ylabel('Rotation Rate (rad/s)')
        plt.title('Gyroscope Data')

        fig.savefig(file_obj, format="png")

        return fig
