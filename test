import unittest
import io
from unittest.mock import patch
from Modules.add_medicine import add_medicine

class TestAddMedicine(unittest.TestCase):

    def test_add_medicine_valid_input(self):
        inputs = ["Medicine1", "12345", "10", "2023-12-31"]
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                add_medicine()

        result = mock_stdout.getvalue()

        # Assert that the function produced the expected output
        self.assertEqual(result, "Enter the following information\nMedicine has been added successfully!\n")

    def test_add_medicine_invalid_input(self):
        # Simulate invalid user input for the function
        inputs = ["Invalid", "12345", "abc", "2023-12-31"]
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                add_medicine()

        # Capture the printed output
        result = mock_stdout.getvalue()

        # Assert that the function produced an error message for invalid input
        self.assertIn("Invalid input. Please enter valid details", result)

if __name__ == '__main__':
    unittest.main()
