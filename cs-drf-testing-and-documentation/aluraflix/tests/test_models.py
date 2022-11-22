from django.test import TestCase

from aluraflix.models import Program


class ProgramModelTestCase(TestCase):

    def setUp(self) -> None:
        self.program = Program(
            title='Test program',
            release_date='2016-07-15',
        )
    
    def test_fields_model_program(self):
        self.assertEqual(self.program.title, 'Test program')
        self.assertEqual(self.program.type, 'F')
        self.assertEqual(self.program.release_date, '2016-07-15')
        self.assertEqual(self.program.likes, 0)
        self.assertEqual(self.program.dislikes, 0)
