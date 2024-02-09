from django.test import TestCase
from ..models import Todo
# Create your tests here.

class TodoTestCase(TestCase):
    def setUp(self):
        Todo.objects.create(title="Run",details="go jugging and exercice")
        Todo.objects.create(title="Study",details="Study for the next exam")
    def testTodoDetails(self):
        run = Todo.objects.get(title="Run")
        expected_object_name = f'{run.details}'
        self.assertEqual(expected_object_name, 'go jugging and exercice')
    def testTodoCheck(self):
        run = Todo.objects.get(title="Study")
        expected_object_name = f'{run.checked}'
        self.assertEqual(expected_object_name, 'False')
        