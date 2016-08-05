import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from hark_imagestore.imagecache import S3ImageCache
from hark.models.image import Image


class TestS3ImageCache(unittest.TestCase):

    @patch('hark_imagestore.lib.aws.S3Bucket.list')
    def test_images(self, mockList):
        mockList.return_value = [
            'machine_images/built',
            'machine_images/built/Debian-8',
            'machine_images/built/Debian-8/virtualbox',
            'machine_images/built/Debian-8/virtualbox/v1.vmdk',
            'machine_images/built/Debian-8/virtualbox/v2.vmdk',
        ]

        expect = [
            Image(guest='Debian-8', driver='virtualbox', version=1),
            Image(guest='Debian-8', driver='virtualbox', version=2),
        ]

        cache = S3ImageCache('a', 'b')

        l = [dict(**im) for im in cache.images()]
        r = [dict(**im) for im in expect]
        assert l == r

    def test_full_image_path(self):
        im = Image(guest='Debian-8', driver='virtualbox', version=1)
        cache = S3ImageCache('aaa', 'bbbb')
        url = cache.full_image_path(im)
        assert url.startswith('https')
        assert im.s3_path() in url
        assert 'aaa' in url
        assert 'bbb' not in url
