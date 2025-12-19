"""Test to demonstrate PIL.Image import crash in Python 3.14t."""

import unittest


class TestPILImport(unittest.TestCase):
    """Test case for PIL.Image import."""

    def test_import_pil_image(self):
        """Test importing PIL.Image - this may crash in Python 3.14t."""
        import PIL.Image

        # If we get here without crashing, the import succeeded
        self.assertIsNotNone(PIL.Image)
        print("Successfully imported PIL.Image")


if __name__ == '__main__':
    unittest.main()
