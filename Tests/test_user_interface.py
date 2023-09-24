import unittest
from unittest.mock import patch
from io import StringIO
from User_interface import display_menu

class TestDisplayMenu(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)  # Capture printed output
    def test_display_menu(self, mock_stdout):
        # Call the function and capture printed output
        display_menu()

        # Get the captured output
        result = mock_stdout.getvalue()

        # Verify that the menu is displayed correctly
        expected_output = """========== Pharmacy Inventory Management ==========
        1. Add Medicine
        2. View Medicines
        3. View Medicines Expiring Soon
        4. Update Expiry Date
        5. Update Quantity
        6. Delete Medicine
        7. Search Medicine
        8. Check Alerts
        9. Exit
        Enter your choice (1/2/3/4/5/6/7/8): """

        self.assertEqual(result, expected_output)
    def test_add_medicine(self)
        inputs = ["1" "Medicine1", "12345", "10", "2023-12-31"]
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                display_menu()

        result = mock_stdout.getvalue()

    
        

if __name__ == '__main__':
    unittest.main()
