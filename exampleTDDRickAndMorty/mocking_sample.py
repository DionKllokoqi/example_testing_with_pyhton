import unittest
from unittest import mock
from path import current_path
from path import read_file
from io import StringIO


class MockTests(unittest.TestCase):

    def test(self):
        m = mock.Mock()
        assert isinstance(m.field, mock.Mock)
        assert isinstance(m.field2, mock.Mock)
        assert isinstance(m(), mock.Mock)
        assert m.field is not m.field2 is not m()

    def test_fields(self):
        m = mock.Mock()
        m.rubiks = 'code'
        self.assertEqual(m.rubiks, 'code')

        m.configure_mock(tdd='rulez')
        self.assertEqual(m.tdd, 'rulez')

    def test_functions(self):
        m = mock.Mock()
        m.get_eleven.return_value = 11
        self.assertEqual(m.get_eleven(), 11)

    def test_exception(self):
        m = mock.Mock()
        m.thow_exception.side_effect = RuntimeError('Oh no!')

        try:
            m.thow_exception()
        except RuntimeError:
            assert True
        else:
            assert False

    def test_multiple_return(self):
        m = mock.Mock()
        m.get_eleven.return_value = 11

        m.get_eleven.side_effect = [12, 13, 14]
        self.assertEqual(m.get_eleven(), 12)
        self.assertEqual(m.get_eleven(), 13)
        self.assertEqual(m.get_eleven(), 14)

    def test_verify_called_once(self):
        m = mock.Mock()
        m.called_function.return_value = 11
        m.called_function()
        m.called_function.assert_called()

    def test_verify_called_multiple(self):
        m = mock.Mock()
        m.called_function.return_value = 11
        m.called_function()
        m.called_function()
        m.called_function()
        self.assertEqual(m.called_function.call_count, 3)

    def test_reset_mock(self):
        m = mock.Mock()
        m.called_function.return_value = 11
        m.called_function()
        m.called_function()
        m.called_function()
        m.called_function.reset_mock()
        self.assertEqual(m.called_function.call_count, 0)

    def test_patch_import(self):
        with mock.patch('path.os') as os_mocked:
            current_path()
            os_mocked.getcwd.assert_called_once()

    @mock.patch('path.os')
    def test_patch_import2(self, os_mocked):
        current_path()
        os_mocked.getcwd.assert_called_once()

    @mock.patch('path.open')
    def test_patch_context_manager(self, open_mocked):
        open_mocked.return_value.__enter__.return_value = StringIO('test')
        self.assertEqual(read_file(), 'test')


if __name__ == "__main__":
    unittest.main()
