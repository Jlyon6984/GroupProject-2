import unittest
from unittest.mock import patch, mock_open
import json
from io import StringIO

# Import the functions from Project2.py (replace 'Project2' with the actual filename)
from Project2 import add_task, delete_task, mark_task_done, show_tasks, load_tasks, save_tasks

class TestTodoApp(unittest.TestCase):
    
    # Mocking load_tasks function to start with a predefined list of tasks
    @patch('builtins.open', new_callable=mock_open, read_data='[{"task": "Test task", "done": false}]')
    def test_load_tasks(self, mock_file):
        tasks = load_tasks()  # Should load the task from the mock file
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['task'], 'Test task')
        self.assertFalse(tasks[0]['done'])

    # Test adding a task to the list
    @patch('builtins.input', return_value="New task")  # Mock input for task description
    @patch('builtins.open', new_callable=mock_open)
    def test_add_task(self, mock_file, mock_input):
        tasks = []
        add_task(tasks)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['task'], 'New task')
        self.assertFalse(tasks[0]['done'])

    # Test showing tasks
    @patch('sys.stdout', new_callable=StringIO)  # Redirect stdout to capture print output
    def test_show_tasks(self, mock_stdout):
        tasks = [{"task": "Task 1", "done": False}, {"task": "Task 2", "done": True}]
        show_tasks(tasks)
        output = mock_stdout.getvalue().strip()
        self.assertIn("1. Task 1 - Not Done", output)
        self.assertIn("2. Task 2 - Done", output)

    # Test marking task as done
    @patch('builtins.input', return_value='1')  # Mock input to select task 1
    @patch('builtins.open', new_callable=mock_open)
    def test_mark_task_done(self, mock_file, mock_input):
        tasks = [{"task": "Task 1", "done": False}]
        mark_task_done(tasks)
        self.assertTrue(tasks[0]['done'])  # Task should be marked as done

    # Test deleting a task
    @patch('builtins.input', return_value='1')  # Mock input to delete task 1
    @patch('builtins.open', new_callable=mock_open)
    def test_delete_task(self, mock_file, mock_input):
        tasks = [{"task": "Task 1", "done": False}]
        delete_task(tasks)
        self.assertEqual(len(tasks), 0)  # Task list should now be empty after deletion

if __name__ == "__main__":
    unittest.main()
