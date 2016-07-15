from unittest import TestCase


class TestHarkImagestoreCLI(TestCase):

    def test_import_hark_imagestore_cli(self):
        from hark_imagestore.cli import hark_imagestore

        assert callable(hark_imagestore)
