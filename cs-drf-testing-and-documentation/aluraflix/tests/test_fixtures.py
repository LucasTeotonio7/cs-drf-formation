from django.test import TestCase
from aluraflix.models import Program


class FixtureDataTestCase(TestCase):

    fixtures = ['initials_programs']

    def test_fixture_loading(self):
        first_programa = Program.objects.get(pk=1)
        all_programs = Program.objects.all()
        self.assertEqual(first_programa.title, 'Coisas bizarras')
        self.assertEqual(len(all_programs), 9)
