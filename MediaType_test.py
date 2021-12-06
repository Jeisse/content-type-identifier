import unittest
from src.media_identifier import identifier


class TestIdentifier(unittest.TestCase):
    def test_get_type(self):
        """
        Test that get_Type return the correct identifier
        """
        jpeg_file = "test.jpeg"
        png_file = "test.png"
        no_identifyed = "hshsh"
        media = identifier.MediaType()

        self.assertEqual(media.get_type(jpeg_file), identifier.MediaType.jpeg)
        self.assertEqual(media.get_type(png_file), identifier.MediaType.png)
        self.assertEqual(media.get_type(no_identifyed), "No identified")

if __name__ == '__main__':
    unittest.main()