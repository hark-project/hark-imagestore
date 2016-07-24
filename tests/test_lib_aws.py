from unittest import TestCase
try:
    from unittest.mock import patch, MagicMock
except ImportError:
    from mock import patch, MagicMock

import hark_imagestore.lib.aws


class TestS3Bucket(TestCase):

    @patch('boto3.session.Session.client')
    def test_list(self, mockClient):
        mockS3 = mockClient.return_value
        mockList = mockS3.list_objects_v2
        ret = {
            'Contents': [
                {'Key': 'foo'},
                {'Key': 'foo/bar'},
                {'Key': 'foo/bar/bang'},
                {'Key': 'foo/baz/born'},
                {'Key': 'foo/baz/born/bista'},
            ]
        }
        mockList.return_value = ret

        bucket = hark_imagestore.lib.aws.S3Bucket(
            'myregion', 'mybucket', 'a', 'b')
        mockClient.assert_called_with('s3')

        expect = [o['Key'] for o in ret['Contents']]

        assert bucket.list() == expect

    @patch('boto3.s3.transfer.S3Transfer.upload_file')
    @patch('boto3.session.Session.client')
    def test_put_object(self, mockClient, mockUploadFile):
        key = 'blorsch/fhdsk'
        filename = 'blab'
        bucket_name = 'fjkslj'
        bucket = hark_imagestore.lib.aws.S3Bucket(
            'myregion', bucket_name, 'a', 'b')

        # test with no callback
        bucket.put_object(key, filename, callback=None)
        mockUploadFile.assert_called_with(
            filename, bucket_name, key, callback=None)

        # test with callback
        cb = MagicMock()
        bucket.put_object(key, filename, callback=cb)
        mockUploadFile.assert_called_with(
            filename, bucket_name, key, callback=cb)
