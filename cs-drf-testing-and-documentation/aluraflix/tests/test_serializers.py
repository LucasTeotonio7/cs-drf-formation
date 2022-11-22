from django.test import TestCase

from aluraflix.models import Program
from aluraflix.serializers import ProgramSerializer


class ProgramSerializerTestCase(TestCase):

    def setUp(self) -> None:
        self.program = Program(
            title='Test program',
            release_date='2016-07-15',
            type="F",
            likes=1000,
            dislikes=100
        )
        self.serializer = ProgramSerializer(instance=self.program)

    def test_check_serializer_fields(self):
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()), 
            set(['title', 'type', 'release_date', 'likes', 'dislikes'])
        )
