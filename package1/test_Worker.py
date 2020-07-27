from unittest import TestCase
from package1.Worker import Worker
from unittest.mock import patch

class TestWorker(TestCase):
    def setUp(self):
        print('setup')
        self.moshe = Worker('Moshe','cohen', 2000, 2, 17, '1 yigal alon,tel aviv', 'il')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        res=self.moshe.full_name()
        self.assertTrue(res=='Moshe cohen')


    def test_age(self):
        pass

    def test_days_to_birthday(self):
        pass

    def test_greet(self):
        pass

    def test_location(self):
        with patch ( 'Worker.requests.get') as mocked_get:
            mocked_get.return_value.ok=True
            mocked_get.return_value.text='success'

            res=self.moshe.location()
            self.assertEqual(res,'success')
            mocked_get.assert_called_with('https://geocode.xyz/?locate=1 yigal alon,tel aviv,il &json=1')
