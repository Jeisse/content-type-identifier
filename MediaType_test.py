import unittest
from src.media_identifier import identifier


class TestIdentifier(unittest.TestCase):
    def test_get_type_when_file_name_valied(self):
        media = identifier.MediaType()
        jpeg_file = "test.jpeg"
        png_file = "test.png"

        self.assertEqual(media.get_type(jpeg_file), identifier.MediaType.jpeg)
        self.assertEqual(media.get_type(png_file), identifier.MediaType.png)

    def test_get_type_when_file_has_substring(self):
        media = identifier.MediaType()
        xlsx_file = "bhbdhbhdb.xlsx"
        tiff_file = "njnjnsj.tiff"

        self.assertEqual(media.get_type(xlsx_file), identifier.MediaType.xlsx)
        self.assertNotEqual(media.get_type(xlsx_file), identifier.MediaType.xls)

        self.assertEqual(media.get_type(tiff_file), identifier.MediaType.tiff)
        self.assertNotEqual(media.get_type(tiff_file), identifier.MediaType.tif)

    def test_get_type_when_file_name_has_string_that_match_media_types_but_are_not_at_the_end(self):
        media = identifier.MediaType()
        file = "bhbd.pnghbhdb"
        file2 = ".jpeg.png"

        self.assertEqual(media.get_type(file), "No identified")
        self.assertEqual(media.get_type(file2), identifier.MediaType.png)

    def test_get_type_when_does_not_identify_file(self):
        media = identifier.MediaType()
        no_identifyed = "hshsh"

        self.assertEqual(media.get_type(no_identifyed), "No identified")

if __name__ == '__main__':
    unittest.main()