from YaMakeDir import *
from unittest import TestCase, main


class TestYaMakeDir(TestCase):

    def test_make_dir(self):
        self.assertEqual(make_dir('Netology test').status_code, 200)

    def test_make_dir_none(self):
        self.assertEqual(make_dir(None).status_code, 400)

    def test_check_dir_name(self):
        make_dir('Netology test')
        files_list = get_files_list()
        self.assertIn('Netology test', files_list)


if __name__ == '__main__':
    main()
