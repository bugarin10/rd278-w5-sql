import unittest
import os
import polars
import sys
#As the module src is not in the test directory I'll append it

dir=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'src'))
sys.path.append(dir)
import source_code  # Import your source_code module correctly


def is_csv_file(file_path):
    # Extract the file extension from the file path
    file_extension = os.path.splitext(file_path)[-1].lower()
    return file_extension == ".csv"


class TestSourceCode(unittest.TestCase):
    """unit test class which will test source code"""

    def test_validity_output(self):
        data = polars.read_csv("pythonproject/src/data/median-income-by-country-2023.csv")
        result = type(source_code.descriptive_statistics(data))
        self.assertEqual(result, polars.dataframe.frame.DataFrame, msg='This is not the expected output')

    def test_csv_validity(self):
        valid_csv_path = "pythonproject/src/data/median-income-by-country-2023.csv"  # Replace with the path to a valid CSV file
        invalid_csv_path = "pythonproject/src/data/Test.docx"  # Replace with the path to an invalid CSV file

        self.assertTrue(is_csv_file(valid_csv_path), "Valid CSV file check failed.")
        self.assertFalse(is_csv_file(invalid_csv_path), "Invalid CSV file check failed.")

if __name__ == "__main__":
    unittest.main()




