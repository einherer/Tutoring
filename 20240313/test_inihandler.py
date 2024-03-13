import unittest
from pathlib import Path
from tempfile import NamedTemporaryFile

from inihandler import IniHandler


class TestIniHandler(unittest.TestCase):
    def setUp(self):
        # Create a temporary INI file
        self.temp_file = NamedTemporaryFile(delete=False)
        self.temp_file.close()
        self.temp_file_path = self.temp_file.name
        self.handler = IniHandler(self.temp_file_path)

    def tearDown(self):
        # Delete the temporary INI file
        Path(self.temp_file_path).unlink()

    def test_write_and_read(self):
        self.handler.write("section1", "key1", "value1")
        self.assertEqual(self.handler.read("section1", "key1"), "value1")

    def test_read_default(self):
        self.assertEqual(
            self.handler.read(
                "nonexistent_section", "nonexistent_key", "default_value"
            ),
            "default_value",
        )

    def test_read_nonexistent_key(self):
        self.assertEqual(
            self.handler.read("section1", "nonexistent_key"), None)

    def test_readsection(self):
        self.handler.write("section1", "key1", "value1")
        self.handler.write("section2", "key2", "value2")
        self.assertEqual(self.handler.readsection(), "section1;section2")

    def test_delesection(self):
        self.handler.write("section1", "key1", "value1")
        self.assertTrue(self.handler.delesection("section1"))
        self.assertEqual(self.handler.readsection(), "")

    def test_readkeys(self):
        self.handler.write("section1", "key1", "value1")
        self.handler.write("section1", "key2", "value2")
        self.assertEqual(self.handler.readkeys("section1"), "key1;key2")

    def test_readentries(self):
        self.handler.write("section1", "key1", "value1")
        self.handler.write("section1", "key2", "value2")
        self.assertEqual(
            self.handler.readentries("section1"), "key1=value1;key2=value2"
        )

    def test_deletekey(self):
        self.handler.write("section1", "key1", "value1")
        self.assertTrue(self.handler.deletekey("section1", "key1"))
        self.assertEqual(self.handler.readkeys("section1"), "")

    def test_deletekey_nonexistent(self):
        self.assertFalse(
            self.handler.deletekey("nonexistent_section", "nonexistent_key")
        )
