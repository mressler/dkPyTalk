from django.test import TestCase
from internetOfSwings import models


class CSVTests(TestCase):

    def test_sime_parse(self):
        someSwing = models.Swing.objects.all()[0]
        someSwing.get_data_as_matrix()

