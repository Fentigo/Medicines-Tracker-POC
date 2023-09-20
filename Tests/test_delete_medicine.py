import unittest
import io
from unittest.mock import patch
from Modules.delete import delete_medicine  # Adjust the import path

class TestDeleteMedicine(unittest.TestCase):

    def test_delete_medicine_confirm_yes(self):
        # Simulate user input to confirm deletion (Y)
        inputs = ["6", "Y"]
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                delete_medicine()

        result = mock_stdout.getvalue()

        # Assert that the function produced the expected output
        self.assertIn("Medicine has been deleted successfully!", result)

    def test_delete_medicine_confirm_no(self):
        # Simulate user input to cancel deletion (N)
        inputs = ["2", "N"]
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                delete_medicine()

        result = mock_stdout.getvalue()

        # Assert that the function produced the expected output
        self.assertIn("Closing the connection now.", result)

    def test_delete_medicine_invalid_id(self):
        # Simulate user input with an invalid ID
        inputs = ["1001"]
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                delete_medicine()

        result = mock_stdout.getvalue()

        # Assert that the function produced an error message for invalid input
        self.assertIn("No medicine found with ID 1001", result)

if __name__ == '__main__':
    unittest.main()
