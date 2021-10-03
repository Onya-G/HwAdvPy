from unittest import mock, TestCase, main
import Accounting


class TestAccounting(TestCase):

    def test_get_owner_name(self):
        with mock.patch('builtins.input', return_value='10006'):
            self.assertEqual(Accounting.get_doc_owner_name(), 'Аристарх Павлов')
        with mock.patch('builtins.input', return_value='67-98'):
            self.assertEqual(Accounting.get_doc_owner_name(), None)

    @mock.patch('builtins.input', return_value='11-2')
    def test_get_doc_shelf(self, number):
        self.assertEqual(Accounting.get_doc_shelf(), '1')

    @mock.patch('builtins.input', return_value='2207 876234')
    def test_delete_doc(self, number):
        self.assertEqual(Accounting.delete_doc(), ('2207 876234', True))

    def test_add_new_doc(self):
        with mock.patch('builtins.input', side_effect=['1234', 'passport', 'Парфен Семенов', '3']):
            self.assertIn({'type': 'passport', 'number': '1234', 'name': 'Парфен Семенов'}, Accounting.add_new_doc())


if __name__ == '__main__':
    main()
