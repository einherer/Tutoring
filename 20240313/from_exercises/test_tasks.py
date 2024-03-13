import os
import unittest
from unittest.mock import patch
from tasks import show_data_list, crea_dirs, classify, DATA_ROOT


class TestFunctions(unittest.TestCase):
    def test_show_data_list_nordir(self):
        self.assertIsNone(show_data_list("nope"))

    def test_show_data_list(self):
        test_dir = os.path.join(DATA_ROOT, "test")
        os.makedirs(test_dir, exist_ok=True)
        with open(os.path.join(test_dir, "test_file.txt"), "w") as f:
            f.write("Test content")

        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output

        show_data_list(test_dir)

        expected_output = f"ls {test_dir}:\ntest_file.txt\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
        os.remove(os.path.join(test_dir, "test_file.txt"))
        os.rmdir(test_dir)

    def test_crea_dirs_exists(self):
        test_dirs = ["..", "."]

        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output
        crea_dirs(test_dirs)

        expected_output = "already exists"
        self.assertIn(expected_output, captured_output.getvalue())
        for dir in test_dirs:
            self.assertTrue(os.path.exists(os.path.join(DATA_ROOT, dir)))

    def test_crea_dirs(self):
        test_dirs = ["test_dir1", "test_dir2"]

        crea_dirs(test_dirs)

        for dir in test_dirs:
            self.assertTrue(os.path.exists(os.path.join(DATA_ROOT, dir)))

        for dir in test_dirs:
            os.rmdir(os.path.join(DATA_ROOT, dir))

    @patch("os.replace")
    def test_move_files(self, mock_replace):
        test_dict = {
            "test_dir1": ["test_file1.txt", "test_file2.txt"],
            "test_dir2": ["test_file3.txt"],
        }

        classify(test_dict)

        mock_replace.assert_called()
        for calls in mock_replace.call_args_list:
            print(calls)

    @patch("os.replace", side_effect=FileNotFoundError)
    def test_move_files_err(self, mock_replace):
        test_dict = {
            "test_dir1": ["test_file1.txt", "test_file2.txt"],
            "test_dir2": ["test_file3.txt"],
        }

        classify(test_dict)

        mock_replace.assert_called()
        for calls in mock_replace.call_args_list:
            print(calls)


if __name__ == "__main__":
    unittest.main()
